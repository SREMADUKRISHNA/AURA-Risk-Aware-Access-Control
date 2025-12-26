import logging
from config import settings
from models.risk_model import AccessRequest, AccessResponse
from backend.utils.behavior_analyzer import BehaviorAnalyzer
from backend.utils.device_fingerprint import DeviceFingerprint
from backend.utils.geo_anomaly import GeoAnomaly

# Initialize logger
logger = logging.getLogger("aura_logger")

class RiskEngine:
    """
    Orchestrates the risk assessment by aggregating signals from various analyzers.
    """

    def __init__(self):
        self.behavior_analyzer = BehaviorAnalyzer()
        self.device_analyzer = DeviceFingerprint()
        self.geo_analyzer = GeoAnomaly()

    def evaluate_risk(self, request: AccessRequest) -> AccessResponse:
        """
        Main entry point for calculating risk.
        """
        logger.info(f"Starting risk evaluation for user: {request.user_id}")

        # 1. Get Sub-scores
        behavior_score = self.behavior_analyzer.analyze(request.user_id, request.login_time)
        device_score = self.device_analyzer.evaluate(request.device_id, request.ip_address)
        geo_score = self.geo_analyzer.detect(request.location, request.login_time)

        # 2. Calculate Weighted Average
        # Formula: (S1*W1 + S2*W2 + S3*W3) / (W1+W2+W3)
        total_weight = settings.WEIGHT_BEHAVIOR + settings.WEIGHT_DEVICE + settings.WEIGHT_GEO
        
        weighted_sum = (
            (behavior_score * settings.WEIGHT_BEHAVIOR) +
            (device_score * settings.WEIGHT_DEVICE) +
            (geo_score * settings.WEIGHT_GEO)
        )
        
        final_risk_score = weighted_sum / total_weight
        final_risk_score = round(final_risk_score, 2)

        # 3. Make Decision
        decision = self._decide(final_risk_score)
        
        # 4. Generate Reason
        reason = self._generate_reason(decision, behavior_score, device_score, geo_score)

        logger.info(f"Risk evaluation complete. Score: {final_risk_score}, Decision: {decision}")

        return AccessResponse(
            risk_score=final_risk_score,
            decision=decision,
            reason=reason
        )

    def _decide(self, score: float) -> str:
        if score < settings.RISK_THRESHOLD_LOW:
            return settings.DECISION_ALLOW
        elif score <= settings.RISK_THRESHOLD_HIGH:
            return settings.DECISION_STEP_UP
        else:
            return settings.DECISION_BLOCK

    def _generate_reason(self, decision: str, behavior: float, device: float, geo: float) -> str:
        factors = []
        if behavior > 50: factors.append("Behavioral Anomaly")
        if device > 50: factors.append("Untrusted Device")
        if geo > 50: factors.append("Location/Time Anomaly")
        
        if not factors and decision == settings.DECISION_ALLOW:
            return "Trust verification successful. Low risk detected."
        
        return f"{decision} triggered due to: {', '.join(factors)}."

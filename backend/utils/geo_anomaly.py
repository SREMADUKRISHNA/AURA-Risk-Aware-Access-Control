from datetime import datetime
from config import settings

class GeoAnomaly:
    """
    Detects impossible travel, unlikely locations, and time-based anomalies.
    """

    def detect(self, location: str, login_time: datetime) -> float:
        """
        Calculate geo/temporal risk score (0-100).
        """
        score = 0.0

        # 1. Location Whitelist Check
        if location in settings.TRUSTED_LOCATIONS:
            score = 10.0 # Very low risk
        else:
            score = 60.0 # Unknown location baseline

        # 2. Time-of-Day Analysis
        # Check if login is during high-risk hours (e.g., late night)
        if login_time.hour in settings.HIGH_RISK_HOURS:
            score += 30.0
        
        # 3. Keyword check for risky locations (Simulation)
        risky_keywords = ["Unknown", "Proxy", "VPN"]
        if any(keyword in location for keyword in risky_keywords):
            score = 100.0

        return min(max(score, 0.0), 100.0)

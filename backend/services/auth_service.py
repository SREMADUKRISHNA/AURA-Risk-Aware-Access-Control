import logging
import json
from datetime import datetime
from models.risk_model import AccessRequest, AccessResponse

# Initialize logger
logger = logging.getLogger("aura_logger")

class AuthService:
    """
    Handles access logging and auditing.
    In a full system, this would also validate JWTs or credentials.
    """

    @staticmethod
    def log_attempt(request: AccessRequest, response: AccessResponse):
        """
        Logs the detailed access attempt to the centralized audit log.
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "user_id": request.user_id,
            "device_id": request.device_id,
            "ip": request.ip_address,
            "location": request.location,
            "risk_score": response.risk_score,
            "decision": response.decision,
            "reason": response.reason
        }
        
        # Log as structured JSON for easy parsing (e.g., by ELK stack or Splunk)
        logger.info(json.dumps(log_entry))

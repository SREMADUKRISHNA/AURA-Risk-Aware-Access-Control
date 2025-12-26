from fastapi import APIRouter, HTTPException, Depends
from backend.services.risk_engine import RiskEngine
from backend.services.auth_service import AuthService
from models.risk_model import AccessRequest, AccessResponse

router = APIRouter()

# Dependency Injection for RiskEngine
def get_risk_engine():
    return RiskEngine()

@router.post("/access", response_model=AccessResponse)
async def evaluate_access(
    request: AccessRequest, 
    risk_engine: RiskEngine = Depends(get_risk_engine)
):
    """
    Evaluate an access request against zero-trust policies.
    Returns a risk score and an access decision.
    """
    try:
        # 1. Calculate Risk
        response = risk_engine.evaluate_risk(request)
        
        # 2. Log the attempt (Side effect)
        AuthService.log_attempt(request, response)
        
        return response
        
    except Exception as e:
        # In production, we log the stack trace internally and return a generic error
        raise HTTPException(status_code=500, detail=f"Internal Risk Engine Error: {str(e)}")

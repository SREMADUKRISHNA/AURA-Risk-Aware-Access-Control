import random
from config import settings

class BehaviorAnalyzer:
    """
    Analyzes user behavior patterns such as login frequency and historical consistency.
    """
    
    def analyze(self, user_id: str, login_time) -> float:
        """
        Calculate behavior risk score (0-100).
        0 = Normal behavior
        100 = Highly anomalous behavior
        """
        # Logic: 
        # 1. Deterministic check on user_id length (simulation of "unknown user format")
        # 2. Random jitter to simulate real-time ML variance
        
        base_score = 0.0

        # Heuristic: Users with 'admin' in name are higher risk targets
        if "admin" in user_id.lower():
            base_score += 20.0
        
        # Heuristic: Very short user IDs might be bots or test accounts
        if len(user_id) < 5:
            base_score += 40.0
        
        # In a real system, we would query a DB for "last_login" delta.
        # Here we simulate an ML model confidence score.
        # We use a hash of the user_id to make it deterministic for the same user.
        user_hash = sum(ord(c) for c in user_id)
        simulated_history_risk = (user_hash % 20) # 0 to 19
        
        total_score = base_score + simulated_history_risk
        
        return min(max(total_score, 0.0), 100.0)

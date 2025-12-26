import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Logging Configuration
LOG_FILE_PATH = os.path.join(BASE_DIR, "logs", "aura.log")
LOG_LEVEL = "INFO"

# Risk Thresholds
RISK_THRESHOLD_LOW = 30
RISK_THRESHOLD_HIGH = 70

# Risk Weights (Must sum to 1.0 approx for normalized scoring logic, 
# but we will use them as multipliers for sub-scores)
WEIGHT_BEHAVIOR = 0.3
WEIGHT_DEVICE = 0.3
WEIGHT_GEO = 0.4

# Decision Constants
DECISION_ALLOW = "ALLOW"
DECISION_STEP_UP = "STEP_UP_AUTH"
DECISION_BLOCK = "BLOCK"

# Simulation / Mock Settings
# In a real system, these would be in a DB
TRUSTED_LOCATIONS = ["New York, USA", "London, UK", "San Francisco, USA"]
TRUSTED_DEVICE_PREFIX = "TRUSTED-"
HIGH_RISK_HOURS = [0, 1, 2, 3, 4]  # 12 AM to 4 AM

# AURA System Architecture

## 1. Overview
AURA (AI-Based Risk-Aware Access Control) is a Zero Trust security engine designed to move beyond static passwords. It evaluates every access request in real-time based on context, behavior, and device trust.

## 2. Zero Trust Principles
- **Never Trust, Always Verify:** Every request is treated as potential threat until proven otherwise.
- **Continuous Monitoring:** Risk is not static; it is re-evaluated on every transaction.
- **Least Privilege:** Access is granted only when risk is low.

## 3. Component Flow

### 3.1 Input
The system receives a JSON payload containing:
- User Identity
- Device Fingerprint
- Network Context (IP, Location)
- Temporal Context (Time)

### 3.2 Risk Engine (The Core)
The `RiskEngine` orchestrates three specialized analyzers:

1.  **Behavior Analyzer:**
    - Detects anomalies in user ID patterns (mocking historical behavioral analysis).
    - Checks for high-risk user accounts.

2.  **Device Fingerprint:**
    - Evaluates `device_id` against trusted naming conventions.
    - Checks IP reputation (Public vs Private vs Blacklisted logic).

3.  **Geo Anomaly:**
    - Checks for "Impossible Travel" (simulated via Trusted Locations).
    - Analyzes Time-of-Day risk (e.g., 3 AM logins are higher risk).

### 3.3 Weighted Scoring
Scores from analyzers (0-100) are weighted:
- Geo/Time: 40%
- Device: 30%
- Behavior: 30%

### 3.4 Decision Matrix
- **0 - 30 (Low Risk):** ALLOW
- **30 - 70 (Medium Risk):** STEP_UP_AUTH (MFA required)
- **70 - 100 (High Risk):** BLOCK

## 4. Tech Stack
- **Language:** Python 3.10+
- **Framework:** FastAPI (High performance, async)
- **Validation:** Pydantic
- **Logging:** Python Standard Logging (File + Stream)

## 5. Directory Structure
- `backend/`: Core logic and API code.
- `config/`: Centralized settings.
- `logs/`: Audit trails.
- `models/`: Data schemas.

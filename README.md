# AURA: Risk-Aware Access Control System

**Enterprise-Grade Zero Trust Engine**

AURA is an intelligent backend system that evaluates access requests in real-time, assigning a risk score based on behavior, device trust, and geolocation anomalies.

## 🚀 Features
- **Real-time Risk Scoring:** quantitative assessment (0-100) of every login.
- **Dynamic Policy Enforcement:** Automatically allows, challenges (MFA), or blocks users.
- **Pluggable Architecture:** Modular analyzers for Behavior, Device, and Geo context.
- **Audit Logging:** Comprehensive JSON logging for SIEM integration.

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.10+
- Pip

### Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   uvicorn backend.main:app --reload
   ```

## 🔌 API Usage

**Endpoint:** `POST /api/v1/access`

**Request Body:**
```json
{
  "user_id": "alice_admin",
  "device_id": "TRUSTED-PC-01",
  "ip_address": "192.168.1.5",
  "location": "New York, USA",
  "login_time": "2023-10-27T10:00:00Z"
}
```

**Response:**
```json
{
  "risk_score": 10.0,
  "decision": "ALLOW",
  "reason": "Trust verification successful. Low risk detected."
}
```

## 🛡️ Risk Logic
- **Allow:** Risk Score < 30
- **Step-Up Auth:** Risk Score 30 - 70
- **Block:** Risk Score > 70

## 📂 Project Structure
- `backend/`: Source code
- `config/`: Settings and thresholds
- `logs/`: Access logs

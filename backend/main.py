import logging
import sys
from fastapi import FastAPI
from backend.routes import access
from config import settings

# 1. Configure Logging
# Ensure the log directory exists
import os
if not os.path.exists(os.path.dirname(settings.LOG_FILE_PATH)):
    os.makedirs(os.path.dirname(settings.LOG_FILE_PATH))

# Setup root logger to file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(settings.LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout) # Also output to console for 'uvicorn' visibility
    ]
)

# 2. Initialize FastAPI
app = FastAPI(
    title="AURA Risk Engine",
    description="AI-Based Risk-Aware Access Control System",
    version="1.0.0"
)

# 3. Include Routers
app.include_router(access.router, prefix="/api/v1", tags=["Access Control"])

@app.get("/")
def health_check():
    """
    Simple health check endpoint.
    """
    return {"status": "active", "system": "AURA Zero Trust Engine"}

# Entry point check is handled by Uvicorn externally

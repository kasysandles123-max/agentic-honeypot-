import os

API_KEY = os.getenv("API_KEY", "sk_test_123456789")

GUVI_CALLBACK_URL = "https://hackathon.guvi.in/api/updateHoneyPotFinalResult"

SCAM_KEYWORDS = [
    "account blocked",
    "verify",
    "urgent",
    "upi",
    "bank",
    "click link",
    "suspended"
]

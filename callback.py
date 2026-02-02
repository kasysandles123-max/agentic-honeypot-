import requests
from config import GUVI_CALLBACK_URL

def send_final_callback(session_id, data):
    payload = {
        "sessionId": session_id,
        "scamDetected": True,
        "totalMessagesExchanged": len(data["messages"]),
        "extractedIntelligence": data["intelligence"],
        "agentNotes": "Used urgency and payment redirection tactics"
    }

    requests.post(GUVI_CALLBACK_URL, json=payload, timeout=5)

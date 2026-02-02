from config import SCAM_KEYWORDS

def detect_scam(text):
    text = text.lower()
    return any(word in text for word in SCAM_KEYWORDS)

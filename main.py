from fastapi import FastAPI, Request, HTTPException
from config import API_KEY
from scam_detector import detect_scam
from agent import generate_agent_reply
from extractor import extract_intelligence
from memory import get_session
from callback import send_final_callback

app = FastAPI()

@app.post("/honeypot")
async def honeypot(request: Request):
    if request.headers.get("x-api-key") != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")

    body = await request.json()
    session_id = body["sessionId"]
    message = body["message"]["text"]

    session = get_session(session_id)
    session["messages"].append(message)

    if detect_scam(message):
        session["scamDetected"] = True

        intel = extract_intelligence(message)
        for k in intel:
            session["intelligence"][k].extend(intel[k])

        reply = generate_agent_reply(session["messages"])

        if len(session["messages"]) >= 12:
            send_final_callback(session_id, session)

        return {
            "status": "success",
            "scamDetected": True,
            "reply": reply
        }

    return {
        "status": "success",
        "scamDetected": False,
        "reply": "Can you explain more?"
    }
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Agentic Honeypot API Live"}

@app.get("/health")
def health():
    return {"status": "running"}

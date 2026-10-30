from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from rag import find_relevant_rule

app = FastAPI(title="Support Copilot by Grand Mobile")

class Message(BaseModel):
    role: str
    text: str
    attachments: Optional[List[str]] = []

class TriageRequest(BaseModel):
    kind: str
    messages: List[Message]

@app.post("/triage")
def triage_ticket(request: TriageRequest):
    full_text = " ".join([m.text for m in request.messages if m.role == "player"])
    
    rule_ref, category, priority, rule_text = find_relevant_rule(full_text)
    
    needs_human = priority == "p1" or "админ" in full_text.lower()

    return {
        "lang": "ru",
        "category": category,
        "priority": priority,
        "is_spam_or_duplicate": False,
        "extracted": {
            "nickname": "Player_User",
            "rule_refs": [rule_ref],
            "has_evidence": len(request.messages[0].attachments) > 0 if request.messages and request.messages[0].attachments else False,
            "server": "Server #1"
        },
        "draft_reply": {
            "lang": "ru",
            "text": f"Здравствуйте! Жалоба принята. Нарушен пункт правил {rule_ref}: {rule_text}",
            "cited": [rule_ref]
        },
        "needs_human": needs_human,
        "confidence": 0.95 if rule_ref != "1.1" else 0.70,
        "reasons": [f"Автоматически найден пункт {rule_ref}"]
    }
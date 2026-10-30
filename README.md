# Support Copilot by Grand Mobile

**Automated Player Support Triage Service**

Developed for **Decentrathon 6.0**

## About the Project

Support Copilot is a support automation service designed to help gaming support teams process and organize player complaints.

The system analyzes incoming player conversations, identifies the type of issue, assigns a priority level, and finds the corresponding section of the game rules.

Its main purpose is to reduce manual ticket sorting and help support teams identify cases that require human attention.

## Key Features

- **Conversation Analysis** — Processes player messages together to analyze the conversation as a whole.
- **Issue Classification** — Identifies complaints related to cheating, insults, spam, and administrator misconduct.
- **Priority Assignment** — Assigns priority levels (P1, P2, P3) based on predefined matching rules.
- **Human Escalation** — Flags P1 cases and administrator-related requests for human review.
- **Rule Matching** — Matches complaint keywords with predefined game rules and returns the corresponding rule reference.
- **Structured Responses** — Returns classification results, extracted information, and a draft reply in JSON format.

## How It Works

Support Copilot uses a deterministic, keyword-based processing pipeline.

1. **Input:** The API receives a request containing a ticket type and a list of messages.
2. **Message Processing:** Messages written by the player are combined into one text input.
3. **Classification:** The system checks the conversation against predefined keyword rules.
4. **Priority Detection:** A priority level is assigned according to the matched issue category.
5. **Rule Matching:** The corresponding game rule reference and description are returned.
6. **Escalation:** The system flags cases that require human attention.
7. **Output:** A structured JSON response is generated with the classification results and a draft reply.

## Technical Approach

The current MVP uses rule-based text processing rather than external Large Language Models (LLMs).

This approach provides:

- Predictable classification based on predefined conditions.
- Transparent matching logic.
- No dependency on external LLM APIs.
- Consistent JSON response formatting.
- A lightweight backend that can be extended in future versions.

The current implementation uses predefined keyword matching in Python to identify complaint categories and priorities.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| FastAPI | REST API development |
| Pydantic | Request data validation |
| Uvicorn | ASGI server |
| JSON | Structured API communication |

## Project Structure

```text
grand-mobile-copilot/
│
├── main.py       # FastAPI application and /triage endpoint
├── rag.py        # Rule matching and complaint classification
└── README.md     # Project documentation
```

## API Documentation

**Endpoint:** `POST /triage`

The endpoint accepts a ticket containing a list of messages.

### Example Request

```json
{
  "kind": "complaint",
  "messages": [
    {
      "role": "player",
      "text": "Игрок использует читы на сервере",
      "attachments": []
    }
  ]
}
```

### Example Response

```json
{
  "lang": "ru",
  "category": "complaint.cheating",
  "priority": "p1",
  "is_spam_or_duplicate": false,
  "extracted": {
    "nickname": "Player_User",
    "rule_refs": ["5.2"],
    "has_evidence": false,
    "server": "Server #1"
  },
  "draft_reply": {
    "lang": "ru",
    "text": "Здравствуйте! Жалоба принята. Нарушен пункт правил 5.2: Запрещено использование стороннего ПО и читов.",
    "cited": ["5.2"]
  },
  "needs_human": true,
  "confidence": 0.95,
  "reasons": [
    "Автоматически найден пункт 5.2"
  ]
}
```

## Getting Started

### Requirements

- Python 3.10 or newer
- pip

### 1. Clone the repository

```bash
git clone https://github.com/jeannette-de-lune/grand-mobile-copilot.git

cd grand-mobile-copilot
```

### 2. Install dependencies

```bash
pip install fastapi uvicorn pydantic
```

### 3. Start the server

```bash
uvicorn main:app --reload
```

### 4. Open API documentation

Visit:

http://127.0.0.1:8000/docs

Use the interactive Swagger UI to send requests to the `/triage` endpoint and inspect the JSON responses.

## Future Improvements

Potential next steps for the project include:

- Integration with an LLM for more advanced conversation understanding.
- Improved nickname and server information extraction.
- Attachment and evidence analysis.
- Expanded classification rules and configurable knowledge sources.
- Integration with existing player support workflows.

## Project Goal

Support Copilot aims to make player support workflows more organized by automating initial complaint classification, priority assignment, and rule matching.

The current MVP establishes the core processing pipeline, with room for further development and integration into larger support systems.

import os
import sys
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)

# Ensure imports resolve
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from agent import root_agent

# ADK Runner + Session service + GenAI content types
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types as gen_types

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://127.0.0.1",
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        "null",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

APP_NAME = "historical_figure_simulator"
USER_ID = "web_user_1"
SESSION_ID = "web_session_1"

# Create services/runner at module scope
session_service = InMemorySessionService()
runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)

# Ensure the session exists at startup (awaited)
@app.on_event("startup")
async def startup_create_session():
    try:
        existing = await session_service.get_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
        if not existing:
            await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
        logging.info("ADK session is ready: %s", SESSION_ID)
    except Exception:
        logging.exception("Failed to ensure ADK session at startup")

# Minimal request model: message only
class ChatOnly(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatOnly):
    try:
        # Let the router infer persona from the natural-language message
        content = gen_types.Content(role="user", parts=[gen_types.Part(text=req.message)])

        # Run via Runner; it builds InvocationContext internally from session
        events = runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

        reply = ""
        async for ev in events:
            if getattr(ev, "type", "") == "llm_response" and ev.data.get("response"):
                reply = ev.data["response"]
            elif hasattr(ev, "is_final_response") and ev.is_final_response():
                try:
                    reply = ev.content.parts[0].text
                except Exception:
                    pass

        if not reply:
            reply = "No response generated."

        return {"reply": reply}

    except Exception as e:
        logging.exception("Chat endpoint failed")
        return {"reply": f"A server error occurred: {type(e).__name__}: {e}"}

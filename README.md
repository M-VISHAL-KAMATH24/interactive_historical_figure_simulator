**Historical Figure Simulator — Multi‑Agent ADK**
A conversational multi‑agent system built with Google’s Agent Development Kit (ADK) that lets users chat with historically inspired personas. A curator-style router welcomes the user and dynamically transfers control to the right persona (Einstein, Leonardo da Vinci, Cleopatra). Each persona blends creative conversation with factual recall via a dedicated knowledge sub‑agent.

**Key Features**
1. Curator router that greets, interprets intent, and delegates seamlessly to the chosen figure.
2. Persona agents that speak in-character using tailored instructions and style guides.
3. Knowledge sub‑agents that answer factual queries using a curated knowledge base (text files, and extensible to web or databases).
4. Delegation workflow: persona → knowledge agent → persona synthesis, preserving voice and tone.
5. Simple web UI (FastAPI + HTML/CSS) that mirrors the terminal experience: type naturally, switch personas by asking in chat.

**How Delegation Works (Einstein Example)**
1. User asks a question.
2. Router routes to “Albert_Einstein”.
3. The Einstein persona decides:
4. Conceptual/philosophical? Answer directly in character.
5. Factual (dates, papers, equations)? Delegate.
6. knowledge_agent retrieves facts from knowledge_base.txt (extensible to web APIs or databases).
7. Einstein persona merges the facts into a polished, on‑brand reply.

**Run Locally**
# Windows (PowerShell)
py -m venv .venv
.\\.venv\\Scripts\\activate
pip install --upgrade pip
pip install google-adk google-genai fastapi uvicorn pydantic python-dotenv

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

start the backend: uvicorn server:app --reload  and then open index.html live server

**Customization Tips**
1. Edit persona text files (einstein_persona.txt, etc.) to refine style, tone, and constraints.
2. Expand knowledge_base access in knowledge_agent.py (e.g., web search tools, RAG over PDFs, or databases).
3. Add new personas by copying a folder, creating a persona/knowledge pair, and registering the agent in agent.py’s router.

![License](https://img.shields.io/badge/License-Apache--2.0-3a57ff)


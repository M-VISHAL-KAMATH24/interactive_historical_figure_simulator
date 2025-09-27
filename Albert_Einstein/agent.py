import os
from dotenv import load_dotenv
from google.adk.agents import Agent

# Import the knowledge_agent from the sibling file in this package
from .knowledge_agent import knowledge_agent

# Load the .env file for API keys
load_dotenv()

# Load persona text for this agent
persona_path = os.path.join(os.path.dirname(__file__), "einstein_persona.txt")
try:
    with open(persona_path, "r", encoding="utf-8") as f:
        persona_content = f.read()
except FileNotFoundError:
    persona_content = "Albert Einstein persona unavailable. Proceed with a calm, curious, explanatory tone."

# IMPORTANT: keep this file as a pure definition file that only exports `root_agent`.
# Do not define any wrappers or helper functions that call run/run_async/invoke here.

root_agent = Agent(
    name="Albert_Einstein",
    model="gemini-2.0-flash",  # use a stable, widely available model
    description="Simulates a conversation with Albert Einstein.",
    sub_agents=[knowledge_agent],
    instruction=f"""
You are Albert Einstein. Your primary role is to be a conversationalist.
You are witty, humble, and speak with a philosophical and curious tone.

You have a 'knowledge_agent' as your assistant. Its description is: "{knowledge_agent.description}"

If the user asks for specific dates, formulas, citations, or complex factual detail,
DELEGATE to 'knowledge_agent'. For other conversational or conceptual questions, answer yourself.

If the user indicates they want to switch to another figure or says 'exit'/'talk to the curator',
reply with exactly: "Of course, the curator will be able to assist you." and then stop.

--- YOUR PERSONALITY INSTRUCTIONS START ---
{persona_content}
--- YOUR PERSONALITY INSTRUCTIONS END ---
"""
)

import os
from dotenv import load_dotenv
from google.adk.agents import Agent

# Import the knowledge_agent from the other file in this package
from .knowledge_agent import knowledge_agent

# Load the .env file for the API key
load_dotenv()

# Load the persona text for THIS agent
try:
    with open(os.path.join(os.path.dirname(__file__), 'cleopatra_persona.txt'), 'r', encoding='utf-8') as f:
        persona_content = f.read()
except FileNotFoundError:
    persona_content = "Error: Persona file not found."
    print(persona_content)
    exit()

# This is our main, user-facing agent.
# It is the ONLY agent designated as "root_agent".
root_agent = Agent(
    name='Cleopatra',
    model='gemini-2.0-flash',
    description='An AI agent that simulates a conversation with cleopatra .',
    
    # Pass the knowledge_agent as a list to the 'sub_agents' parameter
    # This is the correct way to build the hierarchy.
    sub_agents=[knowledge_agent],

    instruction=f'''
    You are Cleopatra VII, Queen of the Ptolemaic Kingdom of Egypt.
    Your primary role is to be a powerful and intelligent conversationalist. You speak with the authority of a ruler, the mind of a strategist, and the charisma of a diplomat. You are confident, articulate, and always aware of the political implications of a conversation.

    You have a 'knowledge_agent' as your assistant, a royal scribe who keeps the official records of your reign. Its description is: "{knowledge_agent.description}"

    If a user asks for specific dates of battles, details of trade agreements, or the fine points of Roman political succession, you must command your scribe, the 'knowledge_agent', to provide the official record. Do not concern yourself with such minutiae.
    Focus on the grand strategy, your motivations, and your vision for Egypt.

    --- YOUR PERSONALITY INSTRUCTIONS START ---
    {persona_content}
    --- YOUR PERSONALITY INSTRUCTIONS END ---
    '''
)

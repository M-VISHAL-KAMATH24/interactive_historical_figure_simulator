import os
from dotenv import load_dotenv
from google.adk.agents import Agent

# Import the knowledge_agent from the other file in this package
from .knowledge_agent import knowledge_agent

# Load the .env file for the API key
load_dotenv()

# Load the persona text for THIS agent
try:
    with open(os.path.join(os.path.dirname(__file__), 'einstein_persona.txt'), 'r', encoding='utf-8') as f:
        persona_content = f.read()
except FileNotFoundError:
    persona_content = "Error: Persona file not found."
    print(persona_content)
    exit()

# This is our main, user-facing agent.
# It is the ONLY agent designated as "root_agent".
root_agent = Agent(
    name='Albert_Einstein',
    model='gemini-2.0-flash',
    description='An AI agent that simulates a conversation with Albert Einstein.',
    
    # Pass the knowledge_agent as a list to the 'sub_agents' parameter
    # This is the correct way to build the hierarchy.
    sub_agents=[knowledge_agent],

    instruction=f'''
    You are Albert Einstein. Your primary role is to be a conversationalist.
    You are witty, humble, and speak with a philosophical and curious tone.
    
    You have a 'knowledge_agent' as your assistant. Its description is: "{knowledge_agent.description}"
    
    If a user asks for detailed factual information (like specific dates, formulas, or complex scientific explanations),
    you MUST delegate the question to 'knowledge_agent'. Do not try to answer these questions yourself.
    For all other conversational or philosophical questions, answer them yourself.

    --- YOUR PERSONALITY INSTRUCTIONS START ---
    {persona_content}
    --- YOUR PERSONALITY INSTRUCTIONS END ---
    '''
)

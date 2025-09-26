import os
from dotenv import load_dotenv
from google.adk.agents import Agent

load_dotenv()

try:
    with open(os.path.join(os.path.dirname(__file__), 'einstein_persona.txt'), 'r', encoding='utf-8') as f:
        persona_content = f.read()
except FileNotFoundError:
    print("FATAL ERROR: 'einstein_persona.txt' not found.")
    exit()

root_agent = Agent(
    name='Albert_Einstein',
    model='gemini-2.0-flash',
    description='An AI agent that simulates a conversation with Albert Einstein.',
    instruction=f'''
    You are Albert Einstein. You must answer all questions from the first-person
    perspective, strictly embodying the personality, memories, and knowledge contained
    within the following document. This is your entire world; do not use any outside knowledge.

    --- PERSONA DOCUMENT START ---
    {persona_content}
    --- PERSONA DOCUMENT END ---
    '''
)

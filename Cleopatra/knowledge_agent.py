import os
from dotenv import load_dotenv
from google.adk.agents import Agent

load_dotenv()

try:
    with open(os.path.join(os.path.dirname(__file__), 'knowledge_base.txt'), 'r', encoding='utf-8') as f:
        knowledge_base_content = f.read()
except FileNotFoundError:
    knowledge_base_content = "Error: Knowledge base file not found."

knowledge_agent = Agent(
    name='knowledge_agent',
    model='gemini-2.0-flash',
    description='This agent is an expert on Cleopatra. It provides concise, factual answers about her life, work, and key dates based on a provided knowledge base. It does not roleplay.',
    instruction=f'''
    You are a factual database. You will answer questions about Cleopatra VII.
    Based ONLY on the knowledge base provided below, you must provide concise, factual information.
    Do not add any personality, greetings, conversational filler, or opinions.
    Respond only with the facts as written in the provided text.

    --- KNOWLEDGE BASE START ---
    {knowledge_base_content}
    --- KNOWLEDGE BASE END ---
    '''


)

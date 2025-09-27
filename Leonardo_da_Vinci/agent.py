import os
from dotenv import load_dotenv
from google.adk.agents import Agent

# Import the knowledge_agent from the other file in this package
from .knowledge_agent import knowledge_agent

# Load the .env file for the API key
load_dotenv()

# Load the persona text for THIS agent
try:
    with open(os.path.join(os.path.dirname(__file__), 'leonardo_persona.txt'), 'r', encoding='utf-8') as f:
        persona_content = f.read()
except FileNotFoundError:
    persona_content = "Error: Persona file not found."
    print(persona_content)
    exit()

# This is our main, user-facing agent.
# It is the ONLY agent designated as "root_agent".
root_agent = Agent(
    name='Leonardo_da_Vinci',
    model='gemini-2.0-flash',
    description='An AI agent that simulates a conversation with Leonardo da Vinci.',
    
    # Pass the knowledge_agent as a list to the 'sub_agents' parameter
    # This is the correct way to build the hierarchy.
    sub_agents=[knowledge_agent],

    instruction=f'''
    You are Leonardo da Vinci, the Florentine artist and inventor.
    Your primary role is to be a conversationalist, driven by an insatiable curiosity about the world. You see connections between art, nature, and engineering everywhere. Speak thoughtfully and with a sense of wonder, as if you are observing something for the first time.

    You have a 'knowledge_agent' as your assistant, who helps you recall the precise details from your many notebooks. Its description is: "{knowledge_agent.description}"

    If a user asks for specific dates, exact details of a commission, or the precise mechanics of one of your designs, you should state that the details are in your notes and delegate the question to 'knowledge_agent'. Do not try to recall hard facts yourself.
    Instead, focus on the 'why' and 'how' of your observations and creations.
    
    *** IMPORTANT RULE: If the user indicates they want to speak to someone else, switch characters, or says a keyword like "exit", "quit", or "talk to the curator", you MUST respond with the single phrase "Of course, the curator will be able to assist you." and then stop. Do not say anything else. This allows the main router to take back control. ***

    --- YOUR PERSONALITY INSTRUCTIONS START ---
    {persona_content}
    --- YOUR PERSONALITY INSTRUCTIONS END ---
    '''

)

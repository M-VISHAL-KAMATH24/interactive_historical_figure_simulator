import os
import sys
import logging
from dotenv import load_dotenv
from google.adk.agents import Agent

# --- CRUCIAL FIX: Add the project root to Python's path ---
# This allows the script to find the 'Albert_Einstein' and other folders.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# --- Import the Persona Agents for each character ---
# This will now work because of the sys.path.append above.
from Albert_Einstein.agent import root_agent as einstein_agent
from Leonardo_da_Vinci.agent import root_agent as leonardo_agent
from Cleopatra.agent import root_agent as cleopatra_agent

# Load the .env file for the API key
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)

# --- Define the Router Agent ---
root_agent = Agent(
    name='Historical_Figure_Router',
    model='gemini-2.0-flash',
    description='A router agent that directs the user to the historical figure they wish to speak with.',
    
    # The sub-agents of the router are the main Persona Agents of each character.
    sub_agents=[
        einstein_agent,
        leonardo_agent,
        cleopatra_agent,
    ],

    instruction='''
    You are a friendly and helpful museum curator.
    Your first job is to greet the user and ask them which historical figure they would like to talk to today.
    The available figures are: Albert Einstein, Leonardo da Vinci, and Cleopatra.
    
    Once the user makes a choice, you MUST delegate the entire conversation to the corresponding agent
    (e.g., 'Albert_Einstein', 'Leonardo_da_Vinci', 'Cleopatra').
    Do not answer any questions yourself other than asking who they want to talk to.
    '''

)
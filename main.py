import os
from dotenv import load_dotenv
from google.adk.agents import Agent

# --- Import the Persona Agents for each character ---
# The ADK will automatically handle their sub-agents (the knowledge agents)
from Albert_Einstein.agent import root_agent as einstein_agent
from Leonardo_da_Vinci.agent import root_agent as leonardo_agent
from Cleopatra.agent import root_agent as cleopatra_agent

# Load the .env file for the API key
load_dotenv()

# --- Define the Router Agent ---
# This is now our main, top-level agent for the whole application.
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)

root_agent = Agent(
    name='Historical_Figure_Router',
    model='gemini-1.5-flash',
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

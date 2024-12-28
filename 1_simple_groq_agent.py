'''
from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

# This function expects .env file and when this function is called it will create environment variable called GROQ_API_KEY
#  and save that key here

load_dotenv()

# Use the required model

agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile")
)

agent.print_response("Write 2 sentence poem for children")'''
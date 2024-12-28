from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

# This function expects .env file and when this function is called it will create environment variable called GROQ_API_KEY
#  and save that key here

load_dotenv()

# Use the required model

agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price = True, analyst_recommendations = True, stock_fundamentals = True)],
    show_tool_calls=True, # internally when it retrievs information we can be able to see them
    markdown=True,
    instructions=["Use tables to display data"]
)

agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA")
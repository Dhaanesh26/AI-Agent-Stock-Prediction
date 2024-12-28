import os
import logging
from pathlib import Path

from phi.agent import Agent
from phi.model.groq import Groq
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.playground import Playground, serve_playground_app
from groq import Client

logging.basicConfig(level=logging.INFO)

# Securely load API key
client = Client(api_key=os.getenv("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"))

# Database file path
db_file_path = Path(__file__).parent / "agents.db"

# Define agents
web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    storage=SqlAgentStorage(table_name="web_agent", db_file=str(db_file_path)),
    add_history_to_messages=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    storage=SqlAgentStorage(table_name="finance_agent", db_file=str(db_file_path)),
    add_history_to_messages=True,
    markdown=True,
)

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set or is empty.")
client = Client(api_key=api_key)

# Initialize app
try:
    app = Playground(agents=[finance_agent, web_agent]).get_app()
except Exception as e:
    logging.error(f"Error initializing the playground: {e}")
    raise

# Serve app
if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
client = Client(api_key="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")

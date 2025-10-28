from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
import openai

import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

##web search agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="search the web for information",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[DuckDuckGo()],
    instructions=["always use the sources"],
    show_tools_calls=True,
    markdown=True,
)

## financial agent
finance_agent=Agent(
    name="Financial Agent",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[YFinanceTools(stock_fundamentals=True, stock_price=True, analyst_recommendations=True,company_news=True),],
    instructions=["always use tables to display data","always use the sources"],
    show_tools_calla=True,
    markdown=True,

)

multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    instructions=["always use the sources","use web search agent for web search queries","use table to display data"],
    show_tools_calls=True,
    markdown=True,  
)

multi_ai_agent.print_response("summarize analyst recommendations and share the latest news for NVDA and AAPL and also give a buy or sell recommendation for both the stocks",stream=True)
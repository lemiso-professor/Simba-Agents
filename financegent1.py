import os
from dotenv import load_dotenv
from pydantic_ai import Agent
import asyncio
from yfinance_tools import YFinanceTools

# Load environment variables from .env file
load_dotenv()

# Initialize the agent with the desired model
agent = Agent('openai:gpt-4o')

# Initialize YFinanceTools
finance_tools = YFinanceTools()

# Function to fetch stock information
async def fetch_stock_info(ticker):
    stock_info = finance_tools.get_stock_info(ticker)
    return stock_info

# Asynchronous execution example
async def main():
    # Prompt the user for a question
    user_question = input('Please enter your finance question (e.g., stock price for AAPL): ')

    # Check if the question is about stock information
    if 'stock price' in user_question.lower():
        ticker = user_question.split()[-1]  # Extract ticker from the question
        stock_info = await fetch_stock_info(ticker)
        print(f'The stock information for {ticker} is: {stock_info}')
    else:
        result = await agent.run(user_question)
        print(result.output)  # Output the answer only once

# To run the asynchronous main function
asyncio.run(main())

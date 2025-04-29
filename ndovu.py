import os
from dotenv import load_dotenv
from pydantic_ai import Agent
import asyncio

# Load environment variables from .env file
load_dotenv()

# Initialize the agent with the desired model
agent = Agent('openai:gpt-4o')

# Prompt the user for a question
user_question = input('I am Ndovu AI, Your personal Assistant\nPlease enter your question: ')

# Function for synchronous execution
result_sync = agent.run_sync(user_question)
print(result_sync.output)  # Output the answer

# Asynchronous execution example
async def main():
    result = await agent.run(user_question)
    print(result.output)  # Output the answer only once

# To run the asynchronous main function
asyncio.run(main())

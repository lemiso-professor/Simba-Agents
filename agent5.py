import os
from dotenv import load_dotenv
from pydantic_ai import Agent

# Load environment variables from .env file
load_dotenv()

# Initialize the agent with the desired model
agent = Agent('openai:gpt-4o')

# Prompt the user for a question
user_question = input('Please enter your question: ')

# Synchronous execution example
result_sync = agent.run_sync(user_question)
print(result_sync.output)  # Output the answer

# Asynchronous execution example
async def main():
    result = await agent.run(user_question)
    print(result.output)  # Output the answer

    async with agent.run_stream(user_question) as response:
        print(await response.get_output())  # Output the answer

# To run the asynchronous main function
import asyncio
asyncio.run(main())

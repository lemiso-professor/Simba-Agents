from pydantic_ai import Agent
import os
from dotenv import load_dotenv

load_dotenv()
# Initialize the agent with the desired model
agent = Agent('openai:gpt-4o')

# Synchronous execution example
result_sync = agent.run_sync('What is the capital of Italy?')
print(result_sync.output)  # Output: Rome

# Asynchronous execution example
async def main():
    result = await agent.run('What is the capital of France?')
    print(result.output)

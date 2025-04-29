from google.adk.agents import Agent, LlmAgent
from google.adk.tools import google_search

# Define the agent
root_agent = Agent(
    name="search_assistant",
    model="gemini-2.0-flash",
    instruction="You are a helpful assistant. Answer user questions using Google Search when needed.",
    description="An assistant that can search the web.",
    tools=[google_search]
)

# Function to interact with the user
def interact_with_user():
    print("Welcome to the Search Assistant! Ask me anything or type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Use the agent to process the input and get a response
        response = root_agent.call(user_input)  # Use the appropriate method to get a response
        print(f"Assistant: {response}")

# Start interaction
interact_with_user()

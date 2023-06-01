from classifier import CustomAgent
from langchain.agents import Tool
from memory_store import write_to_json

def create_classifier(tools=[]):
    # Initialize the CustomAgent with any necessary tools
    agent = CustomAgent(tools)

    # Return the agent
    return agent

tools = [
    Tool(
        name = "Search",
        func= write_to_json,
        description="useful for when you need to answer questions about current events"
    )
]
classifier = create_classifier(tools)

def get_classifier():
    return classifier

def restart_classifier():
    classifier.restart()

def intake(conversation):
    classifier.intake(classifier, conversation)


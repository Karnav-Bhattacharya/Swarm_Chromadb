import pandas as pd
from sentence_transformers import SentenceTransformer
import chromadb
from swarm import Agent, Swarm
from swarm.repl import run_demo_loop
import os

# Enter your Openai api key here
os.environ['OPENAI_API_KEY'] = 'Enter You Key Here'

data = pd.read_csv('Emergency_contacts.csv')
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Combine Position and Name for better search results
descriptions = data['Position'] + " - " + data['Name']
embeddings = embedding_model.encode(descriptions.tolist())

# Set up Chroma database
client = chromadb.Client()
collection = client.create_collection(name="emergency_data")

# Add data to the collection
for i, (desc, row) in enumerate(zip(descriptions, data.itertuples())):
    collection.add(
        ids=[str(i)],
        embeddings=[embeddings[i].tolist()],
        metadatas=[{
            "description": desc,
            "position": row.Position,
            "name": row.Name,
            "phone": row._4
        }]
    )

# Creating and Defining Agents
def query_csv_agent(query):
    """An agent function that searches the CSV using embeddings."""
    embedding = embedding_model.encode([query])[0]
    results = collection.query(query_embeddings=[embedding.tolist()], n_results=3)

    if results["metadatas"]:
        responses = []
        for metadata in results["metadatas"][0]:
            responses.append(f"Position: {metadata['position']}, Name: {metadata['name']}, Phone: {metadata['phone']}")
        return {"response": "Closest matches:\n" + "\n".join(responses)}
    else:
        return {"response": "No relevant data found."}

csv_agent = Agent(
    name="CSV Agent",
    instructions="You immediately help users query CSV data by finding relevant rows based on their input.",
    functions=[query_csv_agent]
)

def transfer_to_csv_agent():
    """Transfer queries related to contact information to csv_agent"""
    return csv_agent

user_interface_agent = Agent(
    name="User Interface Agent",
    instructions="You are a user interface agent that handles all interactions with the user. Call this agent for general questions and when no other agent is correct for the user query.",
    functions=[transfer_to_csv_agent],
)

user_interface_agent.functions.append(transfer_to_csv_agent)

if __name__ == "__main__":
    run_demo_loop(user_interface_agent, stream=True)

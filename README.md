# Swarm_Chromadb
This project demonstrates how to build an emergency contact search system using sentence embeddings and a simple agent-based interface.

How It Works:
The user enters a query (e.g., "Need Aryabhatta Warden contact").
The input query is transformed into an embedding using the same sentence transformer model.
ChromaDB finds the closest matching emergency contact entries using embedding similarity.
The CSV Agent returns the matching contact information.
You can ask generic questions and interact to the user_interface_agent.
When you require specific information from the csv, it will handoff to the csv_agent.

![{5B2DA5A1-E9BB-4F85-AB82-1F087198DB9A}](https://github.com/user-attachments/assets/b00729b8-5982-43c4-811b-cabc3c4c2f6f)


# Requirements:
Python 3.x
sentence-transformers
chromadb
swarm
pandas
A valid OpenAI API key

# Files:
main.py: The main script containing all the logic to load data, create embeddings, set up ChromaDB, and define the agents.
Emergency_contacts.csv: The CSV file containing the emergency contact data. The CSV should have columns for Position, Name, and Phone number.

# Instructions:

1) Clone the Repository:
2) Install Swarm (not yet listed in requirements.txt): pip install git+https://github.com/openai/swarm.git
3) Install Dependencies: Install all required Python libraries using the following command:

Copy code
```pip install -r requirements.txt```

4) Set Up OpenAI API Key: Replace the placeholder in the code (os.environ['OPENAI_API_KEY']) with your actual OpenAI API key.

(Optional)Add Emergency Contact Data: For this example I have added the Emergency Contacts from SWB Sheet. You may add your emergency contacts to the Emergency_contacts.csv file with the appropriate columns.

# Run the Application:
You can run the system by typing... in cmd:

```
python main.py
```
Thanks

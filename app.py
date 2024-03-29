import os
import json
from dotenv import load_dotenv
from openai import OpenAI
# Load environment variables from .env file
load_dotenv()

# Now access the API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Configure the model ID. Change this to your model ID.
model = "ft:gpt-3.5-turbo-0125:learninggpt::97U2upri"

def extract_last_message(json_strings):
    for json_string in json_strings:
        data = json.loads(json_string)
        last_message_content = data['messages'][-1]['content'].strip()
        print(last_message_content)


# Returns a drug class for each drug

json_strings = [
        '{"messages": [{"role": "system", "content": "You are professional drug classifier."}, {"role": "user", "content": "Drug: A CN Gel(Topical) 20gmA CN Soap 75gm\\nMalady"}, {"role": "assistant", "content": " 0"}]}',
        '{"messages": [{"role": "system", "content": "You are profesional drug classifier."}, {"role": "user", "content": "Drug: Provake 100mg Tablet 10SProvake 200mg Tablet 10S\\nMalady"}, {"role": "assistant", "content": " 1"}]}',
        '{"messages": [{"role": "system", "content": "You are profesional drug classifier."}, {"role": "user", "content": "Drug: 1 AL Plus Capsule 10S1 AL 10mg Tablet 15S1 AL 5mg Tablet 10S1 AL Max Tablet 10S1 AL Syrup 30ml\\nMalady"}, {"role": "assistant", "content": " 2"}]}',
    ]

extract_last_message(json_strings)
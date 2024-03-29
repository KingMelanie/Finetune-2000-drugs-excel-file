from openai import OpenAI
import os


client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file


FINE_TUNED_MODEL="ft:babbage-002:learninggpt::97xSaVZt"
YOUR_PROMPT="What is the remote for?"

response = client.completions.create(
    model=FINE_TUNED_MODEL,
    prompt=YOUR_PROMPT,

    temperature = 0.5,
    max_tokens=25,

)

result = response.choices[0].text.strip()
print(result)


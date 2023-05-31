import openai
import os
from dotenv import load_dotenv


# Load .env file
load_dotenv()

# Get API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_embedding(text, model="text-embedding-ada-002"):
    response = openai.Embedding.create(model=model, input=text)
    return response["data"][0]["embedding"]


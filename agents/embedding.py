import openai

openai.api_key = "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"


def get_embedding(text, model="text-embedding-ada-002"):
    response = openai.Embedding.create(model=model, input=text)
    return response["data"][0]["embedding"]


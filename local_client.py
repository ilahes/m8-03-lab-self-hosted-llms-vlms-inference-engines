import time
from openai import OpenAI

# Local model served by Ollama
MODEL = "llama3.2:3b"

# Ollama exposes an OpenAI-compatible HTTP API on localhost.
# This means the client code has the same general shape as a hosted LLM API call:
# we create a client, choose a model, send messages, and receive a generated response.
# The difference is that the base_url points to my own machine instead of a cloud provider.
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # dummy value; Ollama does not require a real API key
)

prompt = "Explain what an inference engine does in exactly two sentences."

start = time.time()

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a concise assistant."},
        {"role": "user", "content": prompt}
    ]
)

elapsed = time.time() - start

print("Model:", MODEL)
print("Prompt:", prompt)
print("\nResponse:")
print(response.choices[0].message.content)
print(f"\nElapsed time: {elapsed:.2f} seconds")
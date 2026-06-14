"""
Task 3 — Ask a local VLM (moondream) about sample_chart.png via Ollama.

Make sure Ollama is running and you have pulled moondream:
    ollama pull moondream

Then run:
    python vlm_local.py
"""

import base64
import time
from openai import OpenAI

# Same local endpoint as Task 2 — same shape, different model
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

IMAGE_PATH = "sample_chart.png"
QUESTION = "Describe what this chart shows. What are the main values or trends visible?"


def load_image_as_base64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def main() -> None:
    print(f"Loading image: {IMAGE_PATH}")
    image_data = load_image_as_base64(IMAGE_PATH)

    print(f"Asking moondream: {QUESTION}\n")
    start = time.time()

    response = client.chat.completions.create(
        model="llava",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_data}"
                        },
                    },
                    {
                        "type": "text",
                        "text": QUESTION,
                    },
                ],
            }
        ],
    )

    elapsed = time.time() - start
    answer = response.choices[0].message.content

    print("Moondream answer:")
    print(answer)
    print()
    print(f"Time taken: {elapsed:.2f}s")
    print()
    print("Paste this answer into self_hosting_report.md under Task 3.")


if __name__ == "__main__":
    main()

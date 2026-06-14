import requests

MODELS = ["llama3.2:3b", "qwen2.5:0.5b"]

PROMPT = "Explain what an inference engine does in exactly two sentences."

for model in MODELS:
    print(f"\n=== {model} ===")

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": PROMPT,
            "stream": False
        }
    )

    data = response.json()

    answer = data.get("response", "")
    load_time_s = data.get("load_duration", 0) / 1_000_000_000
    eval_time_s = data.get("eval_duration", 0) / 1_000_000_000
    tokens = data.get("eval_count", 0)

    tokens_per_sec = tokens / eval_time_s if eval_time_s > 0 else 0

    print("Answer:")
    print(answer)
    print()
    print(f"Load time: {load_time_s:.2f} s")
    print(f"Output tokens: {tokens}")
    print(f"Tokens/sec: {tokens_per_sec:.2f}")
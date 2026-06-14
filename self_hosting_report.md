# Self-Hosting Report

## Task 1 — Benchmark two local models

The same prompt was used for both models:

> Explain what an inference engine does in exactly two sentences.

RAM usage was checked from Windows Task Manager while the models were running.

| Model        | Approx size / quant | Load time (s) | Tokens/sec | RAM used | Quality note                                                                                                          |
| ------------ | ------------------- | ------------- | ---------- | -------- | --------------------------------------------------------------------------------------------------------------------- |
| llama3.2:3b  | 3B / Q4_K_M         | 10.21         | 27.18      | 0.93 GB  | Gave a clearer and more accurate answer, and followed the two-sentence instruction better.                            |
| qwen2.5:0.5b | 0.5B / Q4_K_M       | 2.63          | 112.75     | 0.44 GB  | Gave an understandable answer, but it was less concise and did not follow the exact two-sentence requirement as well. |

**Trade-off observed:**

> The smaller `qwen2.5:0.5b` model loaded faster and generated text much faster than `llama3.2:3b`. However, `llama3.2:3b` gave a clearer and more accurate answer, while `qwen2.5:0.5b` was less concise and did not follow the two-sentence instruction as well. This shows the trade-off between speed/resource usage and answer quality.

---

## Task 2 — Hit the local endpoint from Python

`local_client.py` sends a chat request to Ollama's OpenAI-compatible endpoint at:

> http://localhost:11434/v1

The script uses the `openai` Python SDK, but the `base_url` points to my local Ollama server instead of a cloud API. The API key is set to `"ollama"` only as a dummy value, because Ollama does not require a real API key when it runs locally.

This shows that calling a local model has the same general structure as calling a hosted model: create a client, choose a model, send messages, and read the generated response. The main difference is that the model runs on my own machine instead of a remote server.

---

## Task 3 — VLM: local comparison

Image used: `sample_chart.png`

Task performed: visual question answering / chart understanding.

Prompt given to both models:

> Describe what this chart shows. What are the main values or trends visible?

Since I did not use a Gemini API key, I used the lab fallback option and compared two local VLMs: `moondream` and `llava`.

| System                     | Answer (short summary)                                                                                                                                                  | Speed   | Cost                |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------- |
| Local VLM — moondream      | Gave a very general description of a bar chart about computer/device speeds and boot or switch-on time, but it did not identify exact values clearly.                   | 12.51s  | Free / runs locally |
| Local VLM — llava fallback | Gave a much longer and more detailed answer. It tried to explain the chart values, model names, and trends, but some interpretation seemed uncertain or over-explained. | 111.59s | Free / runs locally |

**Comparison:**

> Moondream was much faster, but its answer was very short and missed most of the chart details. Llava was much slower, but it produced a more detailed response and attempted to explain the visible values and trend. Both models were free to run locally, so the main trade-off was speed versus detail: moondream was faster, while llava gave a richer answer but took much longer.

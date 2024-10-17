from openai import OpenAI
from ollama import Client
import re
import tiktoken

openai_client = OpenAI(api_key="") # Use your API key here
ollama_client = Client(host="http://localhost:11444")

def ask(questions, model, port=None):
    is_gpt = "gpt" in model

    if not is_gpt and port is not None:
        ollama_client = Client(host=f"http://localhost:{port}")

    api = ollama_client.chat if not is_gpt else openai_client.chat.completions.create

    response = api(
        model=model,
        messages=[
            {"role": "user", "content": question}
            for question in questions
        ]
        # temperature=0
    )

    answer = response.choices[0].message.content if is_gpt else response["message"]["content"]
    return answer

def take_out_number(answer):
    return int(re.findall(r'\b\d+\b', answer)[-1])

def count_token(model, prompt):
    tokenizer = tiktoken.encoding_for_model(model)
    return len(tokenizer.encode(prompt))
import sys
sys.path.insert(1, "../..")

from utils.llm_api import *
import random


def ask_key_values(key_values, model, golden_key):
    prompt = "The following is a list of (key, value) pairs. For each key there is an associated value.\n"
    prompt += "\n".join(str(key_value) for key_value in key_values)
    prompt += "\n"
    prompt += f"Give me the average of values associated to the key {golden_key}. Give a number without furthur explanation."

    try:
        response = take_out_number(ask(question=prompt, model=model))
    except IndexError:
        response = 0

    return response, prompt

def build_key_values(length, window_size, key_list):
    result = []
    for i in range(length):
        key_index = i // window_size
        key = key_list[key_index]
        result.append((
            key, int(random.random() * 10**3)
        ))

    return result

def get_average_values(key_values, key):
    focus = [kv[1] for kv in key_values if kv[0] == key]
    return sum(focus) / len(focus)
import random
import re

pattern = r"\('?(\D)'?: ?(\d+)\)"

def make_random_prompt(token_length, letters):
    each = [i for i in letters]
    random.shuffle(each)
    prompt = []
    window = token_length // (len(each) - 1)
    for i in range(token_length):
        index = i // window
        prompt.append(each[index])
    return " ".join(prompt)

def get_letter_counts(response):
    result = re.findall(pattern, response)
    return [(x, int(y)) for x, y in result] # ('A': 10)

def get_gt(prompt, letter):
    return prompt.count(letter)

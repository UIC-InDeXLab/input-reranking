def reshape(prompt, batch_size):
    result = []
    for i in range(0, len(prompt), batch_size):
        result.append(prompt[i:i + batch_size])
    return result
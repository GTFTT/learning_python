
def func(val1: set, val2: str) -> str:
    val1.add("Test")

    return f'Result: {val2*10}'

print(func(set(), '#'))
import re

def extract_and_multiply(memory):
    # Regular expression to find valid `mul(X, Y)` instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, memory)
    total = sum(int(x) * int(y) for x, y in matches)
    return total


if __name__ == '__main__':
    with open('input.txt') as f:
        text = f.read()
        print(extract_and_multiply(text))
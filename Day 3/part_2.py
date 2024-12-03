import re

def extract_and_multiply(memory):
    # Regular expressions for `mul`, `do`, and `don't` instructions
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    tokens = re.split(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", memory)
    print(tokens)
    enabled = True  # Start with `mul` instructions enabled
    total = 0  # Total sum of enabled multiplications
    
    for token in tokens:
        token = token.strip()
        
        if re.match(do_pattern, token):
            enabled = True  # Enable `mul` instructions
        elif re.match(dont_pattern, token):
            enabled = False  # Disable `mul` instructions
        elif match := re.match(mul_pattern, token):
            if enabled:  # Process `mul` only if enabled
                x, y = map(int, match.groups())
                total += x * y
    
    return total

if __name__ == '__main__':
    with open('input.txt') as f:
        text = f.read()
        print(extract_and_multiply(text))
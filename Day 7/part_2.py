from itertools import product

def evaluate_left_to_right(numbers, operators):
    """Evaluate the expression left-to-right given numbers and operators."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            # Concatenate numbers as strings and convert back to int
            result = int(str(result) + str(numbers[i + 1]))
    return result

def find_valid_equations(input_data):
    total_calibration_result = 0

    for line in input_data:
        target, *numbers = map(int, line.replace(':', '').split())
        num_slots = len(numbers) - 1

        # Generate all combinations of operators, including concatenation
        operator_combinations = product(['+', '*', '||'], repeat=num_slots)

        # Check each combination
        for operators in operator_combinations:
            if evaluate_left_to_right(numbers, operators) == target:
                total_calibration_result += target
                break  # No need to check further combinations for this equation

    return total_calibration_result




if __name__ == '__main__':
    with open('input.txt') as f:
        text = f.read()
        input_data = text.strip().splitlines()
        total = find_valid_equations(input_data)
        print(total)


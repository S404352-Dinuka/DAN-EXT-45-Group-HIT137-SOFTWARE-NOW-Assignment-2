"""
HIT137 Assignment 2 - Question 2
Expression Evaluator
"""
'''
Implemented this method to converts the input expression string into a list of tokens
'''
def convert_expression_to_tokens(expression):
    output = []
    current_idx = 0
    expression_length = len(expression)
    while current_idx < expression_length:
        current_character = expression[current_idx]
        if current_character.isdigit():
            num = current_character
            current_idx += 1
            while current_idx < expression_length and expression[current_idx].isdigit():
                num = num + expression[current_idx]
                current_idx += 1
            output.append(("NUM", int(num)))
            continue
        elif current_character in "+-*/":
            output.append(("OP", current_character))
        elif current_character == "(":
            output.append(("LPAREN", current_character))
        elif current_character == ")":
            output.append(("RPAREN", current_character))
        elif current_character.isspace():
            current_idx += 1
            continue
        else:
            return "ERROR"
        current_idx += 1
    output.append(("END", None))
    return output

'''
Implemented this method to read expressions from the input file and writes results to out put file
This method return a dictionary list
'''
def evaluate_file(input_path: str) -> list[dict]:
    results = []
    try:
        with open(input_path, "r") as f:
            lines = f.readlines()
        output_path = "output.txt"
        with open(output_path, "w") as out:
            for line in lines:
                expression0 = line.strip()
                tokens = convert_expression_to_tokens(expression0)
    except FileNotFoundError as e:
        print(e)
    return results


if __name__ == "__main__":
    # This block runs only when this file is executed directly.
    # It is useful for simple local testing during development.
    results = evaluate_file("input.txt")
    print("Check the output.txt")

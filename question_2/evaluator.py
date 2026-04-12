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
Implemented this method to parse numbers parentheses and unary minus
'''
def parse_sub_expression(tokens, index):
    if index < len(tokens):
        token_type, token_value = tokens[index]
        # Check if token type is Number
        if token_type == "NUM":
            return token_value, index + 1
        # Check if token type is Unary negation
        elif token_type == "OP" and token_value == "-":
            node, next_index = parse_sub_expression(tokens, index + 1)
            if node == "ERROR":
                return "ERROR", next_index
            else:
                return ("neg", node), next_index
        # Check if token type is Parentheses
        elif token_type == "LPAREN":
            node, next_index = parse_expression(tokens, index + 1)
            if node == "ERROR":
                return "ERROR", next_index
            if next_index >= len(tokens) or tokens[next_index][0] != "RPAREN":
                return "ERROR", next_index
            return node, next_index + 1
        else:
            return "ERROR", index
    else:
        return "ERROR", index

'''
Implemented this method to parse * and / operations
'''
def parse_precedence_expression(tokens, index):
    expression, next_index = parse_sub_expression(tokens, index)
    if expression != "ERROR":
        while next_index < len(tokens) and tokens[next_index][0] == "OP" and tokens[next_index][1] in ("*", "/"):
            operator = tokens[next_index][1]
            right_expression, next_index = parse_sub_expression(tokens, next_index + 1)
            if right_expression == "ERROR":
                return "ERROR", next_index
            expression = (operator, expression, right_expression)
        return expression, next_index
    else:
        return "ERROR", next_index

'''
Implemented this method to parse + and - operations
'''
def parse_expression(tokens, index):
    expression, next_index = parse_precedence_expression(tokens, index)
    if expression != "ERROR":
        while next_index < len(tokens)  and tokens[next_index][1] in ("+", "-") and tokens[next_index][0] == "OP":
            operator = tokens[next_index][1]
            right_expression, next_index = parse_precedence_expression(tokens, next_index + 1)
            if right_expression == "ERROR":
                return "ERROR", next_index
            expression = (operator, expression, right_expression)
        return expression, next_index
    else:
        return "ERROR", next_index

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
                print(tokens)
                if tokens == "ERROR":
                    tree = "ERROR"
                    result = "ERROR"
                else:
                    tree_node, next_index = parse_expression(tokens, 0)
                    print(tree_node, next_index)
    except FileNotFoundError as e:
        print(e)
    return results


if __name__ == "__main__":
    # This block runs only when this file is executed directly.
    # It is useful for simple local testing during development.
    results = evaluate_file("input.txt")
    print("Check the output.txt")

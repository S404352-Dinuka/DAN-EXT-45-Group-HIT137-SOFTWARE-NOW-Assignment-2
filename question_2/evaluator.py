"""
HIT137 Assignment 2 - Question 2: Expression Evaluator

This file is the starting point for Question 2 of the assignment

The goal of this question is to build a mathematical expression evaluator that:
- reads expressions from an input file
- tokenizes each expression into numbers, operators, and parentheses
- parses expressions using recursive descent parsing
- builds an expression tree
- evaluates the final result
- handles invalid input and runtime errors
- writes output in the exact format required by the assignment

At this stage this is only the initial project setup.
The full tokenizing, parsing, tree generation, evaluation, and output formatting
logic will be added in later commits

Main planned components:
1. Tokeniser
2. Recursive descent parser
3. Expression tree builder
4. Expression evaluator
5. Output formatter
"""


def evaluate_file(input_file_path: str):
    """
    Reads mathematical expressions from the given input file and returns
    a list of results.

    This is the required function for Question 2

    Parameters:
        input_file_path (str): The path of the input file that contains one
        mathematical expression per line

    Returns:
        list[dict]: A list of dictionaries containing the processed results
        for each expression.

    Note:
        This is only the initial skeleton for the assignment.
        The full implementation will be added in later commits.
    """
    # Placeholder return value for the initial setup commit.
    # Later, this function will read the input file, process each expression,
    # and return the final structured results.
    return []


if __name__ == "__main__":
    # This block runs only when this file is executed directly.
    # It is useful for simple local testing during development.
    results = evaluate_file("sample_input.txt")
    print(results)
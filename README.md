# HIT137 Assignment 2 – README

## Group Members
- Dinuka Dhaneshani Mathangaweera – S404352   
- Sehan Hansaja Udayakantha Panik Mudiyanselage – S401456
- Balatripurasundari Polineni – S401680 
- Prabodha Sathsarani Aththanayake Aththanayake Boralage – S401279
---

# 🐍 Python Version Requirement

This project requires **Python 3.9 or above**.

This is because the implementation uses built-in generic type hints such as:

def evaluate_file(input_path: str) -> list[dict]:

The list[dict] syntax is only supported in Python 3.9 and later versions.

---

# Overview

This assignment consists of two parts:

- **Question 01** – File encryption, decryption, and verification  
- **Question 02** – Arithmetic expression evaluator using recursive descent parsing  

All solutions are implemented using plain functions (no classes).

---

# Question 01 – File Encryption & Decryption

## Description
This program reads a text file, encrypts its content using custom shifting rules, decrypts the encrypted file, and verifies whether the decrypted text matches the original.

## Files Used
- raw_text.txt → original input file  
- encrypted_file.txt → encrypted output  
- decrypted_file.txt → decrypted output  

## Key Methods
- check_letters() → calculates shift logic and stores mappings  
- encrypt_file() → encrypts content and writes to file  
- decrypt_file() → decrypts using stored mappings  
- verification() → compares original and decrypted files  

## Features
- Handles uppercase and lowercase letters  
- Uses multiple shifting rules  
- Maintains mapping for accurate decryption  
- Includes error handling  

---

# Question 02 – Expression Evaluator

## Description
This program reads mathematical expressions from a text file, evaluates them, and writes results to an output file.

## Features
- Supports +, -, *, /  
- Handles nested parentheses  
- Supports unary negation  
- Detects invalid expressions  

## Program Flow
Input → Tokenization → Parsing → Expression Tree → Evaluation → Output

## Key Methods
- convert_expression_to_tokens()  
- parse_sub_expression()  
- parse_precedence_expression()  
- parse_expression()  
- generate_result()  
- convert_tokens_to_string()  
- convert_tree_to_string()  
- format_result_for_output()  
- evaluate_file()  

## Output Format
Input: 3 + 5  
Tree: (+ 3 5)  
Tokens: [NUM:3] [OP:+] [NUM:5] [END]  
Result: 8  


---

# Error Handling
- Invalid expressions → ERROR  
- Division by zero → ERROR  
- File errors handled using try/except  

---

# Conclusion
This assignment demonstrates file handling, parsing, and evaluation using clean modular functions.

import sys
import sys
from getpass import getpass

"""
input_variables.py

Comprehensive notes and examples on Python variables and input handling.

This file contains:
- Explanations (as comments) of variable concepts, naming rules, types, mutability.
- Many small, runnable examples showing how to read input from users,
      convert types, validate input, parse multiple values, and handle errors.
- Patterns for interactive programs and also for reading from redirected input.

Usage:
- Read the examples and run the file to see interactive prompts.
- Import functions for use in other scripts.

Author: GitHub Copilot
"""

# ---------------------------
# VARIABLES: BASIC CONCEPTS
# ---------------------------
# - A variable is a name that refers to an object in memory.
# - Python is dynamically typed: you don't declare variable types.
# - Assignment binds a name to an object:
#     x = 10
# - Reassigning changes the binding:
#     x = "hello"
# - Naming rules: letters, digits, underscores; cannot start with a digit.
# - By convention: UPPER_CASE for constants, lower_case_with_underscores for variables.
# - Use descriptive names. Avoid single-letter names except in short loops.
# - Use type() to inspect an object's type and isinstance() to check it.

# Example:
x = 10
print("x =", x, "type:", type(x))
x = "now a string"
print("x =", x, "type:", type(x))

# ---------------------------
# BASIC INPUT: input()
# ---------------------------
# - input(prompt) reads a line from standard input (stdin) as a string.
# - Always returns a str (in Python 3).
# - Use int(), float(), bool conversion as needed.
#
# Simple example:
def greet():
            name = input("Enter your name: ")  # returns string
            print(f"Hello, {name}!")

# ---------------------------
# TYPE CONVERSION
# ---------------------------
# - Convert user input using int(), float(), complex(), bool(), str(), etc.
# - Conversion can raise ValueError if input is not in the right format.
# - Use try/except to handle invalid input.

def read_int(prompt="Enter an integer: "):
            raw = input(prompt)
            n = int(raw)  # may raise ValueError
            return n

def safe_int_input(prompt="Enter an integer: "):
            while True:
                        raw = input(prompt)
                        try:
                                    return int(raw)
                        except ValueError:
                                    print("Invalid integer. Please try again.")

# ---------------------------
# MULTIPLE VALUES FROM ONE LINE
# ---------------------------
# Common patterns: split(), map(), list comprehension.
# Example: user enters "10 20 30"

def read_ints_split(prompt="Enter integers separated by spaces: "):
            raw = input(prompt)
            parts = raw.split()            # split by whitespace
            nums = [int(p) for p in parts] # list comprehension with conversion
            return nums

def read_ints_map(prompt="Enter integers separated by spaces: "):
            raw = input(prompt)
            nums = list(map(int, raw.split()))  # map + list
            return nums

# Unpacking directly into variables (must match count):
def read_two_ints(prompt="Enter two integers separated by space: "):
            a, b = map(int, input(prompt).split())
            return a, b

# ---------------------------
# CSV OR OTHER DELIMITERS
# ---------------------------
def read_csv_line(prompt="Enter comma-separated values: "):
            raw = input(prompt)
            values = [v.strip() for v in raw.split(",")]  # handle spaces around commas
            return values

# ---------------------------
# SAFE PARSING WITH DEFAULTS
# ---------------------------
# Provide a default if user presses Enter:
def input_with_default(prompt, default):
            raw = input(f"{prompt} (default: {default}): ").strip()
            return raw if raw != "" else default

# ---------------------------
# VALIDATION EXAMPLES
# ---------------------------
def read_positive_int(prompt="Enter a positive integer: "):
            while True:
                        try:
                                    n = int(input(prompt))
                                    if n > 0:
                                                return n
                                    print("Must be positive.")
                        except ValueError:
                                    print("Invalid integer.")

# ---------------------------
# READING MULTILINE INPUT
# ---------------------------
# - For interactive input until blank line:
def read_multiline(prompt="Enter lines, finish with an empty line:"):
            print(prompt)
            lines = []
            while True:
                        line = input()
                        if line == "":
                                    break
                        lines.append(line)
            return lines

# - For batch programs (e.g., competitive programming), often you read all input:
def read_all_tokens():
            # Note: sys.stdin.read() can be used when input is redirected from a file.
            data = sys.stdin.read().split()
            return data

# ---------------------------
# BOOLEANS AND TRUTHINESS
# ---------------------------
# Converting user input to boolean commonly uses checks:
def yes_no(prompt="Continue? (y/n): "):
            ans = input(prompt).strip().lower()
            return ans in ("y", "yes", "1", "true", "t")

# ---------------------------
# MUTABILITY & ASSIGNMENT BEHAVIOR
# ---------------------------
# - Immutable types: int, float, bool, str, tuple. Rebinding creates new objects.
# - Mutable types: list, dict, set; modifying in-place affects all references.
# Example:
a = [1, 2, 3]
b = a
b.append(4)
print("a after b.append:", a)  # shows the change

# ---------------------------
# ADVANCED: UNPACKING AND STAR
# ---------------------------
# You can unpack an arbitrary number of inputs:
def read_numbers_unpack(prompt="Enter numbers: "):
            parts = input(prompt).split()
            a, *rest = parts  # a gets first token, rest gets the list of remaining tokens
            return a, rest

# ---------------------------
# PARSING WITH MAP AND GENERATORS
# ---------------------------
# Use generator expressions to avoid creating extra lists:
def sum_of_ints(prompt="Enter integers to sum: "):
            nums = map(int, input(prompt).split())  # nums is an iterator
            return sum(nums)

# ---------------------------
# EXAMPLES FOR TYPICAL TASKS
# ---------------------------
# 1) Read N integers and print their sum (handles whitespace)
def sum_n_numbers():
            n = int(input("How many numbers? "))
            print("Enter the numbers (space or newline separated):")
            # Read until we have n numbers (works for both single line and multiple lines)
            tokens = []
            while len(tokens) < n:
                        tokens.extend(input().split())
            nums = list(map(int, tokens[:n]))
            print("Sum:", sum(nums))

# 2) Read a line and parse as float
def read_float(prompt="Enter a float: "):
            return float(input(prompt))

# 3) Password input (no echo)
def secret_input(prompt="Password: "):
            # getpass hides the input; useful for passwords
            try:
            except ImportError:
                        return input(prompt)
            return getpass(prompt)

# ---------------------------
# TYPE CHECKING AND INTROSPECTION
# ---------------------------
# Use type() and isinstance() to inspect variables
def show_type(value):
            print(repr(value), "has type", type(value), "isinstance int?", isinstance(value, int))

# ---------------------------
# EXAMPLES DEMONSTRATING ERRORS & HANDLING
# ---------------------------
def demo_invalid_conversion():
            s = input("Enter something to convert to int (demo): ")
            try:
                        print("Converted:", int(s))
            except ValueError:
                        print("Cannot convert to int:", s)

# ---------------------------
# README-LIKE SUMMARY (short)
# ---------------------------
# - Use input() to read strings.
# - Convert using int(), float(), etc. Wrap conversions in try/except.
# - For multiple values in one line, use split() + map() or list comprehension.
# - For interactive validation, use loops prompting until valid.
# - Remember mutability semantics and naming conventions.

# ---------------------------
# QUICK INTERACTIVE DEMO
# ---------------------------
if __name__ == "__main__":
            print("--- Quick demo of input and variables ---")
            greet()
            age = safe_int_input("Enter your age: ")
            print("You entered age =", age, "type:", type(age))
            numbers = read_ints_map("Enter some integers separated by spaces: ")
            print("Numbers:", numbers)
            print("Sum of numbers:", sum(numbers))
            if yes_no("Do you want to enter a multiline note? (y/n): "):
                        note = read_multiline()
                        print("Your note (lines):", note)
            pwd = secret_input("Enter a secret (it won't echo if supported): ")
            print("Secret length:", len(pwd))
            print("Demo finished.")
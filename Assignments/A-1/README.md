# Python Algorithmic Programming B - Exercise 1

## Assignment Overview

This is a "warm-up" exercise designed to familiarize you with the Python programming language, focusing on syntax and Object-Oriented Programming (OOP). 

## Task Description

You are provided with an interface `Expression` in the `parser.py` file, which defines a function for calculating a mathematical expression.

Your task is to implement the following classes according to the provided diagram:

- **`Num`**: Represents a number.
- **`BinExp`**: Represents a binary expression.
- **`Plus`**: Represents addition.
- **`Minus`**: Represents subtraction.
- **`Mul`**: Represents multiplication.
- **`Div`**: Represents division.

### Parser Implementation

Next, you need to implement the `parser` function, which, given a string containing a mathematical expression, returns its result.

#### Example:

```python
parser('5+(4-1)*3')  # should return 14
```

## Assumptions:

- You can assume the expression is valid.
- The parser should behave like Python's built-in eval function, which evaluates expressions but without using eval.
  
## Restrictions:

- You are not allowed to use the eval function; instead, you must implement the parser manually.
  
## Suggested Approach:

- You may use the Shunting Yard Algorithm to create instances of the classes mentioned above according to the mathematical expression and return its result.
- Shunting Yard Algorithm

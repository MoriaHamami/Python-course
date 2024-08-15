# Python Algorithmic Programming B - Exercise 1: Syntax and OOP

## Overview

This project is a solution to an assignment from the **Python Algorithmic Programming** course. The task serves as an introductory exercise to Python, specifically focusing on syntax and Object-Oriented Programming (OOP) concepts.

In this project, I implemented a parser that can evaluate basic mathematical expressions without using Python's built-in `eval` function. The solution involves creating a set of classes that represent different components of a mathematical expression and a parser function that processes these expressions using the Shunting Yard Algorithm.

## Class Implementations

The core of the project revolves around the implementation of several classes, each representing a component of a mathematical expression:

- **`Num`**: Represents a numerical value in the expression.
- **`BinExp`**: A base class for binary expressions (e.g., addition, subtraction).
- **`Plus`**: Represents an addition operation.
- **`Minus`**: Represents a subtraction operation.
- **`Mul`**: Represents a multiplication operation.
- **`Div`**: Represents a division operation.

These classes work together to build a tree-like structure of the mathematical expression, which can then be evaluated to produce the final result.

## Parser Function

### Implementation Details

The `parser` function is the centerpiece of this project. Given a string containing a mathematical expression, it returns the result of the expression. The function mimics the behavior of Python's `eval` function but is implemented from scratch.

### Example Usage

Here’s how the `parser` function works:

```python
result = parser('5+(4-1)*3')
print(result)  # Output: 14
```

## Key Features

- **`Expression Validation`**: The parser assumes that the input expression is valid.
- **`Custom Evaluation`**: Instead of using the eval function, the parser constructs the expression using the implemented classes and evaluates it using the Shunting Yard Algorithm.

## Shunting Yard Algorithm

To correctly parse and evaluate the expressions, I utilized the **Shunting Yard Algorithm**, which is efficient in converting infix expressions (like the ones provided in the string) to postfix expressions, which are easier to evaluate.

The algorithm is used to manage the precedence and associativity of operators in the expression, ensuring the correct order of operations.

## File Structure

- **`parser.py`**: Contains the implementation of all the classes and the `parser` function.

## How to Run

1. Clone the repository.

2. Ensure Python 3.9.7 or a compatible version is installed.

3. Run the `MainTrain.py` file:

## Conclusion

This project demonstrates a practical application of Python's OOP capabilities to solve a common problem—parsing and evaluating mathematical expressions. The custom implementation of the parser, without relying on `eval`, showcases a deeper understanding of expression handling in programming.

## Requirements

- Python 3.9.7


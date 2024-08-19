# Functional Programming and Divide and Conquer - Python Algorithmic Programming 

## Assignment Overview

This project is a solution to **Exercise 3** in the **Python Algorithmic Programming** course. The tasks focus on applying functional programming principles and the divide-and-conquer algorithm to solve problems efficiently.

## Table of Contents

- [Question 1: Functional Programming and Divide and Conquer](#question-1-functional-programming-and-divide-and-conquer)
  - [Task Description](#task-description)
  - [Example Usage](#example-usage)
- [Question 2: Divide and Conquer - Maximum Area Histogram](#question-2-divide-and-conquer---maximum-area-histogram)
  - [Task Description](#task-description-1)
  - [Example Usage](#example-usage-1)
- [Conclusion](#conclusion)

## Question 1: Functional Programming and Divide and Conquer

### Task Description

In this task, you are required to implement the `dnc` function in the `dnc.py` file. This function should return a new function based on the provided `base` and `combine` functions, using the divide-and-conquer strategy. Specifically, the returned function will:

- Divide the input array recursively into halves (divide).
- When a single element is reached, the result of applying the `base` function to it will be returned.
- On exiting the recursion, the `combine` function will be applied to the results of the two halves.

This approach allows us to create functions that can compute, for example, the maximum or minimum value in an array using the divide-and-conquer method.

### Example Usage

Here's how you can use the `dnc` function to find the maximum and minimum values in an array:

```python
import random

mx = dnc(lambda x: x, lambda x, y: max(x, y))
mn = dnc(lambda x: x, lambda x, y: min(x, y))

arr = [random.randint(-10, 10) for i in range(1024)]
print(mx(arr))  # Returns the maximum value in the array
print(mn(arr))  # Returns the minimum value in the array

```
## Question 2: Divide and Conquer - Maximum Area Histogram

### Task Description

In this task, you are required to implement the `maxAreaHist` function. Given an array representing a histogram, the function should return the maximum rectangular area that can be formed using consecutive columns in O(n log n) time.

For example, for the histogram represented by the array `[6, 2, 5, 4, 5, 1, 6]`, the function should return `12` (4 + 4 + 4), which is the maximum area that can be formed by adjacent heights of histogram bars.

### Example Usage

Here’s an example of how to use the `maxAreaHist` function:

```python
arr = [6, 2, 5, 4, 5, 1, 6]
print(maxAreaHist(arr))  # Should return 12
```
## Conclusion

This project demonstrates the application of functional programming and divide-and-conquer strategies to solve complex problems efficiently. By breaking down problems into smaller sub-problems, we were able to implement solutions with optimal time complexity.

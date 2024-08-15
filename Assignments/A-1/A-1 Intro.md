# Stream Class Implementation in Python

## Assignment Overview

This project is a solution to an assignment from the **Algorithmic Programming B** course by Dr. Eliyahu Chaleschi, focusing on parallel programming and functional programming techniques in Python.

The task involves implementing a `Stream` class that operates in a multi-threaded environment while allowing the use of functional programming paradigms. This implementation is particularly aimed at creating a workflow where data can be processed in a pipeline, with each step operating in parallel.

## Features of the Stream Class

### Core Concepts

- **Thread Management**: Each `Stream` object is associated with its own list and thread. The thread is initiated in the constructor but remains idle until there is data in the list and a function to process it.

- **Data Processing**: The thread processes elements from the list one by one, applying the defined function to each element. When the list is empty, the thread goes back to a waiting state.

### Methods

1. **`add(item)`**: Adds an element to the list of the `Stream`.

2. **`forEach(func)`**: Accepts a consumer-like function that processes each element in the list. This function does not return anything and is primarily used for side effects (e.g., printing, logging).

3. **`apply(func)`**: Accepts a function that returns a value. This method processes each element and returns a new `Stream` object:
    - If the function returns `True` for an element `x`, the element is passed to the new `Stream` (similar to `filter`).
    - If the function returns a value `y`, this value is passed to the new `Stream` (similar to `map`).

4. **`stop()`**: Immediately stops the thread associated with the `Stream` object and gradually stops all chained `Stream` objects.

### Example Usage

The following is an example of how to use the `Stream` class with fluent programming and lambda expressions:

```python
s.apply(lambda x: x % 2 == 0).apply(lambda x: x * 10).forEach(f)
```

In this example:

- The first apply filters out all odd numbers.
- The second apply multiplies each remaining number by 10.
- The forEach method then processes each number with the function f.

### Workflow Design

This design allows users to define a series of operations (a pipeline) before any data is received. Data flows through each "station" (step in the pipeline) in parallel with the others, where the output of one station becomes the input to the next.

## Installation and Setup

1. Clone the repository.
   
3. Ensure Python 3.9.7 or a compatible version is installed.

4. Run the `stream.py` file to test the functionality.

## Contributing

This project is an individual assignment and does not accept contributions.

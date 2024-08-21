# Traveling Salesman Problem (TSP) - Genetic Algorithm Solution

## Overview
This project provides a solution to the Traveling Salesman Problem (TSP) using a Genetic Algorithm (GA). The goal is to find the shortest possible route that visits a set of cities (represented as points on a 2D plane) exactly once and returns to the starting city. The TSP is a well-known NP-complete problem, and in this implementation, I approximate the solution using the principles of genetic algorithms.

## Problem Statement
Given a list of cities (2D points), the objective is to determine the cheapest (shortest) route that visits each city exactly once and returns to the starting point. The distance between any two cities is calculated using the Euclidean distance formula. The genetic algorithm is designed to find a path with a cumulative minimum distance, without concern for the starting or ending city.

## Genetic Algorithm Approach
The genetic algorithm used in this solution follows these main steps:

1. **Initialization**: A random population of possible routes (individuals or chromosomes) is generated.
2. **Selection**: The most fit individuals, i.e., those with the shortest routes, are selected to create the next generation.
3. **Crossover (Reproduction)**: Selected individuals "mate" to produce offspring, inheriting characteristics from both parents.
4. **Mutation**: A small subset of the population undergoes random changes to introduce diversity and prevent the algorithm from getting stuck in a local optimum.

These steps are iteratively repeated until a predetermined number of iterations has been reached.

## Implementation
The core logic of the genetic algorithm is implemented in the `solve` function in the `tsp_ga.py` file. This function takes an array of `points` and returns the best route found by the genetic algorithm.

### Requirements
- Python 3.x
- `numpy` (for numerical operations)

### Running the Code
1. Ensure that all dependencies are installed.
2. Run the `MainTrain.py`.

```bash
python MainTrain.py
```

### Evaluation
The solution found by the genetic algorithm will be tested against a random algorithm's output. The GA solution should consistently outperform the random solution by a significant margin.

## Conclusion
This project demonstrates the use of genetic algorithms to solve complex optimization problems like the TSP. While not guaranteed to find the optimal solution, the GA provides a robust and efficient method for approximating the shortest route for visiting all cities.

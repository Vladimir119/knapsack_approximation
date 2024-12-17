# Knapsack Approximation Project

## Overview
This project focuses on solving the **Knapsack Problem**, a classic optimization problem. It includes both an exact solution and a polynomial-time approximation scheme (PTAS) for achieving a solution with a guaranteed approximation error of \( \varepsilon \).

### Knapsack Problem Statement
Given:
- A set of \( n \) items, each with:
  - Weight \( w[i] \)
  - Value \( c[i] \)
- A maximum weight capacity \( W \) of the knapsack.

Find a subset of items \( M \) such that:
- The total weight of items in \( M \) does not exceed \( W \).
- The total value of items in \( M \) is maximized.

Mathematically:
\[
\text{maximize } \sum_{x \in M} c(x), \quad \text{subject to } \sum_{x \in M} w(x) \leq W.
\]

### Polynomial-Time Approximation Scheme (PTAS)
The PTAS implemented in this repository provides a solution that is within a factor of \( (1 + \varepsilon) \) of the optimal solution. It uses **value scaling** to reduce the size of the search space, ensuring that the algorithm runs in polynomial time with respect to \( n \) and \( \frac{1}{\varepsilon} \).

### Exact Solution
For comparison, an exact solution is implemented using dynamic programming, which ensures the optimal result but may not scale efficiently for large \( n \).

## Repository Structure
```
knapsack_approximation/
|-- src/
|   |-- base_knapsack
|       |-- np_knapsack.py                   # Contains base algorithm
|   |-- approximation_knapsack
|       |-- approximation_knapsack.py        # Contains the approximation algorithm
|-- tests/
|   |-- unit.py                              # Tests
|-- tex/
|   |-- desc.tex                             # tex file sources
|-- requirements.txt                         # Dependencies
|-- desc.pdf                                 # Theoretical description of the product
|-- README.md                                # This file
```

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/knapsack-approximation.git
   cd knapsack-approximation
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests:
   ```bash
   chmod +x start.sh
   ./start.sh
   ```
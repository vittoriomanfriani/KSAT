# **K-SAT Solver using Simulated Annealing**

This project implements a solver for the **K-Satisfiability (K-SAT)** problem using **Simulated Annealing**. The K-SAT problem is a classical NP-complete problem in computer science and mathematics. The goal is to determine whether there exists an assignment of boolean variables that satisfies all given logical clauses.

This repository includes:
- An implementation of the K-SAT problem generator.
- A Simulated Annealing-based solver.
- Analysis tools to evaluate the solver's performance and identify the algorithmic threshold.

---

## **Features**
- **K-SAT Problem Generator**: Generates random K-SAT instances with configurable numbers of variables, clauses, and literals per clause.
- **Simulated Annealing Solver**: 
  - A probabilistic optimization algorithm to find satisfying assignments.
  - Includes detailed configuration options (annealing schedule, Monte Carlo steps, etc.).
- **Algorithmic Threshold Analysis**:
  - Empirical analysis to determine the number of clauses where the probability of solving the problem drops to 50%.
- **Performance Tracking**:
  - Tracks metrics like acceptance rate, solution quality, and computational cost.

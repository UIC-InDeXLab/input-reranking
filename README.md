# Rank It, Then Ask It: Input Reranking for Maximizing the Performance of LLMs on Symmetric Tasks

## Overview

This project implements the methodology and experiments discussed in the paper. It explores how input reranking improves the performance of Large Language Models (LLMs) on symmetric tasks. The repository is organized into several subdirectories and files for clarity and modularity.

---

## Repository Structure

### 1. `./figures`
Contains plots and reports generated for the paper. These visuals illustrate the experimental results, trends, and key insights.

### 2. `./data`
Contains CSV files with the results of experiment runs. These include raw and processed data used for analysis.

### 3. `./tasks`
Task-specific code and notebooks are organized here. Each subdirectory corresponds to a different task:

#### a. `./tasks/db`
Handles the **Query Database Task**:
- `db_queries:1.ipynb`: Executes the first part of the algorithm, where relevance estimations are obtained from helper models and inputs are ranked accordingly.
- `db_queries:2.ipynb`: Executes the second part, where reranked inputs are queried using the LLM.

#### b. `./tasks/graph`
Handles the **Graph Degree Task**:
- Contains two notebooks similar to `./tasks/db`, focusing on reranking and querying for graph-related tasks.

### 4. `utils`
Contains utility implementations:
- Bipartite algorithm for reranking.
- Functions for making API calls to interact with LLMs.

### 5. `initial_observation.ipynb`
A standalone notebook that measures the LLM's output error for varying graph sizes in the **Graph Degree Task**. Provides baseline insights for the experiments.

---

## Citation
```
@article{dehghankar2024rank,
  title={Rank It, Then Ask It: Input Reranking for Maximizing the Performance of LLMs on Symmetric Tasks},
  author={Dehghankar, M. and Asudeh, A.},
  journal={arXiv preprint arXiv:2412.00546},
  year={2024}
}
```

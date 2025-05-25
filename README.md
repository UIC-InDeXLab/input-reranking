# Rank It, Then Ask It: Input Reranking for Maximizing the Performance of LLMs on Symmetric Tasks

## Overview

This project implements the methodology and experiments discussed in the paper. It explores how input reranking improves the performance of Large Language Models (LLMs) on symmetric tasks. The repository is organized into several subdirectories and files for clarity and modularity.

### Citation
```
@inproceedings{dehghankar2025rank,
  author    = {Dehghankar, Mohsen and Asudeh, Abolfazl},
  title     = {Rank It, Then Ask It: Input Reranking for Maximizing the Performance of LLMs on Symmetric Tasks},
  booktitle = {Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 (KDD '25)},
  year      = {2025},
  isbn      = {979-8-4007-1454-2/2025/08},
  doi       = {10.1145/3711896.3737099},
  publisher = {Association for Computing Machinery},
  address   = {Toronto, ON, Canada},
  month     = {August 3--7},
  url       = {https://doi.org/10.1145/3711896.3737099}
}
```

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

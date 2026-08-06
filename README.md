# Graph Database Cloud Benchmark

## Project Overview

This project benchmarks graph database performance using a common dataset and identical Cypher workloads. The goal is to compare query latency and benchmark reproducibility across graph database platforms.

## Databases Benchmarked

- Neo4j Community Edition
- CognoDB Cloud

> The benchmark framework is designed so additional graph databases can be added using the same workloads.

---

# Dataset

Dataset Name:
SNAP Soc-Pokec Social Network

Source:
https://snap.stanford.edu/data/soc-pokec.html

Relationships Loaded:
100,000

Load Method:
Python Batch Loader using Neo4j Driver

---

# Environment

Operating System:
Windows 11

Language:
Python 3

Driver:
Neo4j Python Driver

Database:
Neo4j Community Edition

Cloud Database:
CognoDB Cloud (Free Tier)

---

# Benchmark Queries

### 1-Hop Traversal

```cypher
MATCH (p:Person)-[:KNOWS]->(friend)
RETURN p.id, friend.id
LIMIT 100
```

### 2-Hop Traversal

```cypher
MATCH (p:Person)-[:KNOWS]->()-[:KNOWS]->(friend)
RETURN p.id, friend.id
LIMIT 100
```

### 3-Hop Traversal

```cypher
MATCH (p:Person)-[:KNOWS]->()-[:KNOWS]->()-[:KNOWS]->(friend)
RETURN p.id, friend.id
LIMIT 100
```

### Aggregation

```cypher
MATCH (p:Person)
RETURN count(p)
```

### Point Lookup

```cypher
MATCH (p:Person {id:$id})
RETURN p
```

---

# Benchmark Methodology

- Same dataset loaded into each database.
- Same Cypher queries executed.
- Warm-up runs before benchmarking.
- 100 benchmark iterations per workload.
- Measured:
  - Average latency
  - P50 latency
  - P95 latency

---

# Neo4j Results

| Benchmark | Average (ms) | P50 (ms) | P95 (ms) |
|-----------|-------------:|---------:|----------:|
| 1-Hop Traversal | 351.160 | 307.362 | 336.374 |
| 2-Hop Traversal | 520.278 | 402.397 | 708.081 |
| 3-Hop Traversal | 440.266 | 433.784 | 581.876 |
| Aggregation | 386.957 | 373.232 | 514.436 |
| Point Lookup | 323.879 | 312.909 | 364.876 |

---

# CognoDB Results

| Benchmark | Average (ms) | P50 (ms) | P95 (ms) |
|-----------|-------------:|---------:|----------:|
| 1-Hop Traversal | 394.034 | 315.257 | 700.424 |
| 2-Hop Traversal | 399.513 | 311.197 | 613.892 |
| 3-Hop Traversal | 442.185 | 368.418 | 613.359 |
| Aggregation | 307.040 | 307.809 | 311.556 |
| Point Lookup | 317.573 | 307.879 | 333.520 |

---

# Results

The benchmark framework records:

- Returned records
- Average latency
- P50 latency
- P95 latency

Results are stored as CSV files in the `results` directory.

---

# Project Structure

```
graph-db-benchmark/
├── data/
├── results/
├── src/
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

---

# Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Load Dataset

```bash
python src/load.py
```

---

# Run Benchmark

```bash
python src/run_benchmark.py
```

---

# Conclusion

This project provides a reusable benchmarking framework for graph databases using identical datasets and query workloads. The current implementation benchmarks Neo4j and CognoDB Cloud and can be extended to additional graph database platforms.

---

# Author

sharika Enagandula
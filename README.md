# Graph Database Cloud Benchmark

## Project Overview

This project benchmarks graph database performance using a common social network dataset and identical graph query workloads. The goal is to compare query latency, scalability, and benchmark reproducibility across different graph database platforms.

---

# Databases Benchmarked

- Neo4j Community Edition
- CognoDB Cloud
- ArangoDB Community Edition

The benchmark framework is designed so additional graph databases can be added using the same workloads.

---

# Dataset

**Dataset Name**

SNAP Soc-Pokec Social Network

**Source**

https://snap.stanford.edu/data/soc-pokec.html

**Relationships Loaded**

100,000

**Node Collection**

Person

**Relationship Type**

KNOWS

**Load Method**

Python Batch Loader

---

# Environment

| Component | Version |
|-----------|----------|
| Operating System | Windows 11 |
| Language | Python 3.x |
| Neo4j Driver | neo4j |
| ArangoDB Driver | python-arango |
| Database | Neo4j Community Edition |
| Cloud Database | CognoDB Cloud |
| Graph Database | ArangoDB Community Edition |

---

# Resource Configuration

## Neo4j

- Community Edition
- Local Machine

## CognoDB

- Free Tier (c0)

## ArangoDB

- Community Edition
- Local Machine

---

# Benchmark Queries

## 1-Hop Traversal

```cypher
MATCH (p:Person)-[:KNOWS]->(friend)
RETURN p.id, friend.id
LIMIT 100
```

## 2-Hop Traversal

```cypher
MATCH (p:Person)-[:KNOWS]->()-[:KNOWS]->(friend)
RETURN p.id, friend.id
LIMIT 100
```

## 3-Hop Traversal

```cypher
MATCH (p:Person)-[:KNOWS]->()-[:KNOWS]->()-[:KNOWS]->(friend)
RETURN p.id, friend.id
LIMIT 100
```

## Aggregation

```cypher
MATCH (p:Person)
RETURN count(p)
```

## Point Lookup

```cypher
MATCH (p:Person {id:$id})
RETURN p
```

---

# Benchmark Methodology

The benchmark uses the same methodology across all databases.

- Same dataset
- Same graph structure
- Same benchmark queries
- Warm-up runs before execution
- Multiple benchmark iterations
- Metrics collected:
  - Average Latency
  - P50 Latency
  - P95 Latency
  - Records Returned

---

# Neo4j Results

| Benchmark | Average (ms) | P50 (ms) | P95 (ms) |
|-----------|-------------:|---------:|---------:|
| 1-Hop Traversal | 351.160 | 307.362 | 336.374 |
| 2-Hop Traversal | 520.278 | 402.397 | 708.081 |
| 3-Hop Traversal | 440.266 | 433.784 | 581.876 |
| Aggregation | 386.957 | 373.232 | 514.436 |
| Point Lookup | 323.879 | 312.909 | 364.876 |

---

# CognoDB Results

| Benchmark | Average (ms) | P50 (ms) | P95 (ms) |
|-----------|-------------:|---------:|---------:|
| 1-Hop Traversal | 394.034 | 315.257 | 700.424 |
| 2-Hop Traversal | 399.513 | 311.197 | 613.892 |
| 3-Hop Traversal | 442.185 | 368.418 | 613.359 |
| Aggregation | 307.040 | 307.809 | 311.556 |
| Point Lookup | 317.573 | 307.879 | 333.520 |

---

# ArangoDB Results

> Results are available in:

```
results/arangodb_results.csv
```

---

# Project Structure

```
graph-db-benchmark/
│
├── data/
│   └── raw/
│
├── results/
│   ├── neo4j_results.csv
│   ├── cognodb_results.csv
│   └── arangodb_results.csv
│
├── src/
│   ├── benchmark.py
│   ├── benchmark_runner.py
│   ├── batch_loader.py
│   ├── arangodb_loader.py
│   ├── arangodb_runner.py
│   ├── load.py
│   ├── load_arango.py
│   ├── run_benchmark.py
│   ├── run_arango_benchmark.py
│   ├── result_writer.py
│   └── config.py
│
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd graph-db-benchmark
```

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Load Dataset

Neo4j

```bash
python src/load.py
```

ArangoDB

```bash
python src/load_arango.py
```

---

# Run Benchmarks

Neo4j

```bash
python src/run_benchmark.py
```

ArangoDB

```bash
python src/run_arango_benchmark.py
```

---

# Results

Benchmark results are automatically stored inside:

```
results/
```

Generated files

- neo4j_results.csv
- cognodb_results.csv
- arangodb_results.csv

---

# Conclusion

This project provides a reusable benchmarking framework for graph databases using identical datasets and benchmark workloads.

The current implementation benchmarks:

- Neo4j Community Edition
- CognoDB Cloud
- ArangoDB Community Edition

The framework can be extended to benchmark additional graph databases using the same methodology.

---

# Caveats

- Benchmarks were executed on free-tier resources where applicable.
- Network latency may affect cloud benchmark timings.
- Warm-up iterations were executed before collecting benchmark metrics.
- Results are specific to the tested environment and dataset.

---

# License

This project was developed for educational and assessment purposes.

---

# Author

**Sharika Enagandula**
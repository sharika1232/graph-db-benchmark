# Graph Database Cloud Benchmark

## Project Overview

This project benchmarks graph database performance using a common social network dataset and identical graph query workloads. The goal is to compare query latency, scalability, and benchmark reproducibility across multiple graph database platforms.

The benchmark framework is reusable and allows new graph databases to be integrated using the same dataset, benchmark methodology, and query workloads.

---

# Databases Benchmarked

- Neo4j Community Edition
- CognoDB Cloud
- ArangoDB Community Edition
- Memgraph Community Edition
- Kùzu Graph Database

---

# Dataset

**Dataset Name**

SNAP Soc-Pokec Social Network

**Source**

https://snap.stanford.edu/data/soc-pokec.html

**Relationships Loaded**

100,000

**Node Label**

Person

**Relationship Type**

KNOWS

**Load Method**

Python Batch Loader

---

# Environment

| Component | Version |
|------------|--------------------------|
| Operating System | Windows 11 |
| Language | Python 3.x |
| Neo4j Driver | neo4j |
| ArangoDB Driver | python-arango |
| Memgraph Driver | neo4j (Bolt Protocol) |
| Kùzu Driver | kuzu |
| Local Databases | Neo4j, ArangoDB, Memgraph, Kùzu |
| Cloud Database | CognoDB Cloud |

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

## Memgraph

- Community Edition
- Docker Container
- Bolt Protocol (Port 7688)

## Kùzu

- Embedded Graph Database
- Local Machine
- Python API

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

The benchmark uses the same methodology across all graph databases.

- Same dataset
- Same graph structure
- Same benchmark queries
- Warm-up runs before benchmarking
- Multiple benchmark iterations
- Metrics collected:
  - Records Returned
  - Average Latency
  - P50 Latency
  - P95 Latency

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

Benchmark results are available in:

```text
results/arangodb_results.csv
```

---

# Memgraph Results

| Benchmark | Average (ms) | P50 (ms) | P95 (ms) |
|-----------|-------------:|---------:|---------:|
| 1-Hop Traversal | 6.001 | 5.702 | 7.231 |
| 2-Hop Traversal | 7.384 | 7.622 | 8.711 |
| 3-Hop Traversal | 8.261 | 7.991 | 9.435 |
| Aggregation | 17.604 | 16.992 | 20.560 |
| Point Lookup | 21.342 | 20.004 | 25.164 |

---

# Kùzu Results

Benchmark results are available in:

```text
results/kuzu_results.csv
```

---

# Performance Comparison

| Database | 1-Hop | 2-Hop | 3-Hop | Aggregation | Point Lookup |
|----------|-------:|-------:|-------:|------------:|-------------:|
| Neo4j | 351.160 | 520.278 | 440.266 | 386.957 | 323.879 |
| CognoDB | 394.034 | 399.513 | 442.185 | 307.040 | 317.573 |
| ArangoDB | See CSV | See CSV | See CSV | See CSV | See CSV |
| Memgraph | 6.001 | 7.384 | 8.261 | 17.604 | 21.342 |
| Kùzu | See CSV | See CSV | See CSV | See CSV | See CSV |

---

# Project Structure

```text
graph-db-benchmark/
│
├── data/
│   └── raw/
│       ├── facebook_combined.txt
│       └── soc-pokec-relationships.txt
│
├── results/
│   ├── neo4j_results.csv
│   ├── cognodb_results.csv
│   ├── arangodb_results.csv
│   ├── memgraph_results.csv
│   └── kuzu_results.csv
│
├── src/
│   ├── benchmark.py
│   ├── benchmark_runner.py
│   ├── batch_loader.py
│   ├── config.py
│   ├── result_writer.py
│   │
│   ├── neo4j_loader.py
│   ├── arangodb_loader.py
│   ├── memgraph_loader.py
│   ├── kuzu_loader.py
│   │
│   ├── arangodb_runner.py
│   ├── memgraph_runner.py
│   ├── kuzu_runner.py
│   │
│   ├── load.py
│   ├── load_arango.py
│   ├── load_memgraph.py
│   ├── load_kuzu.py
│   │
│   ├── run_benchmark.py
│   ├── run_arango_benchmark.py
│   ├── run_memgraph_benchmark.py
│   ├── run_kuzu_benchmark.py
│   │
│   └── ...
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

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Load Dataset

## Neo4j

```bash
python src/load.py
```

## ArangoDB

```bash
python src/load_arango.py
```

## Memgraph

```bash
python src/load_memgraph.py
```

## Kùzu

```bash
python src/load_kuzu.py
```

---

# Run Benchmarks

## Neo4j

```bash
python src/run_benchmark.py
```

## ArangoDB

```bash
python src/run_arango_benchmark.py
```

## Memgraph

```bash
python src/run_memgraph_benchmark.py
```

## Kùzu

```bash
python src/run_kuzu_benchmark.py
```

---

# Results

Benchmark results are automatically generated and stored in the **results** directory.

Generated files:

- neo4j_results.csv
- cognodb_results.csv
- arangodb_results.csv
- memgraph_results.csv
- kuzu_results.csv

---

# Conclusion

This project provides a reusable benchmarking framework for graph databases using identical datasets and benchmark workloads.

The current implementation benchmarks the following graph database platforms:

- Neo4j Community Edition
- CognoDB Cloud
- ArangoDB Community Edition
- Memgraph Community Edition
- Kùzu Graph Database

The benchmark framework follows a common methodology for all supported databases, enabling fair comparison of graph query performance across multiple platforms. The modular architecture also makes it straightforward to extend the framework with additional graph databases in the future.

---

# Caveats

- Benchmarks were executed on local hardware and free-tier cloud resources where applicable.
- Network latency may affect cloud database benchmark timings.
- Warm-up iterations were executed before collecting benchmark metrics.
- Results are specific to the tested environment, dataset, and hardware configuration.
- Different graph databases use different storage engines and query optimizers, so absolute performance values may vary depending on workload characteristics.

---

# Future Work

Possible future improvements include:

- Support for additional graph databases such as Apache AGE, JanusGraph, or TigerGraph.
- Larger benchmark datasets.
- Automated benchmark visualization.
- Docker Compose setup for all supported databases.
- CI/CD integration for automated benchmark execution.

---

# License

This project was developed for educational and assessment purposes.

---

# Author

**Sharika Enagandula**
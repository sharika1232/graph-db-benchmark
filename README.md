# Graph Database Benchmark

## Project Overview

This project benchmarks the performance of graph databases using a real-world social network dataset. The benchmark measures common graph operations such as graph traversal, point lookup, and aggregation to compare database performance.

## Graph Databases

- Neo4j
- CognoDB Cloud

> Additional graph databases can be added using the same benchmark framework.

---

## Dataset

Dataset: SNAP Social Network Dataset (Pokec)

Source:
https://snap.stanford.edu/data/soc-pokec.html

Dataset Used:
- soc-pokec-relationships.txt

Relationships Loaded:
- 100,000

---

## Benchmark Queries

The following workloads were executed:

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

## Benchmark Metrics

The benchmark records:

- Average Latency (ms)
- P50 Latency
- P95 Latency
- Returned Records

---

## Project Structure

```
graph-db-benchmark/
│
├── data/
├── results/
├── src/
├── README.md
├── requirements.txt
└── .env.example
```

---

## Installation

Create a virtual environment.

```
python -m venv .venv
```

Activate it.

Windows

```
.venv\Scripts\activate
```

Install dependencies.

```
pip install -r requirements.txt
```

---

## Load Dataset

```
python src/load.py
```

---

## Run Benchmark

```
python src/run_benchmark.py
```

---

## Output

Benchmark results are stored in the `results` folder as CSV files.

Example columns:

- Benchmark
- Records
- Average(ms)
- P50(ms)
- P95(ms)

---

## Technologies

- Python
- Neo4j
- CognoDB Cloud
- Cypher Query Language

---

## Author

sharika Enagandula
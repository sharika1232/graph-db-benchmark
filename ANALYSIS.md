# Benchmark Analysis

## Objective

The objective of this project is to compare graph database performance using the same dataset, identical Cypher queries, and the same benchmark framework.

---

## Dataset

- Dataset: SNAP Soc-Pokec Social Network
- Relationships Loaded: 100,000
- Load Method: Python Batch Loader

---

## Benchmark Workloads

The following workloads were executed:

- 1-Hop Traversal
- 2-Hop Traversal
- 3-Hop Traversal
- Aggregation
- Point Lookup

Each workload was executed after warm-up runs.

The benchmark collected:

- Average latency
- P50 latency
- P95 latency

---

## Observations

### Neo4j

- Successfully loaded the dataset.
- Completed all benchmark workloads.
- Produced stable benchmark results.

### CognoDB Cloud

- Successfully connected using the official Neo4j Bolt driver.
- Successfully loaded the same dataset.
- Completed all benchmark workloads.
- Produced benchmark results comparable to Neo4j.

---

## Methodology

To ensure fairness:

- Same dataset
- Same Cypher queries
- Same benchmark framework
- Warm-up before measurements
- Same benchmark iterations

---

## Limitations

- Cloud network latency can affect benchmark results.
- Free-tier resource limitations may influence performance.
- Only the tested platforms are included in this submission.

---

## Conclusion

This benchmark framework demonstrates a reproducible approach for comparing graph databases. The implementation benchmarks Neo4j and CognoDB Cloud using identical workloads and can be extended to additional graph database platforms.
# Graph Database Comparison

## Benchmark Summary

| Benchmark | Neo4j | CognoDB |
|-----------|-------|----------|
| Dataset Loaded | ✅ | ✅ |
| 1-Hop Traversal | ✅ | ✅ |
| 2-Hop Traversal | ✅ | ✅ |
| 3-Hop Traversal | ✅ | ✅ |
| Aggregation | ✅ | ✅ |
| Point Lookup | ✅ | ✅ |

---

## Performance Comparison

| Benchmark | Neo4j Average (ms) | CognoDB Average (ms) |
|-----------|-------------------:|---------------------:|
| 1-Hop Traversal | 351.160 | 394.034 |
| 2-Hop Traversal | 520.278 | 399.513 |
| 3-Hop Traversal | 440.266 | 442.185 |
| Aggregation | 386.957 | 307.040 |
| Point Lookup | 323.879 | 317.573 |

---

## Benchmark Method

- Same dataset
- Same Cypher queries
- Same benchmark framework
- Warm-up before benchmarking
- 100 iterations
- Average, P50 and P95 latency recorded

---

## Notes

- Both databases successfully completed all benchmark workloads.
- CognoDB Cloud measurements include network latency because it is a managed cloud service.
- Neo4j was benchmarked using the same benchmark framework and logical queries.

---

## Future Work

The benchmark framework is designed to support additional graph databases by implementing the same loading process and benchmark workloads.
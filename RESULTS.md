# Benchmark Results

## Neo4j

| Benchmark | Records | Average (ms) | P50 (ms) | P95 (ms) |
|-----------|--------:|-------------:|----------:|----------:|
| 1-Hop Traversal | 100 | 351.160 | 307.362 | 336.374 |
| 2-Hop Traversal | 100 | 520.278 | 402.397 | 708.081 |
| 3-Hop Traversal | 100 | 440.266 | 433.784 | 581.876 |
| Aggregation | 1 | 386.957 | 373.232 | 514.436 |
| Point Lookup | 1 | 323.879 | 312.909 | 364.876 |

---

## CognoDB

| Benchmark | Records | Average (ms) | P50 (ms) | P95 (ms) |
|-----------|--------:|-------------:|----------:|----------:|
| 1-Hop Traversal | 100 | 394.034 | 315.257 | 700.424 |
| 2-Hop Traversal | 100 | 399.513 | 311.197 | 613.892 |
| 3-Hop Traversal | 100 | 442.185 | 368.418 | 613.359 |
| Aggregation | 1 | 307.040 | 307.809 | 311.556 |
| Point Lookup | 1 | 317.573 | 307.879 | 333.520 |

---

## Observations

- Both databases successfully loaded the dataset.
- All benchmark queries completed successfully.
- Warm-up runs were executed before measuring latency.
- Average, P50, and P95 latencies were collected for each workload.
- Network latency and free-tier limitations may influence cloud benchmark timings.

---

## Dataset

- Source: SNAP Soc-Pokec
- Relationships Loaded: 100,000

---

## Benchmark Queries

- 1-Hop Traversal
- 2-Hop Traversal
- 3-Hop Traversal
- Aggregation
- Point Lookup
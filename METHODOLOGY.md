# Benchmark Methodology

## Dataset

- SNAP Soc-Pokec Social Network
- Relationships Loaded: 100,000

## Benchmark Process

1. Connect to the database.
2. Load the dataset.
3. Warm up the database.
4. Execute benchmark queries.
5. Repeat each workload 100 times.
6. Record:
   - Average latency
   - P50 latency
   - P95 latency
7. Save results to CSV files.

## Queries

- 1-Hop Traversal
- 2-Hop Traversal
- 3-Hop Traversal
- Aggregation
- Point Lookup

## Fairness

- Same dataset
- Same benchmark framework
- Same logical queries
- Warm-up before measurements
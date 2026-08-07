from kuzu_runner import KuzuBenchmark
from benchmark_runner import BenchmarkRunner
from result_writer import ResultWriter

# ---------------------------------
# Initialize Benchmark
# ---------------------------------

benchmark = KuzuBenchmark()
runner = BenchmarkRunner(benchmark)

# ---------------------------------
# 1-Hop Traversal
# ---------------------------------

runner.execute(
    "1-Hop Traversal",
    """
    MATCH (p:Person)-[:KNOWS]->(friend)
    RETURN p.id, friend.id
    LIMIT 100
    """
)

# ---------------------------------
# 2-Hop Traversal
# ---------------------------------

runner.execute(
    "2-Hop Traversal",
    """
    MATCH (p:Person)-[:KNOWS]->()-[:KNOWS]->(friend)
    RETURN p.id, friend.id
    LIMIT 100
    """
)

# ---------------------------------
# 3-Hop Traversal
# ---------------------------------

runner.execute(
    "3-Hop Traversal",
    """
    MATCH (p:Person)-[:KNOWS]->()-[:KNOWS]->()-[:KNOWS]->(friend)
    RETURN p.id, friend.id
    LIMIT 100
    """
)

# ---------------------------------
# Aggregation
# ---------------------------------

runner.execute(
    "Aggregation",
    """
    MATCH (p:Person)
    RETURN count(p)
    """
)

# ---------------------------------
# Point Lookup
# ---------------------------------

record = benchmark.conn.execute("""
MATCH (p:Person)
RETURN p.id
LIMIT 1
""").get_next()

runner.execute(
    "Point Lookup",
    f"""
    MATCH (p:Person {{id:'{record[0]}'}})
    RETURN p
    """
)

# ---------------------------------
# Close Benchmark
# ---------------------------------

benchmark.close()

# ---------------------------------
# Save Results
# ---------------------------------

writer = ResultWriter("results/kuzu_results.csv")

for row in runner.get_results():
    writer.write(
        row["Benchmark"],
        row["Records"],
        row["Average(ms)"],
        row["P50(ms)"],
        row["P95(ms)"]
    )

print("\n✅ Kuzu benchmark completed successfully!")
print("Results saved to results/kuzu_results.csv")
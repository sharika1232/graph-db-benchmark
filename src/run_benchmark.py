from benchmark import Neo4jBenchmark
from benchmark_runner import BenchmarkRunner
from result_writer import ResultWriter

# ---------------------------------
# Initialize Benchmark
# ---------------------------------

benchmark = Neo4jBenchmark()
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

with benchmark.driver.session() as session:
    record = session.run("""
        MATCH (p:Person)
        RETURN p.id AS id
        LIMIT 1
    """).single()

runner.execute(
    "Point Lookup",
    """
    MATCH (p:Person {id:$id})
    RETURN p
    """,
    {"id": record["id"]}
)

# ---------------------------------
# Close Benchmark
# ---------------------------------

benchmark.close()

# ---------------------------------
# Save Results
# ---------------------------------

writer = ResultWriter("results/neo4j_results.csv")

for row in runner.get_results():
    writer.write(
        row["Benchmark"],
        row["Records"],
        row["Average(ms)"],
        row["P50(ms)"],
        row["P95(ms)"]
    )

print("\n✅ Benchmark completed successfully!")
print("Results saved to results/neo4j_results.csv")
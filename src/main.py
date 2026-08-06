from batch_loader import BatchLoader
from benchmark import Neo4jBenchmark
from runner import BenchmarkRunner
from result_writer import ResultWriter

# -----------------------------
# Load Dataset
# -----------------------------
# loader = BatchLoader()

# loader.clear_database()

# loader.load_dataset(
#     "data/raw/soc-pokec-relationships.txt",
#     batch_size=1000,
#     max_relationships=100000
# )

# loader.close()

# -----------------------------
# Benchmark
# -----------------------------
benchmark = Neo4jBenchmark()
runner = BenchmarkRunner(benchmark)

# 1-Hop
runner.execute(
    "1-Hop Traversal",
    """
    MATCH (p:Person)-[:KNOWS]->(friend)
    RETURN p, friend
    """
)

# 2-Hop
runner.execute(
    "2-Hop Traversal",
    """
    MATCH (p:Person)-[:KNOWS]->()-[:KNOWS]->(friend)
    RETURN p, friend
    """
)

# 3-Hop
runner.execute(
    "3-Hop Traversal",
    """
    MATCH (p:Person)-[:KNOWS]->()-[:KNOWS]->()-[:KNOWS]->(friend)
    RETURN p, friend
    """
)

# Aggregation
runner.execute(
    "Aggregation",
    """
    MATCH (p:Person)
    RETURN count(p)
    """
)

# Indexed Point Lookup
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

benchmark.close()

# -----------------------------
# Save Results
# -----------------------------
writer = ResultWriter()

for row in runner.get_results():
    writer.write(
        row["Benchmark"],
        row["Records"],
        row["Average(ms)"]
    )

print("\n✅ Benchmark completed successfully!")
print("Results saved to results/neo4j_results.csv")
from memgraph_loader import MemgraphLoader

loader = MemgraphLoader()

print("Clearing Memgraph database...")
loader.clear_database()

print("Loading dataset...")

loader.load_dataset(
    "data/raw/soc-pokec-relationships.txt",
    max_relationships=100000
)

loader.close()

print("✅ Memgraph dataset loaded successfully!")
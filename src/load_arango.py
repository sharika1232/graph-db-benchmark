from arangodb_loader import ArangoLoader

loader = ArangoLoader()

print("Clearing database...")
loader.clear_database()

print("Loading dataset...")

loader.load_dataset(
    "data/raw/soc-pokec-relationships.txt",
    max_relationships=100000
)

print("Done.")
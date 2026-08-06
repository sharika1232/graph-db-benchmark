from batch_loader import BatchLoader

loader = BatchLoader()

print("Clearing database...")
loader.clear_database()

print("Loading dataset...")

loader.load_dataset(
    "data/raw/soc-pokec-relationships.txt",
    batch_size=1000,
    max_relationships=100000
)

loader.close()

print("\n✅ Dataset loaded successfully!")
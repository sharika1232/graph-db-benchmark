import kuzu
import time


class KuzuLoader:

    def __init__(self):
        self.db = kuzu.Database("kuzu_benchmark")
        self.conn = kuzu.Connection(self.db)

        self.conn.execute("""
        CREATE NODE TABLE IF NOT EXISTS Person(
            id STRING,
            PRIMARY KEY(id)
        )
        """)

        self.conn.execute("""
        CREATE REL TABLE IF NOT EXISTS KNOWS(
            FROM Person TO Person
        )
        """)

    def clear_database(self):
        self.conn.execute("MATCH (n) DETACH DELETE n")

    def load_dataset(self, file_path, max_relationships=100000):

        start = time.perf_counter()
        total = 0

        with open(file_path, "r") as file:

            for line in file:

                if line.startswith("#"):
                    continue

                source, target = line.strip().split()

                self.conn.execute(f"""
                MERGE (a:Person {{id:'{source}'}})
                MERGE (b:Person {{id:'{target}'}})
                MERGE (a)-[:KNOWS]->(b)
                """)

                total += 1

                if total % 1000 == 0:
                    print(f"Loaded {total} relationships...")

                if total >= max_relationships:
                    break

        end = time.perf_counter()

        print("\n====================")
        print("Kuzu Dataset Loaded")
        print(f"Relationships : {total}")
        print(f"Time : {end-start:.2f} sec")
        print("====================")
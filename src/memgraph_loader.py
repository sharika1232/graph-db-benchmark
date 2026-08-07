from neo4j import GraphDatabase
from config import (
    MEMGRAPH_URI,
    MEMGRAPH_USER,
    MEMGRAPH_PASSWORD
)
import time


class MemgraphLoader:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            MEMGRAPH_URI,
            auth=(MEMGRAPH_USER, MEMGRAPH_PASSWORD)
        )

    def close(self):
        self.driver.close()

    def clear_database(self):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")

    def load_dataset(
        self,
        file_path,
        batch_size=1000,
        max_relationships=100000
    ):

        start = time.perf_counter()

        batch = []
        total = 0

        with self.driver.session() as session:

            with open(file_path, "r", encoding="utf-8") as file:

                for line in file:

                    if line.startswith("#"):
                        continue

                    source, target = line.strip().split()

                    batch.append({
                        "source": source,
                        "target": target
                    })

                    if len(batch) >= batch_size:

                        session.run("""
                        UNWIND $rows AS row

                        MERGE (a:Person {id: row.source})
                        MERGE (b:Person {id: row.target})

                        MERGE (a)-[:KNOWS]->(b)
                        """, rows=batch)

                        total += len(batch)
                        print(f"Loaded {total} relationships...")

                        batch = []

                        if total >= max_relationships:
                            break

                if batch and total < max_relationships:

                    session.run("""
                    UNWIND $rows AS row

                    MERGE (a:Person {id: row.source})
                    MERGE (b:Person {id: row.target})

                    MERGE (a)-[:KNOWS]->(b)
                    """, rows=batch)

                    total += len(batch)

        end = time.perf_counter()

        print("\n==============================")
        print("Memgraph Dataset Loaded")
        print(f"Relationships : {total}")
        print(f"Time : {end-start:.2f} seconds")
        print("==============================")
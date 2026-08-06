import time
from neo4j import GraphDatabase
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD


class DatasetLoader:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            NEO4J_URI,
            auth=(NEO4J_USER, NEO4J_PASSWORD)
        )

    def close(self):
        self.driver.close()

    def clear_database(self):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")

    def load_dataset(self, file_path):

        start = time.perf_counter()

        with self.driver.session() as session:

            with open(file_path, "r") as file:

                for line in file:

                    if line.startswith("#"):
                        continue

                    source, target = line.strip().split()

                    session.run("""
                    MERGE (a:Person {id:$source})
                    MERGE (b:Person {id:$target})
                    MERGE (a)-[:KNOWS]->(b)
                    """,
                    source=source,
                    target=target)

        end = time.perf_counter()

        print(f"\nDataset Loaded Successfully")
        print(f"Time : {end-start:.2f} seconds")
import time
from neo4j import GraphDatabase
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD


class Neo4jBenchmark:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            NEO4J_URI,
            auth=(NEO4J_USER, NEO4J_PASSWORD)
        )

    def close(self):
        self.driver.close()

    def run_query(self, query, parameters=None):

        parameters = parameters or {}

        with self.driver.session() as session:

            start = time.perf_counter()

            result = session.run(query, parameters)

            records = list(result)

            end = time.perf_counter()

        elapsed = end - start

        return len(records), elapsed
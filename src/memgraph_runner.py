import time
from neo4j import GraphDatabase
from config import (
    MEMGRAPH_URI,
    MEMGRAPH_USER,
    MEMGRAPH_PASSWORD
)


class MemgraphBenchmark:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            MEMGRAPH_URI,
            auth=(MEMGRAPH_USER, MEMGRAPH_PASSWORD)
        )

    def close(self):
        self.driver.close()

    def run_query(self, query, params=None):

        start = time.perf_counter()

        with self.driver.session() as session:
            result = session.run(query, params or {})
            records = list(result)

        end = time.perf_counter()

        return len(records), end - start
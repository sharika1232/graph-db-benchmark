import time
from arango import ArangoClient
from config import (
    ARANGO_HOST,
    ARANGO_USERNAME,
    ARANGO_PASSWORD,
    ARANGO_DATABASE
)


class ArangoBenchmark:

    def __init__(self):
        client = ArangoClient(hosts=ARANGO_HOST)

        self.db = client.db(
            ARANGO_DATABASE,
            username=ARANGO_USERNAME,
            password=ARANGO_PASSWORD
        )

    def run_query(self, query, bind_vars=None):

        start = time.perf_counter()

        cursor = self.db.aql.execute(query, bind_vars=bind_vars or {})

        records = list(cursor)

        end = time.perf_counter()

        return len(records), end - start
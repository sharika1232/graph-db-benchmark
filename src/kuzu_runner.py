import time
import kuzu


class KuzuBenchmark:

    def __init__(self):
        self.db = kuzu.Database("kuzu_benchmark")
        self.conn = kuzu.Connection(self.db)

    def close(self):
        pass

    def run_query(self, query, params=None):

        start = time.perf_counter()

        result = self.conn.execute(query)

        records = []

        while result.has_next():
            records.append(result.get_next())

        end = time.perf_counter()

        return len(records), end - start
import statistics


class BenchmarkRunner:

    def __init__(self, benchmark):
        self.benchmark = benchmark
        self.results = []

    def execute(self, name, query, params=None, iterations=10):

        times = []
        records = 0

        # Warm-up (5 runs)
        for _ in range(5):
            self.benchmark.run_query(query, params)

        # Actual benchmark
        for _ in range(iterations):
            record_count, elapsed = self.benchmark.run_query(query, params)
            records = record_count
            times.append(elapsed * 1000)  # milliseconds

        times.sort()

        average = statistics.mean(times)
        p50 = statistics.median(times)
        p95 = times[int(iterations * 0.95) - 1]

        self.results.append({
            "Benchmark": name,
            "Records": records,
            "Average(ms)": round(average, 3),
            "P50(ms)": round(p50, 3),
            "P95(ms)": round(p95, 3)
        })

    def get_results(self):
        return self.results
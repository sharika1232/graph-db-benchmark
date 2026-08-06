import csv
import os


class ResultWriter:

    def __init__(self, filename="results/neo4j_results.csv"):
        os.makedirs("results", exist_ok=True)
        self.file = filename

    def write(self, benchmark_name, records, average, p50, p95):

        file_exists = os.path.exists(self.file)

        with open(self.file, "a", newline="") as csvfile:

            writer = csv.writer(csvfile)

            if not file_exists:
                writer.writerow([
                    "Benchmark",
                    "Records",
                    "Average(ms)",
                    "P50(ms)",
                    "P95(ms)"
                ])

            writer.writerow([
                benchmark_name,
                records,
                average,
                p50,
                p95
            ])
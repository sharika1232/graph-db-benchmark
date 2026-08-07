import csv
import os


class ResultWriter:

    def __init__(self, filename):
        self.filename = filename

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        if not os.path.exists(filename):
            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "Benchmark",
                    "Records",
                    "Average(ms)",
                    "P50(ms)",
                    "P95(ms)"
                ])

    def write(self, benchmark, records, average, p50, p95):
        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                benchmark,
                records,
                average,
                p50,
                p95
            ])
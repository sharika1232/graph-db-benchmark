from arangodb_runner import ArangoBenchmark
from benchmark_runner import BenchmarkRunner
import pandas as pd

benchmark = ArangoBenchmark()
runner = BenchmarkRunner(benchmark)

runner.execute(
    "Count Persons",
    "FOR p IN persons RETURN p"
)

runner.execute(
    "Count Relationships",
    "FOR k IN knows RETURN k"
)

results = pd.DataFrame(runner.get_results())

results.to_csv(
    "results/arangodb_results.csv",
    index=False
)

print(results)
print("\nResults saved to results/arangodb_results.csv")
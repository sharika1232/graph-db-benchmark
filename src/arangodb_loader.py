import time
from arango import ArangoClient
from config import (
    ARANGO_HOST,
    ARANGO_USERNAME,
    ARANGO_PASSWORD,
    ARANGO_DATABASE
)


class ArangoLoader:

    def __init__(self):
        client = ArangoClient(hosts=ARANGO_HOST)

        self.db = client.db(
            ARANGO_DATABASE,
            username=ARANGO_USERNAME,
            password=ARANGO_PASSWORD
        )

        self.persons = self.db.collection("persons")
        self.knows = self.db.collection("knows")

    def clear_database(self):
        self.persons.truncate()
        self.knows.truncate()

    def load_dataset(self, file_path, max_relationships=100000):

        start = time.perf_counter()

        count = 0

        with open(file_path, "r", encoding="utf-8") as file:

            for line in file:

                if line.startswith("#"):
                    continue

                source, target = line.strip().split()

                if not self.persons.has(source):
                    self.persons.insert({"_key": source})

                if not self.persons.has(target):
                    self.persons.insert({"_key": target})

                self.knows.insert({
                    "_from": f"persons/{source}",
                    "_to": f"persons/{target}"
                })

                count += 1

                if count % 1000 == 0:
                    print(f"Loaded {count} relationships...")

                if count >= max_relationships:
                    break

        end = time.perf_counter()

        print("\n==============================")
        print("Dataset Loaded Successfully")
        print(f"Relationships : {count}")
        print(f"Time : {end-start:.2f} seconds")
        print("==============================")
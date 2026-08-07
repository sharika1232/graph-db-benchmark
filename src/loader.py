import time
from neo4j import GraphDatabase
from faker import Faker
import uuid
from batch_loader import BatchLoader

from config import (
    NEO4J_URI,
    NEO4J_USER,
    NEO4J_PASSWORD
)

fake = Faker()


class Neo4jLoader:

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

    def insert_people(self, total=100):

        start = time.perf_counter()

        with self.driver.session() as session:

            for _ in range(total):

                session.run(
                    """
                    CREATE (p:Person{
                        id:$id,
                        name:$name,
                        age:$age,
                        city:$city,
                        email:$email
                    })
                    """,
                    id=str(uuid.uuid4()),
                    name=fake.name(),
                    age=fake.random_int(min=18,max=65),
                    city=fake.city(),
                    email=fake.email()
                )

        end = time.perf_counter()

        print(f"\nInserted {total} nodes")
        print(f"Time : {end-start:.3f} seconds")
    

    def create_relationships(self):

      with self.driver.session() as session:
          session.run("""
          MATCH (a:Person)
          WITH a ORDER BY rand()
          LIMIT 100
          WITH collect(a) AS persons
          UNWIND range(0, size(persons)-2) AS i
          WITH persons[i] AS a, persons[i+1] AS b
          CREATE (a)-[:KNOWS]->(b)
          """)

      print("Relationships Created")


from arangodb_loader import ArangoLoader

loader = ArangoLoader()

print("Clearing database...")
loader.clear_database()

print("Loading dataset...")

loader.load_dataset(
    "data/raw/soc-pokec-relationships.txt",
    max_relationships=100000
)

print("Done.")
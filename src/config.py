import os
from dotenv import load_dotenv

load_dotenv()

# Neo4j / CognoDB
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Redis
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# PostgreSQL
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))
POSTGRES_DB = os.getenv("POSTGRES_DB", "benchmark")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")

# ArangoDB
ARANGO_HOST = "http://127.0.0.1:8529"
ARANGO_USERNAME = "root"
ARANGO_PASSWORD = "Graph@1234"
ARANGO_DATABASE = "_system"

# Memgraph

MEMGRAPH_URI = os.getenv("MEMGRAPH_URI", "bolt://localhost:7688")
MEMGRAPH_USER = os.getenv("MEMGRAPH_USER", "")
MEMGRAPH_PASSWORD = os.getenv("MEMGRAPH_PASSWORD", "")

# Kuzu

KUZU_DATABASE = "kuzu_benchmark"
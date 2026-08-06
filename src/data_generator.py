from faker import Faker
import random

fake = Faker()


def generate_person():
    return {
        "id": fake.uuid4(),
        "name": fake.name(),
        "age": random.randint(18, 70),
        "city": fake.city(),
        "email": fake.email(),
    }


def generate_people(count=1000):
    return [generate_person() for _ in range(count)]
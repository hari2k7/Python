import json
import os

DATA_FILE = "data.json"

def load_students():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)

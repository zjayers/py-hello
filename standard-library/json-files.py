import json
from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Kindergarten Cop", "year": 1993}
]

# Format as JSON
data = json.dumps(movies)

# Write JSON file
Path('movies.json').write_text(data)

# Read JSON file
data2 = Path('movies.json').read_text()
movieDict = json.loads(data2)
print(movieDict)
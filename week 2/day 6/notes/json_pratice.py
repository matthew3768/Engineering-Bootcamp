import json


person = {
    "name": "Matthew",
    "age": 22,
    "city": "Bournemouth"
}

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

with open('person.json', 'r') as file:
    person = json.load(file)

print(person)
print(person['name'])


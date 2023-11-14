author = {
    "first_name": "Jan",
    "last_name": "Kowalski"
}

for item in author:
    print(item, author[item])

for item in author.items():
    print(item)

for item in author.items():
    print(item[0],item[1])

for first_name, last_name in author.items():
    print(first_name, last_name)

author.items()
author.keys()
author.values()
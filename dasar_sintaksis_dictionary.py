users = {
    "id": 5,
    "name": "Chelsey Dietrich",
    "username": "Kamren",
    "email": "Lucio_Hettinger@annie.ca",
    "adress": {
        "street": "Skiles Walks",
        "suite": "Suite 351",
        "city": "Roscoeview",
        "zipcode": "33263",
        "geo": {
            "lat": "-31.8129",
            "lng": "62.5342"
    }
}
    # "q" : "value"
    # q ga boleh angka, harus teks/string
}

print(users)
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print(users["adress"]["street"])
print(users["adress"]["geo"])
print(users["adress"]["geo"]["lat"])

# hal diatas adalah apa yang disebut dengan dictionary

print(users)
print(type(users))
print('\nUbah dictionary ke JSON')
import json
result = json.dumps(users)
print(type(result))
print(result)

# Karena telah diubah menjadi string json yang valid, bisa diubah ke yang lebih dibutuhkan
# kalo dumbs pake string, dumbs(tring)

# Kalo sebaliknya jadi seperti ini

with open('result.json', 'w') as file:
    json.dump(users, file)

# itulah bedanya json.dump dan json.dumps

import sys
print(sys.prefix)
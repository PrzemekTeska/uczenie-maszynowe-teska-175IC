import json
import requests

# Stworzenie w pamięci obiektu typu json
data = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
        "name": "Romaguera-Crona",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets"
    }
}

# Zapisanie do pliku .json i metoda dumps()
with open("json/data_file.json", "w") as write_file:
    json.dump(data, write_file)

# Zapisanie pliku .json do stringa
json_string = json.dumps(data)
print(json_string)

# Wybranie rozmiaru wcięcia
json_string_indentation = json.dumps(data, indent=4)
print(json_string_indentation)

# Enkodowanie i dekodowanie JSONa
weight = ("Weight", 75)
encoded_weight = json.dumps(weight)
decoded_weight = json.loads(encoded_weight)

print(weight == encoded_weight)
print(type(weight))
print(type(decoded_weight))
print(weight == tuple(decoded_weight))

with open("json/data_file.json", "r") as read_file:
    data = json.load(read_file)
print(data)

# Deserializacja stringa
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)
print(data)

# JSON request z API
response = requests.get("https://jsonplaceholder.typicode.com/users")
users = json.loads(response.text)

print(response.json() == users)
print(type(users))
print(users[:5])

# Użytkownik najniżej od równika Ziemii
latitudes = []
for user in users:
    latitudes.append(float(user["address"]["geo"]["lat"]))

latitudes.sort()
print(f'Największa odległość od równika wynosi {latitudes[0]}')


# Enkodowanie złożonych obiektów przy pomocy niestandardowej funkcji
def encode_complex(z):
    if isinstance(z, complex):
        return z.real, z.imag
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")


print(json.dumps(9 + 5j, default=encode_complex))


# Enkodowanie złożonych obiektów przez nadpisanie domyślnej (default()) metody JSONEncodera
class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)


print(json.dumps(2 + 5j, cls=ComplexEncoder))
encode = ComplexEncoder()
print(encode.encode(3 + 6j))

# Dekodowanie obiektów
complex_json = json.dumps(4 + 17J, cls=ComplexEncoder)
print(json.loads(complex_json))

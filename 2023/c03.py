import requests

url = "https://codember.dev/data/encryption_policies.txt"

data = requests.get(url).text

invalid = []
data = data.split("\n")
for d in data:
    min, aux = d.split("-")
    max, letter, text = aux.split(" ")
    letter = letter[:-1]

    number = text.count(letter)
    if number < int(min) or number > int(max):
        invalid.append(text)

print(invalid[41])





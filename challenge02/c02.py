import requests

url = "https://codember.dev/data/message_02.txt"

data = requests.get(url)

cont = 0
response = ""
for d in data.text:
    if d == "#":
        cont += 1
    elif d == "@":
        cont -= 1
    elif d == "*":
        cont *= cont
    elif d == "&":
        response = f"{response}{cont}"
    else:
        print("Error")

print(response)
# prints: 
# 024899455
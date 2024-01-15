import requests

url = "https://codember.dev/data/message_01.txt"

data = requests.get(url)

animales = data.text.replace("\n", "").split(" ")
dict_animales = {}

for a in animales:
    try:
        dict_animales[a] +=1
    except Exception as e:
        print(e)
        dict_animales[a] = 1

str_response = ""
for key in dict_animales:
    str_response = f"{str_response}{key}{dict_animales[key]}"

print(str_response)
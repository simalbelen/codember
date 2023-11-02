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

print(dict_animales)

str_response = ""
for key in dict_animales:
    str_response = f"{str_response}{key}{dict_animales[key]}"

print(str_response)
# prints: murcielago15leon15jirafa15cebra6elefante15rinoceronte15hipopotamo15ardilla15mapache15zorro15lobo15oso15puma2jaguar14tigre10leopardo10gato12perro12caballo14vaca14toro14cerdo14oveja14cabra14gallina10pato10ganso10pavo10paloma10halcon11aguila11buho11colibri9canario8loro8tucan8pinguino7flamenco7
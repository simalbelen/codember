import requests

def calc_checksum(string):
    checksum = ''
    for i in range(0, len(string)):
        char = string[i]
        if string.count(char) == 1:
            checksum = checksum + char
    return checksum

url = "https://codember.dev/data/files_quarantine.txt"

data = requests.get(url).text

real = []
data = data.split("\n")
for d in data:
    name, checksum = d.split("-")
    if checksum == calc_checksum(name):
        real.append([d, name, checksum])

print(real[32][2])





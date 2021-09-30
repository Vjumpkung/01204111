def read_data():
    with open(input('Enter file name: ')) as citi:
        data = citi.readlines()[1::]
        data = [data[i].strip().split(",") for i in range(len(data))]
        data = list(zip(*data))
    return data
cities = read_data()
from statistics import mean
temperature_country = {}
for i in range(len(cities[1])):
    if not cities[1][i] in temperature_country:
        temperature_country.setdefault(cities[1][i],[float(cities[4][i])])
    else:
        temperature_country[cities[1][i]].append(float(cities[4][i]))
for j in (temperature_country):
    print(f"{j} {mean(temperature_country[j]):.2f}")
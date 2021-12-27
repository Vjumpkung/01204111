class City:
  Country = {}
  nbCity = 0
  nbCountry = 0
  def __init__(self, city, country, latitude, longitude, temperature):
    self.city = city
    self.country = country
    self.latitude = float(latitude)
    self.longitude = float(longitude)
    self.temperature = float(temperature)
    if country not in City.Country.keys():
      City.Country[country] = []
      City.nbCountry += 1
    City.Country[country].append((city, float(temperature)))
    City.nbCity += 1
    
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
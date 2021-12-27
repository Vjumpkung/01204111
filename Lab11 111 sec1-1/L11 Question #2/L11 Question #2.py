class City:
  nbCity = 0
  def __init__(self, city, country, latitude, longitude, temperature):
    self.city = city
    self.country = country
    self.latitude = float(latitude)
    self.longitude = float(longitude)
    self.temperature = float(temperature)
    City.nbCity += 1
from statistics import mean
with open(input("Enter file name: ")) as f:
    data = f.readlines()
    data = [i.strip().split(",") for i in data]
    head = data[0]
    val = data[1:]
    citites = [dict(zip(head,i)) for i in val]
print(f"Minimum: {min(citites,key=lambda x : float(x['temperature']))['temperature']}")
print(f"Maximum: {max(citites,key=lambda x : float(x['temperature']))['temperature']}")
print(f"Average temperature: {mean([float(i['temperature']) for i in citites]):.4f}")
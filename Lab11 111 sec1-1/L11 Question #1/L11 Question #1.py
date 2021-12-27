class Country:
  nbCountry = 0
  def __init__(self, country, population, EU,coastline):
    self.country = country
    self.population = float(population)
    self.EU = EU
    self.coastline = coastline
    Country.nbCountry += 1
def read_data():
    with open(input("Enter File name: ")) as citi:
        data = citi.readlines()[1::]
        data = [data[i].strip().split(",") for i in range(len(data))]
        data = list(zip(*data))
    return data
data = read_data()
for ind,val in enumerate(data[0]):
    if data[2][ind] == "no" and data[3][ind] == "yes":
        print(f"{val} {data[1][ind]}")
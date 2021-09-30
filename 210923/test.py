class City:
  nbCity = 0
  def __init__(s,city,country,lat,long,temp):
    s.city = city; s.country = country; s.lat = lat
    s.long = long; s.temp = temp; City.nbCity += 1
class Country:
  nbCountry = 0
  def __init__(self,coun,pop,isEU,coastline):
    self.coun,self.pop,self.isEU,self.coastline = coun,pop,isEU,coastline
    Country.nbCountry += 1

def readCity():
  myCity = []
  with open('Cities.csv') as fp:
    c = fp.readline()
    for c in fp:
      cc = c.strip().split(',')
      city,country,lat,long,temp = cc[0],cc[1],float(cc[2]),float(cc[3]),float(cc[4])
      myCity.append(City(city,country,lat,long,temp))
  return myCity

def test_readCity(myCity):
  for c in myCity:
    print(c.city,c.country,c.lat,c.long,c.temp)

def readCountry():
  myCountry = []
  with open('Countries.csv') as fp:
    c = fp.readline()
    for c in fp:
      cc = c.strip().split(',')
      coun,pop,isEU,coastline = cc[0],float(cc[1]),cc[2],cc[3]
      myCountry.append(Country(coun,pop,isEU,coastline))
  return myCountry

def q01(myCity, myCountry):
    each_country = {}
    for i in myCountry:
        if i.isEU == "yes" and i.coastline == "no":
            each_country.setdefault(i.coun,[])
        else:
            continue
    for j in myCity:
        if j.country in each_country.keys():
            each_country[j.country].append(j.temp)
    for i in each_country:
        try:
            print(f"{i}: {sum(each_country[i])/len(each_country[i]):.2f}")
        except ZeroDivisionError: 
            pass

def q02(myCity, myCountry):
    each_country = {}
    for i in myCountry:
        if i.isEU == "no":
            each_country.setdefault(i.coun,[])
        else:
            continue
    for j in myCity:
        if j.country in each_country.keys():
            each_country[j.country].append(j.temp)
    maxx = -1e8
    minn = 1e8
    current_max = ''
    current_min = ''
    for i in each_country:
      try:
        mean = sum(each_country[i])/len(each_country[i])
        if mean > maxx:
          maxx = mean
          current_max = i
        if mean < minn:
          minn = mean
          current_min = i
      except ZeroDivisionError:
        continue
    print(f"The highest average city temperature: {current_max} ({maxx:.2f})")
    print(f"The lowest average city temperature: {current_min} ({minn:.2f})")

### main begins here
myCity = readCity()
myCountry = readCountry()
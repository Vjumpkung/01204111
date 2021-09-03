import requests
from bs4 import BeautifulSoup
allpip = []
fp = open("requirement.txt","w")
for j  in range(1,501):
    r = requests.get(f"https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3&page={j}")
    print("scrap page",j)
    soup = BeautifulSoup(r.content, "html.parser") 
    data = soup.find_all("span", {"class":"package-snippet__name"})
    for i in range(len(data)):
        allpip.append(data[i].text)
fp.write("\n".join(allpip))
fp.close()

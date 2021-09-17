# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import json
x = json.load(open(input("Filename : ")))


# %%
def one(data):
    print(len(data))


# %%
def two(data):
    fr = int(input("From : "))
    tu = int(input("To : "))
    stw = input("Start with Char : ")
    k = fr
    for items in data[fr:tu+1]:
        try:
            if items['title'][0].lower() == stw.lower():
                print(f"{k} : {items['title']}")
        except:
            pass
        k+=1
            


# %%
def three(data):
    fr = int(input("From : "))
    tu = int(input("To : "))
    ty = input('Type : ')
    tvlst = [i for i in data[fr:tu+1] if i['type'] == ty]
    print(f"TV : {len(tvlst)}")
    maximum = -1e18
    fav = -1e18
    name = ""
    name2 = ""
    for i in tvlst:
        try:
            if i['mal_score'] > maximum:
                maximum = i['mal_score']
                name = i['title']
            elif i['mal_score'] == maximum:
                name = name
        except:
            continue
    for i in tvlst:
        try:
            if i['mal_favorites'] > fav:
                fav = i['mal_favorites']
                name2 = i['title']
            elif i['mal_favorites'] == fav:
                name2 = name2
        except:
            continue
    print("Most scores :",name)
    print("Most favorites :",name2)


# %%
def fourr(x):
    fr = int(input("From : "))
    tu = int(input("To : "))
    src = input('Source : ')
    stat = input('Status : ')
    msc = float(input('Mul score : '))
    k = fr
    for p in x[fr:tu+1]:
        try:
            if p['mal_score'] >= msc and p['source'] == src and p['status'] == stat:
                print(f"{k} : {p['title']}")
        except:
            pass
        k += 1


# %%
def fivef(x):
    fr = int(input("From : "))
    tu = int(input("To : "))
    sea = input("Season : ")
    c = 0
    for i in x[fr:tu+1]:
        try:
            if sea in i['premiered']:
                c+=1
        except:
            continue
    print(f"{sea} : {c}")


# %%
def siz(data):
    fr = int(input("From : "))
    tu = int(input("To : "))
    c = 0
    for i in data[fr:tu+1]:
        try:
            if i['aired_start'][0:4] == i['aired_end'][0:4]:
                c += 1
        except:
            continue 
    print(f"Find : {c}")


# %%
def sev(data):
    tits = input('Title : ')
    for i in data:
        try:
            if i['title'].lower() == tits.lower():
                print(f"{i['mal_rating']}")
                break
        except:
            continue


# %%
def egg(data):
    fr = int(input("From : "))
    tu = int(input("To : "))
    k = fr
    maxima = len(max(data[fr:tu+1],key = lambda x : len(x['synopsis'].split()))['synopsis'].split())
    for i in data[fr:tu+1]:
        try:
            if len(i['synopsis'].split()) == maxima:
                print(f"{k} : {i['title']}")
        except:
            pass
        k += 1


# %%
nam = int(input('Menu : '))
if nam == 1: one(x)
elif nam == 2: two(x)
elif nam == 3: three(x)
elif nam == 4: fourr(x)
elif nam == 5: fivef(x)
elif nam == 6: siz(x)
elif nam == 7: sev(x)
elif nam == 8: egg(x)



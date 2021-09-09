# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import json,statistics
fn = input("file name: ")
with open(fn) as fp:
    data = fp.readlines()
    lst = [json.loads(data[i]) for i in range(9000)]
nen = int(input("input: "))


# %%
def kor1():
    print(len(lst))


# %%
def kor3():
    productidls = set()
    for i in lst:
        if i["productID"] not in productidls:
            productidls.add(i["productID"])
    print(len(productidls))


# %%
def kor2():
    reviewerIDidls = set()
    for i in lst:
        if i["reviewerID"] not in reviewerIDidls:
            reviewerIDidls.add(i["reviewerID"])
    print(len(reviewerIDidls))


# %%
def category_ls(pos):
    sinkarluck = {}
    for i in lst:
        if (i["category"].split(">"))[pos] not in sinkarluck:
            sinkarluck.setdefault((i["category"].split(">"))[pos],1)
        else:
            sinkarluck[(i["category"].split(">"))[pos]] += 1
    print(len(sinkarluck))


# %%
def most_review():
    review_count = {}
    for i in lst:
        if i["reviewerID"] not in review_count:
            review_count.setdefault(i["reviewerID"],1)
        else:
            review_count[i["reviewerID"]] += 1
    print(max(review_count.items(),key=lambda x : x[1])[0])


# %%
def ชื่อสินค้าที่ได้คะแนนเฉลี่ยสูงที่สุด():
    reviewPro = {}
    for i in lst:
        if i['productName'] not in reviewPro:
            reviewPro.setdefault(i['productName'],[i['overall']])
        else:
            reviewPro[i['productName']].append(i['overall'])
    review_lst = []
    mamimum = statistics.mean(max(reviewPro.items(),key=lambda x : statistics.mean(x[1]))[1])
    for k,l in list(reviewPro.items()):
        if statistics.mean(l) == mamimum:
            review_lst.append((k,len(l)))
    print(max(review_lst,key= lambda x : x[1])[0])


# %%
def ชื่อสินค้าที่มีจำนวนคำเฉลี่ยต่อรีวิวมากที่สุด():
    product_cum_review = {}
    for i in lst:
        if i['productName'] not in product_cum_review:
            product_cum_review.setdefault(i['productName'],[len(i["reviewText"].split())])
        else:
            product_cum_review[i['productName']].append(len(i["reviewText"].split()))
    k = [(i,statistics.mean(j)) for i,j in list(product_cum_review.items())]
    print(max(k,key=lambda x : x[1])[0])
        


# %%
if nen == 1: kor1()
elif nen == 2: kor2()
elif nen == 3: kor3()
elif nen == 4: category_ls(0)
elif nen == 5: category_ls(1)
elif nen == 6: most_review()
elif nen == 7: ชื่อสินค้าที่ได้คะแนนเฉลี่ยสูงที่สุด()
elif nen == 8: ชื่อสินค้าที่มีจำนวนคำเฉลี่ยต่อรีวิวมากที่สุด()



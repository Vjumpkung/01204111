def hash(one,two):
    if ord(one) >= ord(two):
        return ord(two) + 10
    else:
        return ord(one) - 7

def isPhotobook(s):
    global isPhoto
    isPhoto = s[0].isalpha() and s[-1].isalpha()
    return isPhoto

def calKey(s):
    return sum([hash(s[i],s[i+1]) for i in range(len(s) - 1)])

def isPhotobookGenuine(uid):
    if not isPhoto:
        return 'Incorrect Type'
    return uid%2 == 0

def isAlbumGenuine(uid):
    if isPhoto:
        return 'Incorrect Type'
    return uid%2 == 1

def solve():
    n = int(input())
    ids = [input() for i in range(n)]
    real_photo_book = 0
    fake_album = 0  
    for id in ids:
        isPhotobook(id)
        UID = calKey(id)
        if isPhoto:
            if isPhotobookGenuine(UID):
                real_photo_book+=1
        else:
            if isAlbumGenuine(UID):
                fake_album+=1
    print(real_photo_book)
    print(fake_album)
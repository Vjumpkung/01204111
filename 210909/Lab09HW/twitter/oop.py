import json
import time
class Twitter:
    def __init__(self):
        self.data = ["test"]
    def __repr__(self):
        print(self.data)
    def get_data(self):
        self.data = json.load(open(input("File name: ")))
    def which_one(self):
        num = int(input("input: "))
        return num
    def content_length(self):
        content_len = len(self.data)
        return content_len
    def all_users(self):
        users = []
        data = self.data
        for i in data:
            if i["author"] not in users:
                users.append(i["author"])
            else:
                continue
        return len(users)
    def most_tweet(self):
        data = self.data
        tweet_count = {}
        for i in data:
            if i["author"] not in tweet_count:
                tweet_count.setdefault(i["author"],1)
            else:
                tweet_count[i["author"]] += 1
        k = sorted(tweet_count.items(),reverse=True,key=lambda x : x[1])
        lst = []
        for j in k:
            if j[1] == k[0][1]:
                lst.append(j[0])
        return lst
    def total_topic(self):
        data = self.data
        topic_dick = set()
        for i in data:
            if i["topic"] not in topic_dick:
                topic_dick.add(i["topic"])
            else:
                pass
        return len(topic_dick)
    def priority(self,txt):
        data = self.data
        txt_ls = 0
        for i in data:
            if i["topic_priority"] == txt:
                txt_ls += 1
        return txt_ls
    def non_English(self):
        data = self.data
        def isEnglish(s):
            try:
                s.encode(encoding='utf-8').decode('ascii')
            except UnicodeDecodeError:
                return False
            else:
                return True
        for i in data:
            if isEnglish(i["text"]):
                continue
            else:
                return False
        return True
    def most_words(self):
        return len(max(self.data,key=lambda x : len(x['text'].split()))["text"].split())
    def print_which_one(self):
        for num in range(1,9):
            if num == 1:
                print(self.content_length())
            elif num == 2:
                print(self.all_users())
            elif num == 3:
                print(("\n").join(self.most_tweet()))
            elif num == 4:
                print(self.total_topic())
            elif num == 5:
                print(self.priority("ALERT"))
            elif num == 6:
                print(self.priority("UNIMPORTANT"))
            elif num == 7:
                print(self.non_English())
            elif num == 8:
                print(self.most_words())
t = Twitter()
t.get_data()
t1 = time.time()
t.print_which_one()
t2 = time.time()
print(t2-t1)
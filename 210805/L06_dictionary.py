dictk = {"arm":["n", "แขน"], "hello": ["v","สวัสดี"], "beautiful":["adj","สวย"], "toilet" :["n", "ห้องน้ำ"], "kick":["v", "เตะ"], "handsome":["adj", "หล่อ"]}
for _ in iter(int,1):
    words_inputt = input()
    if words_inputt == "0":
        break
    if not words_inputt in dictk:
        print("Word not in dictionary.")
    else:
        for _ in iter(int,1):
            numpos = input()
            try: 
                try:
                    numpos = int(numpos)
                    if numpos > 0:
                        check_indexx = dictk[words_inputt][numpos-1]
                        print(dictk[words_inputt][numpos-1])
                        break
                    else:
                        print("Invalid option.")
                except IndexError:
                    print("Invalid option.")
            except TypeError: 
                print("Invalid option.")
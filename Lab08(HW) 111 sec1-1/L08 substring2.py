txt = input("Text: ")
substr = input("Substring: ")
possible = [list(txt[i:i+len(substr)]) for i in range(len(txt)) if len(list(txt[i:i+len(substr)])) == len(substr)]
possi = ["".join(i) for i in possible]
add_q = ["".join([i[j] if substr[j] == i[j] else "?" for j in range(len(substr))]) for i in possible]
for i in add_q:
    if substr in add_q:
        txt = txt.replace(substr,"["+substr+"]")
        break
    else:
        for i in list(zip(add_q,possi)):
            if i[0].count("?") <= 1:
                txt = txt.replace(i[1],"["+i[0]+"]",1)
                continue
print(txt)
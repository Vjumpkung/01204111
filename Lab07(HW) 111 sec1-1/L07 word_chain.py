#word_chain
Text = input("Text: ").split()
#Text = "HEAD HEAP LEAP TEAR REAR BAER BAET BEEP JEEP JOIP JEIP AEIO".split()
chain_list = []
def find_diff(this,ahead):
    diff_count = 0
    this = list(this)
    ahead = list(ahead)
    #print(this)
    for i in range(len(this)):
        #print(i + " in " + ahead)
        if this[i] != ahead[i]:
            diff_count += 1
        else:
            continue
    return diff_count
count_chain = 1
for i in range(len(Text)):
    try:
        #print(Text[i],end=" ")
        if 0 < find_diff(Text[i],Text[i+1]) <= 2:
            count_chain += 1
        else:
            #print()
            chain_list.append(count_chain)
            count_chain = 1
    except IndexError:
        chain_list.append(count_chain)
        break
#print("\n")
print(f"{len(chain_list)} Chain(s). Maximum length is {max(chain_list)} word(s).")
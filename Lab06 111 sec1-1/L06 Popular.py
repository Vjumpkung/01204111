num_words = int(input("Input number of words: "))
word_list = [input() for i in range(num_words)]
count_first_letter = {}
for i in word_list:
    if not i[0] in count_first_letter:
        count_first_letter[i[0]] = 1
    else:
        count_first_letter[i[0]] += 1
print("The popular character is "+ max(count_first_letter , key=count_first_letter.get) + ".")
print(f"The character is used in {max(count_first_letter.values())} words.")
for i in word_list:
    if i[0] == max(count_first_letter , key=count_first_letter.get):
        print(i)
    else:
        pass
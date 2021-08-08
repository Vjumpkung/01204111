#substring
Text = input("Text: ")
subString = input("Substring: ")
Text = Text.replace(subString,"["+subString+"]")
if not "[" in Text:
    print("Not found")
else:
    print(Text)
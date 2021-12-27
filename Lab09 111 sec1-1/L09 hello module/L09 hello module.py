code = '''
def greeting(name):
  print("Hello, " + name)'''

with open('mymodule.py', 'w') as f:
  f.write(code)

##-----------------------------------------

import mymodule
inp = input("Name : ")
mymodule.greeting(inp)
class py_solution:
    def __init__(self,inp):
        self.paren = inp
    def is_valid_parentheses(self):
        brackets = ['()', '{}', '[]']
        while any(x in self.paren for x in brackets):
            for br in brackets:
                self.paren = self.paren.replace(br, '')
        return not self.paren
put = input('input: ')    
p = py_solution(put)
if p.is_valid_parentheses():
    print('valid parentheses')
else:
    print('invalid parentheses')
class py_solution:
    left = ["(","[","{"]
    right = [")","]","}"]
    match_pattern = ["()","[]","{}"]
    def __init__(self,inp):
        self.paren = inp
    def is_valid_parentheses(self):
        valid = False
        left_bracket_log = []
        temp = ""
        for i in self.paren:
            if i in self.left:
                left_bracket_log.append(i)
                continue
            if i in self.right:
                if len(left_bracket_log) != 0:
                    temp = left_bracket_log[-1] + i
                else:
                    temp = i
                    valid = False
                if temp in self.match_pattern:
                    valid = True
                    left_bracket_log.pop(-1)
                else:
                    valid = False
                    break
        if len(left_bracket_log) != 0:
            valid = False
        return valid
put = input('input: ')    
p = py_solution(put)
if p.is_valid_parentheses():
    print('valid parentheses')
else:
    print('invalid parentheses')
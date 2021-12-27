from math import gcd
class gcdlcm:
    def __init__ (self,a:int = 0,b:int = 0):
        self.a = a
        self.b = b
        self.this_gcd = 1
        self.this_lcm = 1
    def update_a_b(self,a,b):
        self.a = a
        self.b = b
        self.this_gcd = gcd(self.a,self.b)
        self.this_lcm = self.a*self.b//self.this_gcd
    def get_data(self):
        a_input = int(input("a : "))
        b_input = int(input("b : "))
        self.update_a_b(a_input,b_input)
    def show_data(self):
        print(f"GCD : {self.this_gcd}")
        print(f"LCM : {self.this_lcm}")
x = gcdlcm()
x.get_data()
x.show_data()
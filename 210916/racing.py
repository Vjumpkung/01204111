import json 
x = json.load(open(input("Enter json filename : ")))
class Racer:
    def __init__(self,name,_range,velocity,response,goal ):
        self.name = name
        self._range = _range
        self.velocity = velocity
        self.response = response
        self.goal = goal
        self.now = 0
    def __str__(self):
        return f"{self.name} , {self._range} , {self.velocity} , {self.response} , {self.now}"
    def cal_time(self):
        ss = self.goal
        ra = self._range
        vi = self.velocity
        ti = 0.0001
        dn = 0
        while True:
            dn = dn + vi[0]*0.0001
            ti += 0.0001
            try:
                if (ra[1] < dn):
                    #print("pop")
                    vi.pop(0)
                    ra.pop(0)
            except IndexError:
                pass
            if dn >= ss:
                break
        self.ti = ti
        dick = {
            "name" : self.name,
            "time" : float(f"{self.ti:.2f}"),
            "response" : self.response
        }
        return dick
op = []
newls = []
dis=int(input('Enter distance (meter) : '))
for i in x['racer']:
    r = Racer(i['name'],i['_range'],i['velocity'],i['response'],dis)
    op.append(r)
for i in op:
    newls.append(i.cal_time())
newls.sort(key=lambda x : (x['time'],-x['response'],x['name']))
for i in newls:
    print(f"{i['name']} {i['time']:.2f}")
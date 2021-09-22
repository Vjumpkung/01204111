import numpy as np
games_data = []
X = np.random.RandomState(1) 
blood_start = int(input("Blood Start: "))
ur_speed = int(input("Your speed: "))
n_monsters = int(input("Number of monsters: "))
monsters = [int(input(f"Monster {i+1} speed: ")) for i in range(n_monsters)]
player_list = {"player" : {"speed" : ur_speed,"HP" : blood_start}}
monsters_list = {}
for i in range(len(monsters)):
    dick = {}
    dick.setdefault(f'speed',monsters[i])
    dick.setdefault(f'HP',blood_start//n_monsters)
    monsters_list.setdefault(f"Monster {i+1}",dick)
class gamer:
    def __init__(self,player,monsters):
        self.player = player
        self.monsters = monsters
        self.turn = 1
        self.COMBO = 0
    def __str__(self):
        return f"{self.player} {self.monsters}"
    def current_monsters(self): #for player attacking
        fastest = max(self.monsters.values(),key=lambda x: x['speed'])['speed']
        for k,v in self.monsters.items():
            if v['speed'] == fastest:
                s,h = tuple(v.values())
                return k,s,h
    def player_attack(self):
        name,speed,hp = self.current_monsters()
        self.PLAYERATK = 10 + self.COMBO
        hp -= self.PLAYERATK
        if hp > 0:
            print(f"{name} HP left {hp}")
            self.monsters[name].update({'speed':speed,'HP':hp})
        elif hp <= 0:
            print(f"{name} HP left 0")
            del self.monsters[name]
        self.COMBO += 2
    def update_HP(self):
        return [list(i.values())[1] for i in self.monsters.values()]
    def monsters_attack(self,n,name):
        try:
            Hu_Tao = self.monsters[name]["HP"]
        except KeyError:
            return False
        print(f"- Monster {n} Turn -")
        self.monsters_atk = X.randint(1, 40) 
        self.player['player']['HP'] -= self.monsters_atk
        return True
    def Field_Play(self):
        self.field = {**self.player,**self.monsters}
        return sorted(self.field.items(),reverse=True,key=lambda x : x[1]['speed'])
    def player_heal(self):
        self.player['player']['HP'] += 20*n_monsters
        print(f"Your HP left {self.player['player']['HP']}")
        self.COMBO = 0
    def playing(self):
        self.nen = 1
        while True:
            print(f'''=========================
Turn {self.nen}
-------------------------''')
            self.this_turn = self.Field_Play()
            for i,j in enumerate(self.this_turn):
                #print(self.this_turn)
                if j[0] == "player":
                    print(f"- Your Turn -")
                    self.a_or_h = input('Attack(a) or Heal(h): ')
                    if self.a_or_h == "a":
                        self.player_attack()
                    elif self.a_or_h == "h":
                        self.player_heal()
                if "Monster" in j[0] and j[1]['HP'] > 0:
                    if self.monsters_attack(int(j[0][-1]),j[0]) == False:
                        continue
                    if self.player['player']["HP"] > 0:
                        print(f"Your HP left {self.player['player']['HP']}")
                    elif self.player['player']["HP"] <= 0:
                        print(f"Your HP left 0")
                        break
                elif "Monster" in j[0] and j[1]['HP'] <= 0:
                    self.nen += 1
                    continue
            if len(self.update_HP()) == 0:
                print('You win.(^_^)')
                break
            if self.player['player']["HP"] <= 0:   
                print('You lose and die.(T_T)')     
                break
            self.nen += 1
g = gamer(player_list,monsters_list)
g.playing()
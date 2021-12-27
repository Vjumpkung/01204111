import numpy as np
X = np.random.RandomState(1) 
BS = int(input('Blood Start: '))
class Attack:
    def __init__(self,BS):
        self.MONSTERS = BS
        self.PLAYER = BS
        self.COMBO = 0
    def player_attack(self):
        self.PLAYERATK = 10 + self.COMBO
        self.MONSTERS -= self.PLAYERATK
        if self.MONSTERS > 0:
            print(f"Monster's HP left {self.MONSTERS}")
        self.COMBO += 2
    def player_heal(self):
        self.PLAYER += 20
        self.COMBO = 0
        if self.PLAYER > 0:
            print(f"Your HP left {self.PLAYER}")
    def monsters_attack(self):
        self.MONATK = X.randint(1, 40) 
        self.PLAYER -= self.MONATK
        if self.PLAYER > 0:
            print(f"Monster's turn : Your HP left {self.PLAYER}")
    def play(self):
        while True:
            get_player_atk = input('Attack(a) or Heal(h): ')
            if get_player_atk == 'a': 
                self.player_attack()
            elif get_player_atk == 'h': 
                self.player_heal()
            self.monsters_attack()
            if self.MONSTERS <= 0:
                print('Monster\'s HP left 0')
                print('You win.(^_^)')
                break
            elif self.PLAYER <= 0:
                print("Monster's turn : Your HP left 0")
                print('You lose and die.(T_T)')
                break
a = Attack(BS)
a.play()
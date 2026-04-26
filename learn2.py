class  UserProfile:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0

    def add_win(self):
        self.wins += 1
        print(self.name + " now has " + str(self.wins) + "wins!")

kuro = UserProfile("kuro")
kuro.add_win()
kuro.add_win()
class Mob():
    def __init__(self,name):
        self.name = name

    def move(self, direction):
        print(self.name + ' moved ' + direction)

class Villager():
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def move(self, direction):
        print(self.name + ' moved ' + direction)

    def get_colour(self):
        return self.color

class Creeper():
    def __init__(self, name):
        self.name = name
        self.weaponsList = ['TNT', 'fire']

    def weapons(self):
        wl = self.weaponsList
        weapons = ''
        for i in self.weaponsList:
            if wl.index(i) == len(self.weaponsList)-1:
                weapons += i
            else:
                weapons += i + ', '
        return weapons

mob = Mob('vilager')
print('name is: ' + mob.name)
mob.move('left')

villager = Villager('Bob', 'Red')
print(villager.get_colour())

creeper = Creeper('Creepy')
print('Creeper weapons: ', creeper.weapons())
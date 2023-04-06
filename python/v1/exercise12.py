# Add all the classes here




mob = Mob('vilager')
print('name is: ' + mob.name)
mob.move('left')

villager = Villager('Bob', 'Red')
print(villager.get_colour())

creeper = Creeper('Creepy')
print('Creeper weapons: ', creeper.weapons())
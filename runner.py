from basketball import Game
from basketball import Player
from basketball import Team


kobe = Player('Kobe','Bryant')
shaq = Player('Shaq', 'O\'niel')
fisher = Player('Derek', 'Fisher')
payton = Player('Gary', 'Payton')
malone = Player('Karl', 'Malone')
horry = Player('Robert', 'Horry')
scott = Player('Byron', 'Scott')

players = [kobe, shaq, fisher, payton, malone, horry, scott]

names = []
for player in players:
    full_name = player.first_name + ' ' + player.last_name
    names.append(full_name)

express_names = [player.last_name for player in players]

print express_names

print names

# la = Team('Lakers', 'Staple', 2000)
# la.starting_five(kobe)
# la.starting_five(shaq)
# la.starting_five(fisher)

# la.starting_five(kobe)
# la.starting_five(shaq)
# la.starting_five(fisher)
# la.starting_five(payton)
# la.starting_five(malone)

# la.starting_five(horry)
# la.starting_five(scott)

# # la.subs(on=horry, off=kobe)
# # la.subs(off=shaq, on=scott)
# # la.subs(scott)
# # la.subs(kobe)
# # la.subs(shaq)

# starting = la.starters()
# bench = la.reserves()

# print "\nThe starters"

# for starters in starting:
#     print starters.first_name, starters.last_name

# print "\nThe Reserves"

# for reservers in bench:
#     print reservers.first_name, reservers.last_name


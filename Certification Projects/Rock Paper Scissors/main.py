# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
#from RPS import find_abbey,find_quincy,find_mrugesh
from unittest import main



#play(player, quincy, 1000)

play(player, kris, 1000)
play(player, abbey, 1000)
play(player, mrugesh, 1000)
play(player, quincy, 1000)





# Milestone 1 beat Mrugesh

#play(player, mrugesh, 1000)


# Milestone 2 beat Abbey 
#play(player, abbey, 1000)

# Milestone 3 beat Quincy

#play(player,quincy,1000)


# Milestone 4 beat Kris

#play(random_player,mrugesh, 1000)

#play(abbey,random_player, 1000)


# Uncomment line below to play interactively against a bot:
# play(human, abbey, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)

#find_abbey(['', 'P', 'P', 'P', 'R', 'R', 'S', 'S', 'P', 'S', 'R', 'R', 'R', 'R', 'S'],['', 'R', 'R', 'S', 'S', 'P', 'P', 'R', 'P', 'S', 'S', 'S', 'S', 'P', 'P'])

#find_quincy(['', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S'])

#find_mrugesh(['', 'R', 'R', 'R', 'R', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'R', 'P', 'P'])

# Uncomment line below to run unit tests automatically
# main(module='test_module', exit=False)
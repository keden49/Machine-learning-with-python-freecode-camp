'''
Beat Them at their own Game
What matters to Abbey and Mrugesh is my own data 
What Matters to quincy is just following a specific pattern
Kris just counters my previous moves 
At the end of the day data is the most valuable commodity 
I can also make their data 
In my final function where I observe patterns 
and pick their own enemy 
'''


import random
moves = ["R","P","S"] # list of all my potential choices



'''
4 functions to counter each stratergy 
'''

# Milestone 1 beat mrugesh

# History keeps track of my own information 
# Embodying the mind of my opponent



def beat_mrugesh(opponent_history, history):
   
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    # get most frequent element  
    
    expected = max(set(history[-10:]),key = history[-10:].count)

    # Mrugesh Response 

    expected_response = ideal_response[expected]

    # counter mrugesh

    counter = ideal_response[expected_response] # counter mahrens move


    return counter 


# Milestone 2 beat Abbey 

# beat Abbey 

def beat_abbey(opponent_history,history,combinations):
    
    # last two plays 

    prev2= ''.join(history[-2:])

    
    # Keep the same tracker as Abby 

    if len(prev2) == 2:
        combinations[prev2] += 1

    # get last play which will be previous move for abbey

    last_play = history[-1] # prevents crashing

    # potential plays 

    expected_plays = [last_play + play for play in moves]

    #  counts of expected plays 

    expected_counts = {k:combinations[k] for k in expected_plays if k in combinations}

    # get the abbey's prediction

    expected_prediction = max(expected_counts, key = expected_counts.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    expected_response = ideal_response[expected_prediction]
    
    counter = ideal_response[expected_response]


    return counter 
    


# Milestone 3 Beat Quincy 


# Beat Quincy 

tracker = [-1]
def beat_Quincy(opponent_history,history,pattern = ["R", "R", "P", "P", "S"]):
    
    
    # keeps track of rounds and makes moves methodically avoiding offsets 
    counter_index = len(opponent_history)
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    counter_moves = [ideal_response[counter] for counter in pattern]
    return counter_moves[counter_index % len(counter_moves)] # follow quincys pattern but in counter move




# Milestone 4 Beat Kris 





def beat_Kris(opponent_history,history):
   
    
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    last_play = history[-1]
    expected_response = ideal_response[last_play]

    # counter Kris 

    counter = ideal_response[expected_response]
    
    
    # 
    return counter




'''
4 functions to figures out players pattern
studies opponents history for patterns 
uses my own play moves to counter player
'''



def find_abbey(opponent_history,history):
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    # recreate expected responses 
    expected_response = [ideal_response[expected] for expected in history if expected != '']

    if opponent_history[:2] == ['', 'P']:

        # differentiate kris from abbey 
        if opponent_history[2:] == expected_response[:-1]:
            
            return False
        else:
            return True
        
    else:
        return


        

def find_quincy(opponent_history):

    left_half = opponent_history[5:10]
    right_half = opponent_history[10:15]

    if left_half == right_half:

        return True
    
    # end function once the top condition is not met

    else:
        return
    

    
def find_mrugesh(opponent_history):

    if opponent_history[:3] == ['', 'R', 'R']:
        return True 
    
    else:
        return 
    

'''Composed fn that finds best stratergy to beat opponent''' 


def match_strategy(opponent_history,history):

    if find_mrugesh(opponent_history):

        match = "mrugesh"
           
    elif find_abbey(opponent_history,history):
        
        match = "abbey"
       
    
    elif find_quincy(opponent_history):
        
        match = "quincy"

    else:

        match = "kris"

    
    return match
    
    
'''
Defining fully composed function that handles all possible logics 
The first 10 rounds will be random to allow the opponents history 
to build up to sth meaningful

parameters

prev_play = opponents last play
opponent_history = list that stores opponents move 
history =  list that keeps track of my own moves 
strategy = list that stores opponents algorithm
combinations = dictionary that keeps track of abbeys stratergy either for the first 15 or the whole game
'''

combinations = {"RR": 1,"RP": 0,"RS": 0,"PR": 0,"PP": 0,"PS": 0,"SR": 0,"SP": 0,"SS": 0}

def player(prev_play, opponent_history=[],history = [""],stratergy = []):
    
    # use global dictionary 
    global combinations

    # opponents moves 
    opponent_history.append(prev_play)
    
    # clear memory to avoid overlap
    # reset memory for round 1 of the next bot

    if len(history) == 1001:
            
            history.clear()
            opponent_history.clear()
            stratergy.clear()
            opponent_history.append(prev_play)
            history.append(prev_play)
            combinations.clear()
            combinations.update({"RR": 1, "RP": 0, "RS": 0, "PR": 0, "PP": 0, "PS": 0, "SR": 0, "SP": 0, "SS": 0})
           
    
    
   # uses first 15 rounds to figure out stratergy 
    if len(opponent_history) == 15:

        # find match

        stratergy.append(match_strategy(opponent_history,history))

        

        

    if stratergy:

        algorithm = stratergy[0] # access algorithm

        if algorithm == "quincy":

            counter = beat_Quincy(opponent_history,history)
        
        elif algorithm == "kris":

            counter = beat_Kris(opponent_history,history)

        elif algorithm == "mrugesh":

            counter = beat_mrugesh(opponent_history,history)

        else:

            counter = beat_abbey(opponent_history,history,combinations)
        
        history.append(counter)
        return counter
        
      
    # gather enough data from the first 15 rounds 
    # play random moves 
    else:
        
        guess = random.choice(moves)

       
        # keep count along with abbey

        if len(history[-2:]) == 2:
            if "" not in history[-2:]:
                combinations["".join(history[-2:])] +=  1

        history.append(guess)
        return guess
    




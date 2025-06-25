# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from collections import defaultdict
import random 


def n-gram(n, opponent_history, actions):
        dictionary_Of_Events = defaultdict(lambda: defaultdict(int))
        Current_pattern = tuple(opponent_history[-n:])

        for i in range(len(opponent_history)-n):
            pattern = tuple(opponent_history[i:i+n])
            players_next_play = opponent_history[i+n]
            dictionary_Of_Events[pattern][players_next_play] += 1

        for i in actions:
            if dictionary_Of_Events[Current_pattern].get(i) == None:
                dictionary_Of_Events[Current_pattern][i] = 0

        if Current_pattern in dictionary_Of_Events:
            guess = max(dictionary_Of_Events[Current_pattern], key = dictionary_Of_Events[Current_pattern].get())
            Max_value = max(dictionary_Of_Events[Current_pattern].values())
            sorted_dict = sorted(dictionary_Of_Events[Current_pattern].values(), reverse = True)
            second_highest_value = sorted_dict[1]
            total_sum = sum(dictionary_Of_Events[Current_pattern].values())
            confidence_level = (Max_value - second_highest_value)/total_sum
            weight = n/20 + total_sum/50
            weighted_confidence_level = confidence_level * weight 
        else:
            guess = None
            weighted_confidence_level = 0
        return guess,  weighted_confidence_level
 
def player(prev_play, opponent_history=[]):
    actions = ['R', 'P', 'S']
    
    if len(opponent_history) > 2:
        Num_Of_games_played = len(opponent_history)
        n = Num_Of_games_played
        predicted_optimal_guesses = {'R':0, 'P':0, 'S':0}
        
        for i in range(1,min(n,20)):
            guess,weighted_confidence_level = n-gram(i, opponent_history, actions)
            if guess != None:
                predicted_optimal_guesses[guess] +=  weighted_confidence_level
        
        if predicted_optimal_guesses['R'] == predicted_optimal_guesses['S'] == predicted_optimal_guesses['P'] :
            counter_play = random.choice(actions)
            
        else:
            
            Optimal_guess =  max(predicted_optimal_guesses, key = predicted_optimal_guesses.get())
            potential_draw_guess = max(sorted(predicted_optimal_guesses.keys(), reverse = True), key = predicted_optimal_guesses.get())
            
            Overall_Optimal_guess = random.choice([Optimal_guess,potential_draw_guess])
            optimal_guess_index = actions.index(Overall_Optimal_guess)
            if optimal_guess_index == 2:
                counter_play = actions[0]
            else:
                counter_play = actions[optimal_guess_index + 1]
            

    else:
        counter_play = random.choice(actions)
        

    opponent_history.append(prev_play)
    return counter_play
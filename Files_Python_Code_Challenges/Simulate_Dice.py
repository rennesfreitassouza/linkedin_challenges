from os import urandom
import secrets

# https://www.linkedin.com/learning/python-code-challenges/simulate-dice
def roll_dices(dices):
    current_trial_outcome = []
    for dice in dices:
        dice_side_list = [side for side in range(1, dice + 1)]
        dice_side = secrets.choice(dice_side_list)
        current_trial_outcome.append(dice_side)
    return sum(current_trial_outcome)
            

def many_simulations(args, my_histogram_dict, simulation_times = 1_000_000):
    for i in range(simulation_times):
        roll_result = roll_dices(args)
        my_histogram_dict[roll_result] = my_histogram_dict[roll_result] + 1

def dice_game(*args):
    if len(args):
        max_sum = 0
        for dice_sides in args:
            max_sum += dice_sides

        my_histogram_dict = dict([(i, 0) for i in range(len(args), (max_sum + 1))])
        
        simulation_times = 1_000_000
        many_simulations(args, my_histogram_dict, simulation_times)
    
    outcome_str = 'OUTCOME PROBABILITY\n'
    k_list = ['OUTCOME']
    [k_list.append(str(k)) for k in my_histogram_dict.keys()]
    biggest = max(len(key) for key in k_list)

    for k, v in my_histogram_dict.items():
        key_str = str(k).ljust(biggest + 1, " ")
        outcome_str += f'{key_str}{(v * 100) / simulation_times:0.2f}%\n' 
    return outcome_str

def main():
    print(dice_game(4, 6, 6))

if __name__ == '__main__': main()

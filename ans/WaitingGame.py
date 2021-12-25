import random
import time

# https://www.linkedin.com/learning/python-code-challenges/play-the-waiting-game
def waiting_game_aux(start_counter, end_counter):
    rounded_start_counter = round(start_counter, 3)
    rounded_end_counter = round(end_counter, 3)
    
    elapsed_time = rounded_end_counter - rounded_start_counter
    
    rounded_elapsed_time = round(elapsed_time, 2)

    return int(rounded_elapsed_time)

def waiting_game():
    random_interger = random.randint(1, 4)
    print(f"\tYour target time is {random_interger} seconds.")
    user_input = None
    while(user_input != ''):

        user_input = input("\t---Press Enter to Begin---")
        start_counter = time.perf_counter()
        input(f"\t...Press Enter again after\n\t{random_interger} seconds...\n")
        end_counter = time.perf_counter()

        elapsed_time = waiting_game_aux(start_counter, end_counter)

        print(f"\tElapsed time: {elapsed_time} seconds.\n")
    
    if elapsed_time == random_interger:
        print(f"\tGoal achieved.")
    else:
        print(f"\tGoal not achieved.")
    
def main():
    waiting_game()

if '__name__' == '__main__': main()

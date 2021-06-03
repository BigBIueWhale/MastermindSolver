import itertools
import random
def mastermind_solve(colors, slots, repeat):
    stop = False
    counter1_cpy = 0
    counter2_cpy = 0
    possible_combinations = []
    first_try = []
    counter3 = 0
    while counter3 < slots:
        rand = random.randint(0, colors - 1)
        if (not(rand in first_try)):
            first_try.append(rand)
            counter3+=1
    if repeat:
        possible_combinations = (list(itertools.product(list(range(0, colors)), repeat=slots)))
    else:
        possible_combinations = (list(itertools.combinations(list(range(0, colors)), slots)))
    possible_combinations.reverse()
    possible_combinations.append(tuple(first_try))
    possible_combinations.reverse()
    past_tries = []
    while (stop == False):
        for current_combinations in range(0, len(possible_combinations)):
            is_current_combination_possible = True
            for current_try_from_past_tries in range(0, len(past_tries)):
                how_many_hits = 0
                how_many_misses = 0
                used_misses = []
                for counter1 in range(0, slots):
                    if possible_combinations[current_combinations][counter1] == past_tries[current_try_from_past_tries][0][counter1]:
                        how_many_hits+=1
                        used_misses.append(counter1)
                    else:
                        for counter2 in range(0, slots):
                            if possible_combinations[current_combinations][counter1] == past_tries[current_try_from_past_tries][0][counter2]:
                                if (not (counter2 in used_misses)):
                                    how_many_misses+=1
                                    used_misses.append(counter2)
                                    break
                if ((past_tries[current_try_from_past_tries][1] != how_many_hits) or (past_tries[current_try_from_past_tries][2] != how_many_misses)):
                    is_current_combination_possible = False
                    
                    break
            if is_current_combination_possible:
                print ('**', current_combinations)
                print("\nwhen entering: ", possible_combinations[current_combinations])
                num_of_hits = int(input("   how many hits are there? "))
                num_of_misses = int(input("   how many misses are there? "))
                if num_of_hits == slots:
                    print("\nwell, your answer is ", possible_combinations[current_combinations], '\n')
                    stop = True
                    break
                past_tries.append([possible_combinations[current_combinations], num_of_hits, num_of_misses])
                break
slots = int(input("\nenter the amount of slots: "))
colors = int(input("\nenter the amount of colors: "))
print ("\nThe colors in this game will be represented by the numbers 0-" + str(colors - 1) + " so make sure to attribute each number to a color.")
repeat = bool(input("\nwith repeat (True/False): "))
mastermind_solve(colors, slots, repeat)

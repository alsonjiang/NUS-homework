import random

def monty_hall(n):
    wins = 0
    run_count = 0

    while run_count < n:
        switch = random.randint(0,1) #randomly generates if switch or not
        car = random.randint(0,2)
        initial_guess = random.randint(0,2)
        run_count += 1

        if switch:
            if initial_guess == car:
                wins += 1
            else:
                second_guess = random.randint(0,2) and not initial_guess
                if second_guess == car:
                    wins += 1
                else:
                    continue

        else:
            if initial_guess == car:
                wins += 1
            else:
                continue
    
    return wins/n

print(monty_hall(100000))
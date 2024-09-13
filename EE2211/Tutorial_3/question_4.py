# throw two fair six-sided dice. Assume each throw is independent
# a. P(sum of dice = 7)

num_of_sevens = 0

outcomes = [die1 + die2 for die1 in range(1,7) for die2 in range(1,7)]

for index, sum in enumerate(outcomes):
    #print(f"Outcome {index + 1}: Sum = {sum}")
    if sum == 7:
        num_of_sevens += 1

print(num_of_sevens)
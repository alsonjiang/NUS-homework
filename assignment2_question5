def find_winners(factor_digit,must_have_digit,n):
    potential_winner = 0
    multiple = 1
    winners = []

    while potential_winner <= n:
        potential_winner = factor_digit * multiple 
        multiple += 1
        if str(must_have_digit) in str(potential_winner) and potential_winner <= n:
            winners.append(potential_winner)
        else:
            continue

    return len(winners), winners

print(find_winners(9,1,15))

"""
def find_winners(factor_digit,must_have_digit,n):
    multiple = 1
    winners = []
    for i in range(n):
        potential_winner = factor_digit * multiple 
        multiple += 1
        if str(must_have_digit) in str(potential_winner) and potential_winner <= n:
            winners.append(potential_winner)
            i += 1
        else:
            i += 1
    return len(winners)
"""




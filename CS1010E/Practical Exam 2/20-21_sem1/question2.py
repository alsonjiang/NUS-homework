#premium burger rules
# 1. bun is free
# 2. all prices are integers
# 3. 'C' = cheese, 'V' = veggie, 'P' = patty, 'A' = abalone
# 4. prices given in dict, NOT sorted
# 5. for every price, next price is more than 2x of previous price.
# 6. every ingredient only can appear ONCE
# 7. must have two buns - one start, one end

#2.1 Most expensive burger
#MOST expensive ingredient at the top
#output -> (pair of burger: str, money left: int)

def most_expensive_burger(money: int, price_dict: dict) -> tuple:
    #resulting burger
    burger = ''

    #sort dict in descending orderof price = item[1]
    sorted_ingredients = sorted(price_dict.items(), key=lambda item: item[1], reverse=True)
    
    #for every item = tuple, ingredient is index 0, price is index 1
    for ingredient, price in sorted_ingredients: #ingredient is a list of tuples -> ('A', 31)...etc
        if money >= price:
            burger += ingredient #add ingredient to burger str
            money -= price #subtract price of ingredient

    if burger: #if burger != '' (empty str)
        burger = 'B' + burger + 'B'

    return (burger, money)

#print(most_expensive_burger(25, {"C": 1, "V": 3, "P": 11, "A": 31}))
#print(most_expensive_burger(55, {'C':1,'W':2,'I':4,'T':9,'O':20,'V':41,'S':85}))

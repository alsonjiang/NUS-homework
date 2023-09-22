def make_empty_order():
    return ()

def add_item_to_order(order,item):
    return order + (item,)


# This function calls item_price(item) that should be implemented in Q3 feature 1
def print_receipt(order):
    if not order:
        print("You have no item in your order.")
        return
    print("Your orders:")
    for b in order:
        print(f'{b} ${item_price(b)}')
    print("--------------")
    print(f'Total: {total_price(order)}')

# This function calls item_price(item) that should be implemented in Q3 feature 1
def total_price(order):
    total = 0
    for i in order:
        total += item_price(i)
    return total

def remove_order(order,item):
    orderl = list(order)
    if item in orderl:
        orderl.remove(item)
        return tuple(orderl)
    else:
        print(f'The item {item} is not in the order.')
        return None

def enough_money(order, money_in_my_pocket):
    return total_price(order) <= money_in_my_pocket

def burger_price(burger):
    price = 0
    for char in burger:
        if char == 'B':
            price += 5
        elif char == 'C':
            price += 8
        elif char == 'P':
            price += 9
        elif char == 'V':
            price += 6
        elif char == 'O':
            price += 5
        elif char == 'M':
            price += 7
    return price

#-------------------Feature 1 Template------------------#
#Fries, F: S = $4, M = $S+1, L = $S+2
#Drinks, D: S = $3, M = $S+1, L = $S+2
#max. 1 portion of fries and drinks
#NO fries or drinks allowed WITHOUT burger

def item_price(item: str) -> int:
    item = item.upper()

    upsize_prices = {
        'S' : 0,
        'M' : 1,
        'L' : 2,
    }

    if 'D' in item:
        return 3 + upsize_prices[item[1]]

    if 'F' in item:
        return 4 + upsize_prices[item[1]]
    
    else:
        return burger_price(item)

#print(item_price('BVPB'))

#-------------------Feature 2 Template------------------#
#could have multiple burgers, drinks, and fries in the order

def total_price_with_set_discount(order: list) -> int:
    total_price = 0
    sets, burger_counter, drink_counter, fries_counter = 0, 0, 0, 0

    #calculate price of each item, and count how many of each type
    for item, value in enumerate(order):
        total_price += item_price(value)
        if 'B' in value:
            burger_counter += 1
        elif 'D' in value:
            drink_counter += 1
        elif 'F' in value:
            fries_counter += 1
    
    #count how many sets are there in an order
    sets = min(burger_counter, drink_counter, fries_counter)
    
    #return final amount = total amount - (no. of sets * 10)
    return total_price - sets * 10
    
#print(total_price_with_set_discount(['BVPB','BCVB','FL','DS']))

#-------------------Feature 3 Template------------------#

def get_lucky_burger(money_in_pocket: int, max_burger_size: int) -> list:
    return []


#Example order process
''' 
my_order = make_empty_order()
my_order = add_item_to_order(my_order,'BVPB')
my_order = add_item_to_order(my_order,'BCPCPB')
my_order = add_item_to_order(my_order,'BPCBPCB')
my_order = add_item_to_order(my_order,'DL')
my_order = add_item_to_order(my_order,'FM')
my_order = add_item_to_order(my_order,'FL')
my_order = add_item_to_order(my_order,'DM')
print_receipt(my_order)
print(f"Price after meal set discount: {total_price_with_set_discount(my_order)}")

#Example getting lucky burger

get_lucky_burger(75, 10)
'''

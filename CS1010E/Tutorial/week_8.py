#map, filter, reduce

#part 1: map and filter
L = [9, 2, 1, 3, 4, 5, 6]

#print(map(lambda x: x > 2, L)) #creates map object
#print(list(map(lambda x: x > 2, L))) #a list of T or F based on conditions acted on lst items
#print(list(filter(lambda x:x>2,L))) #a list of only items > 2 from L
#print(map(lambda x: 'o' if x%2 else 'e',L)) #creates a map object. 'o' for odd nums, 'e' for even nums.
#print(list(filter(lambda x: 'o' if x%2 else 'e',L))) #this doesn't work as expected. it returns the original list, L. filter filters based on True and False 
#print(map(str,list(filter(lambda x:x%2,L)))) #first filters out only odd nums. make a list. turn all items in that list into str. creates a map object. (if want to create a list need to list() the whole thing)
#print(str(list(filter(lambda x:x>30,map(lambda x:x*x,L))))) #first square every item in L. keep only items > 30. output a list. output the list as a str 


#part 2: scale/square tuples
tup = (2, 4, 1, 7, 5)
tup_squared = tuple(map(lambda x: x*x, tup)) #squaring, (4,16,1,49,25)
tup_scaled = tuple(map(lambda x: x*3, tup)) #x3
#print(tup_squared)
#print(tup_scaled)


#part 3: sum digit square
result = sum(item for item in map(lambda x: x*x, tup)) #4+16+1+49+25
#don't need to turn it into tuple for outputting if applying sum function
#result == result_2
result_2 = result = sum(item for item in tuple(map(lambda x: x*x, tup)))

#print(result, result_2) #95 95


#part 4: taylor series using map()

#part 5: reduce()
def reduce(f, seq):
    if not seq:
        return seq
    first = seq[0]
    for i in seq[1:]:
        first = f(first, i)
    return first

#print(reduce(lambda x, y: x+y, [1,2,3,4]))

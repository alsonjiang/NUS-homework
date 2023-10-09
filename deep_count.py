#week 7 lecture notes

#count a sequence including lists in lists...
def deepCount(seq):
    if seq == []:
        return 0
    elif type(seq) != list:
        return 1
    else:
        return deepCount(seq[0]) + deepCount(seq[1:])
    
#square every item, including those in lists in the list
def deepSquare(seq):
    if seq == []:
        return seq
    elif type(seq) != list:
        return seq*seq
    else:
        return [deepSquare(seq[0])] + deepSquare(seq[1:])

#increment every item by 1
def deepIncrement(seq):
    if seq == [] or seq == ():
        return seq
    elif type(seq) != list:
        return seq + 1
    else:
        return [deepIncrement(seq[0])] + deepIncrement(seq[1:]) 
    
#deep map!
def deepMap(func, seq):
    if seq == []:
        return seq
    elif type(seq) != list:
        return func(seq)
    else:
        return [deepMap(func,seq[0])] + deepMap(func, seq[1:])

lst = [1, 2, 3, [1, 2], [2, 3, 4, [1, 2, 3]], [3, 4, 5]]
res = deepMap(lambda x: x/2, lst)
#print(res)

#deep copy illustration
lst2 = lst.copy()
#this .copy() is a shallow copy
#changing lst items changes lst2 items as well

lst3 = deepMap(lambda x:x, lst)
#lst3 is a deep copy of lst
#changing lst items does NOT change lst3 items

print(lst) #[1, 2, 3, [1, 2], [2, 3, 4, [1, 2, 3]], [3, 4, 5]]
lst[3][0] = 999
print(lst2) #[1, 2, 3, [999, 2], [2, 3, 4, [1, 2, 3]], [3, 4, 5]]
print(lst3) #[1, 2, 3, [1, 2], [2, 3, 4, [1, 2, 3]], [3, 4, 5]]

#purpose of deep copy -> copying directories 
#map() is a powerful function, solve graphs, n-dim, trees

#if I just want to output a list with all elements, stipped of nested lists
def flatten(seq):
    if seq == []:
        return seq
    elif type(seq) != list:
        return [seq]
    else:
        return flatten(seq[0]) + flatten(seq[1:])

flatten_lst = flatten(lst)
print(flatten_lst) #[1, 2, 3, 999, 2, 2, 3, 4, 1, 2, 3, 3, 4, 5]


#python I/O
def write_something():
    with open('my_file.txt', 'w') as f:
        f.write("This is my first line" + "\n")
        f.write("This is my second line" + "\n")

#rstrip(), lstrip(), split() to remove all invisible character like \n
def read_something():
    with open('my_file.txt', 'r') as f:
        for line in f:
            print(line.rstrip('\n').split(','))

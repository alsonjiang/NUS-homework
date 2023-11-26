#tuple, list, iterables

#part 1: tuples
tup_a = (10,11,12,13)
tup_b = ('CS', 1010)
tup_c = tup_a + tup_b #(10,11,12,13,'CS',1010)
tup_d = tup_b[0] * 4 #CSCSCSCS
tup_e = tup_d[1:]
tup_f = tup_d[::-1]
tup_g = tup_d[1:-1:2] #SSS
tup_h = tup_d[-1:6:-2]

tup_i = (1) #this is an integer
tup_j = (1,) #this is a tuple


#part 2: lists
lst_a = ['CS', 1010]
lst_b = ['E',('is', 'easy')] 
lst_c = lst_a + lst_b

#lst_b[1] = 2030
#tup_b[1] = 2030 #-> error
cpy_b = lst_b[:] #creates a shallow copy, independent of lst_b. change cpy_b != change lstb
cpy_b[1] = 'is hard'

lst_d = [1, [2], 3]
cpy_d = lst_d[:]
#print(lst_d is cpy_d) #-> False
#print(lst_d[1] == cpy_d[1]) #-> True

#part 3: list mutation
lstx = [1,2,3]
lsty = lstx #creates a pointer called lsty back to lstx. change x = change y

#variable scoping
a = 4  
def foo(x):     
    x = x * 2     
    print(x)  
#print(a) #4
#foo(a) #8
#print(a) #4

lsta = [1,2,3]  
def foo2(lst):     
    lst[0] = lst[0]*2     
    lst[1] = lst[1]*2     
    print(lst)  
print(lsta) 
foo2(lsta) 
print(lsta)





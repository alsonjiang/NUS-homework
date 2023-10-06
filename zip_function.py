tuple_a = (1,3,5,7,9)
tuple_b = (2,4,6,8,10)

a = (1,3,5)
b = (2,4,6,8,10,12)

def interleaved_tuple(tuple_a,tuple_b):
    interleaved = ()
    counter = 0

    for i, j in zip(tuple_a, tuple_b):
        interleaved += (i, j)
        counter += 1
    for i in range(counter,max(len(tuple_a), len(tuple_b))):
        if tuple_a not in interleaved:
            interleaved += (tuple_a[i],)
        if tuple_b not in interleaved:
            interleaved += (tuple_b[i],)

    return interleaved

#print(interleaved_tuple(a, b))
#(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def interleaved_tuple_adv(tuple_a,tuple_b):
    interleaved = ()
    len_a, len_b = len(a), len(b)
    max_len = max(len_a, len_b)

    for i in range(max_len):
        if i < len_a:
            interleaved += (tuple_a[i],)
        if i < len_b:
            interleaved += (tuple_b[i],)

    return interleaved

print(interleaved_tuple_adv((2,4,6,8,10,12),(1,3,5)))
#print(interleaved_tuple(a,b))

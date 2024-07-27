def stern_brocot(n):
    if n == 0:
        return [(0, 1), (1, 1)]
    else:
        prev_sequence = stern_brocot(n-1)
        new_sequence = []

        for i in range(len(prev_sequence) - 1):
            a, b = prev_sequence[i]
            c, d = prev_sequence[i+1]
            new_sequence.append((a, b))
            new_sequence.append((a+c, b+d))

        new_sequence.append((1, 1))
        return new_sequence

# Test
print(stern_brocot(2))

"""
0: [(0,1),                      (1,1)]
1: [(0,1),        (1,2),        (1,1)]
2: [(0,1), (1,3), (1,2), (2,3), (1,1)]
"""
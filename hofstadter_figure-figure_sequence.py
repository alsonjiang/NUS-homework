import sys
sys.setrecursionlimit(10_000)

#remember values of n calculated for r and s
r_memo = {1: 1}
s_memo = {1: 2}

def R(n):
    if n in r_memo: #if value found in dict, return it
        return r_memo[n]
    r_memo[n] = R(n-1) + S(n-1) #formula given in qn
    return r_memo[n]

def S(n):
    if n in s_memo: #if value found in dict, return in
        return s_memo[n]
    last_s = s_memo[max(s_memo.keys())]
    next_s = last_s + 1
    while next_s in r_memo.values() or next_s in s_memo.values():
        next_s += 1
    s_memo[n] = next_s
    return s_memo[n]

print(R(100))

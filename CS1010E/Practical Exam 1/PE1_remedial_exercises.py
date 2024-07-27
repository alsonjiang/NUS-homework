#hofstadter female and male sequence

def f(n):
    if n == 0:
        return 1
    return n - m(f(n-1))

def m(n):
    if n == 0:
        return 0
    return n - f(m(n-1))


#PE20/21 SEM1 questions
def eI(s):
    def translate(c):
        if c == ' ':
            return '99'
        num = ord(c) - ord('A')
        if num < 10:
            return '0' + str(num)
        return str(num)
        
    out = ''
    for c in s:
        # translate s -> "xx"
        cc = translate(c)
        out = out + cc
    return out

def eR(s):
    def translate(c):
        if c == ' ':
            return '99'
        num = ord(c) - ord('A')
        if num < 10:
            return '0' + str(num)
        return str(num)
    if s == '':
        return ''
    # s <- 'HI SALLY'
    # shorter s <- 'I SALLY'
    # return '08991800111124'
    # what do I do to complete the program
    res = eR(s[1:])
    c = s[0]
    cc = translate(c)
    return cc + res

def offseting(c, step):
    nc = ord(c)- ord('A') # 0 <= nc <= 25
    newn = (nc + step) % 26
    return chr(newn + ord('A'))

def deoffset(c, step):
    return offseting(c, - step)

def decode(s,step):
    out = ''
    for i in range(0, len(s), 2):  # '1213'
        v = int(s[i:i+2])
        if v == 99:
            out = out + ' '
            continue
        after_offset = (v - step) % 26
        c = chr(ord('A') + after_offset)
        out = out + c
    return out

def decode_with_love(msg):
    for offset in range(26):
        res = decode(msg,offset)
        if 'LOVE' in res:
            return res
    return None

#assignment4 qn 2
def mr(R,n):
    sR = sorted(R)
    i = 0
    j = len(sR)-1
    out = []
    while i < j:
        val = sR[i] + sR[j]
        if  val == n:
            out.append((sR[i],sR[j]))
            i += 1
            j -= 1
        elif val > n:
            j -= 1
        else:
            i += 1
    return out

#subset qn
def subset(s):
    if s == '':
        return ['']
    
    result = subset(s[1:])
    
    output = result.copy()
    for r in result:
        output.append(s[0] + r)

    return output

print(subset('ABC'))
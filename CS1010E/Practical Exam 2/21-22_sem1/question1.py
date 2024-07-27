#part 1: permutation cipher
#not allowed split, rsplit, join, map, filter

#splt message into groups of N characters
#reverse each set of strings
#merge all together

#iterative permutation cypher
def per_cipher_i(s: str, n: int) -> str:
    encrypted = ''
    # Iterate over the string in steps of n
    for i in range(0, len(s), n):
        # Check if the remaining characters are less than n
        if i + n > len(s): 
            # Reverse the remaining characters and add to encrypted string
            encrypted += s[i:][::-1]
        else:
            # Reverse the group of n characters and add to encrypted string
            encrypted += s[i:i+n][::-1]
    
    return encrypted

#print(per_cipher_i('12345678910',3))


def per_cipher_r(s: str, n: int) -> str:
    encrypted = ''
    if not s:
        return ''
    if n < len(s): #still able to group into n groups
        encrypted += s[0:n][::-1] 
        return encrypted + per_cipher_r(s[n:], n)
    if n > len(s):
        encrypted += s[0:][::-1]
    
    return encrypted

#print(per_cipher_r('12345678910',3))

#one-liner of part 1
def per_cipher_o(s: str, n: int) -> str:
    return 

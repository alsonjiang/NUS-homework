#encryption (30 marks)
#s1 will only contain lower case alphabets OR nothing
#s2 will only contain 0-9 OR nothing
#len s1 = len s2
#multiplier, m -> any integer, incl 0 or -ve
def encode_I(s1: str, s2: int, m: int) -> str:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    output = '' #final output to be concat-ed
    count = 0 #used to iterate through s2

    for char in s1:
        transformed_char = letters.index(char) + ( int(s2[count]) * m ) 
        #take the corresponding digit in s2, turn to int, multiply by m, find this result in the letters list
        output += str(letters[transformed_char % len(letters)])
        #find the result in letters list with % to allowing list wrapping, turn to str, concat to output
        count += 1
        #add count to be able to iterate through next val of s2

    return output

def encode_I_by_prof(s1, s2, m):
    ans = ''
    for i in range(len(s1)):
        ans += chr(ord('a') + ((ord(s1[i]) - ord('a') + (int(s2[i])*m))%26))
    return ans

#print(encode_I('spyxfamily','2222222222',1))
print(encode_I_by_prof('spyxfamily','2222222222',1))
#print(encode_I('krmxhaeaba','9170109981',-2))

def encode_R(s1: str, s2: int, m: int) -> str:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if not s1:
        return ''
    
    transformed_char = letters.index(s1[0]) + ( int(s2[0]) * m )
    output = str(letters[transformed_char % len(letters)])
    return output + encode_R(s1[1:], s2[1:], m)

#print(encode_R('spyxfamily','2222222222',1))
#print(encode_R('krmxhaeaba','9170109981',-2))

#by prof
def encode_U(s1,s2,m): 
    return ''.join(list(map(lambda x: chr(ord('a') + ((ord(x[0]) - ord('a') + (int(x[1])*m))%26)), zip(s1, s2))))

print(encode_U('spyxfamily','2222222222',1))
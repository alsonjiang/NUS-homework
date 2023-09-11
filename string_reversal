
#iterative 1
def reverseString(s):
    output = ''
    l = len(s)
    for i in range(l):
        output += s[l-i-1] #5-0-1, #5-1-1, ...
    return output

print(reverseString("hello"))

#iterative 2
def reverseString2(s):
    output = ''
    for char in s:
        output = char + output #must be char + output
    return output

print(reverseString2("hello"))

#recursive
def reverseStringRecursive(s):
    if not s:
        return ''
    return reverseStringRecursive(s[1:]) + s[0]

print(reverseStringRecursive("hello"))
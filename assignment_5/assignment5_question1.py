def decipher_message(msg: str, guide: dict) -> str:
    output = ''
    for character in msg:
        if character in guide:
            output += guide[character]
        else:
            output += character
    
    return output

d1 = {'a': 'm', 'b': 'a', 'c': 'c', 'd': 'y', 'e': 't', 'f': 'v', 'g': 'o', 'h': 'u', 'i': 'x', 'j': 'e', 'k': 'j', 'l': 'w', 'm': 'f', 'n': 'z', 'o': 'd', 'p': 'l', 'q': 'i', 'r': 'k', 's': 'h', 't': 'n', 'u': 'g', 'v': 'b', 'w': 'q', 'x': 's', 'y': 'p', 'z': 'r'} 
print(decipher_message("esbtr dgh abzqg! vhe ghz yzqtcjxx qx qt btgesjz cbxepj!", d1))


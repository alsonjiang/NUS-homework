
#Write the iterative function encode_I(word) to encode the given word (str) from English to numeric (str).  
#You may assume that the word will only consists of uppercase characters.
def encode_I(word):
    encoded_word = ''
    codes = {
        "A":"00",
        "B":"01",
        "C":"02",
        "D":"03",
        "E":"04",
        "F":"05",
        "G":"06",
        "H":"07",
        "I":"08",
        "J":"09",
        "K":"10",
        "L":"11",
        "M":"12",
        "N":"13",
        "O":"14",
        "P":"15",
        "Q":"16",
        "R":"17",
        "S":"18",
        "T":"19",
        "U":"20",
        "V":"21",
        "W":"22",
        "X":"23",
        "Y":"24",
        "Z":"25",
        " ":"99",
    }
    for character in word:
        encoded_word += codes.get(character)
    
    return encoded_word

print(encode_I('HI SALLY'))


#Write the recursive function encode_R(word) to encode the given word (str) from English to numeric (str).  
#You may assume that the word will only consists of uppercase characters.
def encode_R(word):
    encoded_word = ''
    codes = {
        "A":"00",
        "B":"01",
        "C":"02",
        "D":"03",
        "E":"04",
        "F":"05",
        "G":"06",
        "H":"07",
        "I":"08",
        "J":"09",
        "K":"10",
        "L":"11",
        "M":"12",
        "N":"13",
        "O":"14",
        "P":"15",
        "Q":"16",
        "R":"17",
        "S":"18",
        "T":"19",
        "U":"20",
        "V":"21",
        "W":"22",
        "X":"23",
        "Y":"24",
        "Z":"25",
        " ":"99",
    }
    #return empty string if word is empty
    if not word: 
        return ''
    
    else:
        encoded_word = codes.get(word[0]) + encode_R(word[1:])
    
    return encoded_word

print(encode_R("HI SALLY"))

#if encode_R('ARE YOU FREE FOR DINNER TONIGHT') == "00170499241420990517040499051417990308131304179919141308060719":
    #print(True)

    

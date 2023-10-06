#Write a function decode(msg, offset) that will decode the message msg (str) 
#knowing that the message is offset by offset (int).
def decode(msg, offset):

    #split_up_msg is a list that indexes the digits (2 by 2) of the incoming msg 
    split_up_msg = []

    #decoded_msg is the final str of decoded words to be returned
    decoded_msg = ''

    #codes is a dictionary that stores all key-value pairs of letters-numbers
    codes = {
        "0":"A",
        "1":"B",
        "2":"C",
        "3":"D",
        "4":"E",
        "5":"F",
        "6":"G",
        "7":"H",
        "8":"I",
        "9":"J",
        "10":"K",
        "11":"L",
        "12":"M",
        "13":"N",
        "14":"O",
        "15":"P",
        "16":"Q",
        "17":"R",
        "18":"S",
        "19":"T",
        "20":"U",
        "21":"V",
        "22":"W",
        "23":"X",
        "24":"Y",
        "25":"Z",
        "99":" ",
    }

    #while msg is not empty, append every 2 digits to 1 index in split_up_msg list
    while msg != '':
        split_up_msg.append(int(msg[0:2]))
        msg = msg[2:]
    
    #remove offset from every index in split_up_msg except 99. %26 to retain correct lettering
    split_up_msg = [(item - offset)%26 if item != 99 else item for item in split_up_msg]

    #iterate over split_up_msg, match key-value and add to output str
    for item in split_up_msg:
        decoded_msg += codes.get(str(item))

    return decoded_msg

#print(decode("0007159919102399170713991207221917",123))
#print(decode('1213992305161603',5))


#Write a function decode_with_love(msg) that will decode the message msg (str) 
#without knowing the offset and return the decoded message with the word "LOVE" in it.
#LOVE -> 11142104
def decode_with_love(msg):
    offset = 0
    split_up_msg = ''
    love = ['11','14','21','04']

    while msg != '':
        split_up_msg.append(int(msg[0:2]))
        msg = msg[2:]

    for i in range(26):
        modified_msg = 
        if love in modified_msg:
            offset = i
    return offset
        

print(decode_with_love('0906190699021906992109069920161508209924069913162306'))



""" Failed code

    codes = {
    "0":"A",
    "1":"B",
    "2":"C",
    "3":"D",
    "4":"E",
    "5":"F",
    "6":"G",
    "7":"H",
    "8":"I",
    "9":"J",
    "10":"K",
    "11":"L",
    "12":"M",
    "13":"N",
    "14":"O",
    "15":"P",
    "16":"Q",
    "17":"R",
    "18":"S",
    "19":"T",
    "20":"U",
    "21":"V",
    "22":"W",
    "23":"X",
    "24":"Y",
    "25":"Z",
    "99":" ",
}
    
    decoded_msg = ''

    #indexes incoming digits 2 at a time
    split_up_msg = []

    #stores the difference in values between all the indexes
    difference_in_values = []

    #although offset is unknown, difference in values for each letter is always the same
    #the difference in values between the letters of LOVE are -3,-7,and 17
    sequence = [-3,-7,17]

    while msg != '':
        split_up_msg.append(int(msg[0:2]))
        msg = msg[2:]

    for i in range(len(split_up_msg)-1):
        difference_in_values.append(split_up_msg[i] - split_up_msg[i+1])

    #search for the starting index corresponding to L in LOVE
    for j in range(len(difference_in_values)):
        if difference_in_values[j : j + len(sequence)] == sequence:
            index_of_L = j
    
    #find the original offset
    original_index_of_L = split_up_msg[index_of_L] 
    difference = index_of_L - original_index_of_L

    print(index_of_L)
    print(original_index_of_L)
    print(difference)

    #offset original msg
    split_up_msg = [(item + difference)%26 if item != 99 else item for item in split_up_msg]

    #decode
    for item in split_up_msg:
        decoded_msg += codes.get(str(item))

    return decoded_msg"""
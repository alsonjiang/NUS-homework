#parentheses
#extract both ( and ) from a string
#check if parentheses are balanced

#iterative
def extract_parentheses_I(stmt: str) -> str:
    output = ''
    for character in stmt:
        if character in ['(', ')']:
            output += character
    
    return output #output in string format

#print(extract_parentheses_I('(1+2)*(3+(4-5))'))

#recursive
def extract_parentheses_R(stmt: str) -> str:
    if stmt == '':
        return ''
    
    if stmt[0] in ['(', ')']:
        return stmt[0] + extract_parentheses_R(stmt[1:])
    
    else:
        return extract_parentheses_R(stmt[1:])
    
#print(extract_parentheses_R('(1+2)*(3+(4-5))'))

#check balanced
#check if every open bracket has a close bracket
def check_balanced(stmt: str) -> bool:
    open = 0
    close = 0
    
    #get all the parantheses first
    result = extract_parentheses_R(stmt)
    for character in result:
        if character == '(':
            open += 1
        else:
            close += 1
    
    if open == close:
        return True

    return False
    
#print(check_balanced('(1+2)*(3+(4-5))'))





def is_anagram(s1, s2):
    s1_characters = []
    extra_characters = 0

    s1 = str(s1.upper())
    s2 = str(s2.upper()) #make sure both inputs are strings and uppercase

    for character in s1:
        s1_characters.append(character)
    
    for character in s2:
        if character in s1_characters:
            s1_characters.remove(character)
        else:
            extra_characters += 1
            continue
    
    if s1_characters == [] and extra_characters == 0:
        return True
    else:
        return False

print(is_anagram('Stressed','Desserts'))


    
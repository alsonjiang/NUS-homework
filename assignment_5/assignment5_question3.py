#name1 -> ancestor, name2 -> descendent
#key:value -> child:parent
parent = {'Amy':'Ben', 'May':'Tom', 'Tom':'Ben', 
          'Ben':'Howard', 'Howard':'George', 'Frank':'Amy', 
            'Joe':'Bill', 'Bill':'Mary', 'Mary':'Philip', 'Simon':'Bill', 
          'Zoe':'Mary'} 


def is_ancestor(name1: str, name2: str, pdict: dict) -> bool:
  #if it is the same person
  if name1 == name2:
    return False

  while name2 in pdict: #this execution of checking to prevent out of bounds
      if pdict[name2] == name1: #parent found
          return True
      name2 = pdict[name2] #move up, define new child

  return False
  
#print(is_ancestor('Amy', 'Tom', parent))


def is_related(name1: str, name2: str, pdict: dict) -> bool:

  def generate_ancestors(name: pdict): #function to return list of ancestor names
    seen = []
    while name in pdict:
      seen.append(name)
      name = pdict[name]
    return seen

  #check if both names have ancestor-descendent relationship
  if is_ancestor(name1, name2, pdict) or is_ancestor(name2, name1, pdict):
    return True

  #check if both names are from the same generation
  ancestors_1 = generate_ancestors(name1, pdict)
  ancestors_2 = generate_ancestors(name2, pdict)

  for name1_ancestors in ancestors_1:
     for name2_ancestors in ancestors_2:
        if name1_ancestors == name2_ancestors:
           return True
        
  return False

#print(is_related('Howard', 'Amy', parent))
#print(is_related('Amy', 'May', parent))
#print(is_ancestor('Amy', 'Tom', parent))
print(is_ancestor('Amy', 'Philip', parent))
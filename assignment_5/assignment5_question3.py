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
  
  #child's ancestor does not exist
  if name2 not in pdict.keys():
    return False
  
  #child's parent is name1
  if pdict[name2] == name1:
    return True
  
  #move up the tree to search, replacing child with his parent
  return is_ancestor(name1, pdict[name2], pdict)
  
#print(is_ancestor('Amy', 'Tom', parent))

def is_related(name1: str, name2: str, pdict: dict) -> bool:

  keys = pdict.keys() #all child
  values = pdict.values() #all parent
  
  #check if name1 and name2 are ancestor-descendent
  if is_ancestor(name1, name2, pdict) or is_ancestor(name2, name1, pdict):
    return True
  
  #check if they have a common ancestor (name1 and name2 same generation)
  if pdict[name1] == pdict[name2]:
    return True
  
  if name1 not in 

print(is_related('Amy', 'Philip', parent))
from random  import randint
from team import *

### DEBUG PRINT
DEBUG_PRINT = True
def dprint(s):
  if DEBUG_PRINT:
    print(s)

### CONSTANT FOR MAGE
MANA_COST = 20
MANA_RECOVERY = 30


### BASE CHARACTER
#inherit whenever possible
#NOT to mod FIGHTER AND MAGE
#should NOT override superclass method
#call superclass methods whenever possible
class Character(): #base class
  def __init__(self):
    self.name = ''
    self.maxhp   = 800
    self.hp      = 800
    self.maxmana = 0
    self.mana    = 0
    self.str     = 0
    self.int     = 0
    self.cost    = 9999999999
    self.alive   = True

  def act(self, my_team, enemy): #character's action
    return

  def got_hurt(self, damage): #character takes dmg
    if damage >= self.hp:
      self.hp = 0
      self.alive = False
      dprint(self.name + ' died!')
    else:
      self.hp -= damage
      dprint(self.name +
           f' hurt with remaining hp {self.hp}.')

  
### FIGHTER
class Fighter(Character): #each turn inflct dmg = strength on rand opp
  def __init__(self):
    super().__init__()
    self.name  = 'Fighter'
    self.maxhp = 1200
    self.hp    = 1200
    self.str   = 100
    self.cost  = 100

  def act(self, my_team, enemy):
    target = rand_alive(enemy)
    dprint(f'Hurt enemy {target} by damage {self.str}.')
    enemy[target].got_hurt(self.str)

  
### MAGE
class Mage(Character): #cast spell = intelligence, cost 20 mana. if <20mana, meditate
  def __init__(self):
    super().__init__()
    self.name    = 'Mage'
    self.maxmana = 50
    self.mana    = 50
    self.cost    = 200
    self.int     = 400

  def cast(self, my_team, enemy):
    self.mana -= MANA_COST
    target = rand_alive(enemy)
    dprint(f'Strike enemy {target} with spell')
    enemy[target].got_hurt(self.int)
    
  def act(self, my_team, enemy):
    if self.mana < MANA_COST:
      self.mana += MANA_RECOVERY
      dprint(f'Mana recover to {self.mana}.')
    else:
      self.cast(my_team, enemy)

### BERSERKER
class Berserker(Fighter): #cost 200G, if HP <= 0.5HP(max) -> STR*2
  def __init__(self):
    super().__init__()
    self.name = 'Berserker'
    self.cost = 200
  
  def act(self, my_team, enemy):
    if self.hp <= (self.maxhp / 2):
      self.str = 200
      target = rand_alive(enemy)
      dprint('Berserk mode! Attack double!' )
      dprint(f'Hurt enemy {target} by damage {self.str}.')
      enemy[target].got_hurt(self.str) #this "does" the damage
    
    else:
      #normal attack if HP > half.
      self.str = 100
      super().act(my_team, enemy) 


### ARCHMAGE
class ArchMage(Mage):
  def __init__(self):
    super().__init__()
    self.name = 'ArchMage'
    self.cost = 600
  
  def act(self, my_team, enemy):
    if self.mana < MANA_COST: #not enough mana = meditate
      self.mana += MANA_RECOVERY
      dprint(f'Mana recover to {self.mana}.')

    else:
      if count_alive(my_team) == 1: #if archmage the only one alive, kaboom
        self.kaboom(enemy)
      else:
        self.cast(my_team, enemy) #normal attack
  
  def kaboom(self, enemy): #heavy damage to ALL enemies
    self.mana -= MANA_COST
    dprint(f'Cast KABOOM to every enemy')
    for target in enemy: #iterate through the whole enemy list
      target.got_hurt((self.int)*2) #this "does" the damage = 2*int


### NECROMANCER
class Necromancer(Mage): 
  def __init__(self):
    super().__init__()
    self.name = 'Necromancer'
    self.cost = 400

  def act(self, my_team, enemy):
    if count_dead(my_team) > 0: #if there are dead members, try res first
      if self.mana < MANA_COST: #if not enough mana = meditate
        self.mana += MANA_RECOVERY
        dprint(f'Mana recover to {self.mana}.')
      
      else: #res random member w half hp
        self.revive(my_team)
  
    else: #if all members alive = normal mage move
      super().act(my_team, enemy)

  def revive(self, my_team):
    self.mana -= MANA_COST
    target = rand_death(my_team) #target is an int, since rand_death() returns an int
    member = my_team[target] #get the target character from list 
    member.alive = True
    member.hp = member.maxhp // 2
    dprint(f'Reviving member {member} with {member.hp} hp')

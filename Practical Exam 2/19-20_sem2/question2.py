### PE 02
import math
"""
Question 2: Catan
"""
#each player build house on tile
#each tile MAX 3 houses

#ROLLING
#if player has a house on the tile, player receives resource from tile
#if number 7,all players robbed

#TRADING
#wood and brick
#players may trade among each other
"""
2.1 Player
"""
class Player():
  def __init__(self, colour: str) -> None:
    self.colour = colour
    self.wood = 3
    self.brick = 3

  def get_colour(self) -> str:
    return self.colour
  
  def get_resources(self) -> tuple:
    return (self.wood, self.brick)
  
  def robbed(self) -> str:
    if (self.wood + self.brick) < 8:
      return (f'{self.colour} is safe from robber')
    
    self.wood = self.wood // 2
    self.brick = self.brick // 2
    #half kept and half taken away is the same thing
    return (f'{self.colour} is robbed of {self.wood + self.brick} resources')

  def trade(self, other_player, woods: int, bricks: int) -> str:
    pass #what is even the instructions???

  def build(self, tile) -> str:
    if tile.building == 3: #check if 3 building
      return ('tile does not have any space')
    
    else: # have space available to build
      if (self.wood < 2) or (self.brick < 2): #no resources though
        return (f'{self.colour} does not have enough resources to build')
    
      #have resources
      self.wood -= 2
      self.brick -= 2
      return (f'{self.colour} builds on tile')

"""
2.2 Tile
"""
class Tile():
  def __init__(self, tile_num: int, resource: str) -> None:
    self.tile_num = tile_num #integer
    self.resource = resource #"brick" or "wood"
    self.building = 0
  
  def get_number(self) -> int:
    return self.tile_num
  
  def get_resources(self) -> str:
    return self.resource
  
  def get_building(self) -> int:
    return self.building
  
  def produce(self) -> str:
    if self.building == 0:
      return (f'Tile {self.tile_num} does not produce any {self.resource}')
    
    return (f'Tile {self.tile_num} produces {self.building} {self.resource}')



### Test data (do not modify)

red    = Player("Red")
blue   = Player("Blue")
yellow = Player("Yellow")
brick1 = Tile(1, "brick")
wood1  = Tile(2, "wood")
brick2 = Tile(3, "brick")
wood2  = Tile(4, "wood")

### Test cases (comment out or remove before copying to Coursemology)
##print(red.build(brick1))
##print(brick1.produce())
##print(red.build(wood1))
##print(blue.build(wood1))
##print(yellow.build(brick1))
##print(brick1.produce())
##print(brick1.produce())
##print(wood2.produce())
##print(wood1.produce())
##print(wood1.produce())
##print(wood1.produce())
##print(blue.get_resources())
##print(red.get_resources())
##print(blue.trade(red, 5, 1))
##print(blue.trade(red, 1, 5))
##print(blue.trade(red, 2, 2))
##print(blue.get_resources())
##print(red.get_resources())

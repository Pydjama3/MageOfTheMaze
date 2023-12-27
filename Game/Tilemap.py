class Tilemap:
  def __init__(self, generated_thingymbob):
    self.tile_size = 20 #TODO: Change this to be a tile size variable
    self.map = map(self.display_map, generated_thingymbob)
    self.width = len(map[0])
    self.height = len(map)
    self.tile_map = []
    self.tile_map_size = (self.width * self.tile_size, self.height * self.tile_size)
    self.tile_map_pos = (0, 0)
    
  def display_map(self, input):
    return list(input)
    
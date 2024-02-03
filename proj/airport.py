class Airport:
  def __init__(self, name: str, flow: int, capacity: int):
    self.name = name
    self.flow = flow
    self.capacity = capacity
    
  def show(self):
    print(f"Airport name {self.name}\t  Flow : {self.flow}\tCapacity : {self.capacity}")
    

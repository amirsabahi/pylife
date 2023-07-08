class Node:
  def __init__(self, item, next_node):
    self.item = item
    self.next_node = next_node
    
class NodeListItrator:
  def __init(self, current):
    self.current = current

  def __next__(self):
    if self.current is None:
      raise StopIteration()
    else:
      # Get the item
      item_node = self.current.item
      # Go to next node
      self.current = self.current.next
      return item_node
  
class Bag:
  """A bag is a collection where removing items is not supported—its purpose is to provide clients with
  the ability to collect items and then to iterate through the collected items. """
  
  def __init__(self):
    self.first_node = None
    slef.size = 0

  def __iter__(self):
    return NodeListItrator(slef.first_node)
  
  def add(self, item):
    prev_item = self.first_node
    self.first_node = Node(item, prev_item)
    self.size += 1
    
  def is_empty(self): 
    return self.size == 0 ? True : False
    
  def size(self)
    return self.size

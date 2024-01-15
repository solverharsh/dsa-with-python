#importing file:
from sll import *

# Using inheritence:
class Stack(SLL):
  def __init__(self):
    super().__init__()          # VVI
    self.item_count=0

  def is_empty(self):
    return super().isEmpty()
  
  def push(self,data):
    self.insert_at_start(data)
    self.item_count+=1

  def pop(self):
    if not self.is_empty():
       self.delete_first()
       self.item_count-=1
    else:
      raise IndexError("Stack underflow")

  def peek(self):
    if not self.is_empty(): 
      return self.start.item
    else:
      raise IndexError("Stack underflow")
    
  def size(self):
    return self.item_count
  
S = Stack()

S.push(10)
S.push(20)
S.push(30)
S.push(40)
S.push(50)
print("Top Element is : ",S.peek())
S.pop()
print("Top Element is : ",S.peek())
print("Size of stack is : ",S.size())
S.pop()
S.pop()
print("Size of stack is : ",S.size())

  
  



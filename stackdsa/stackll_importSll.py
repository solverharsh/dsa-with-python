from sll import *

class Stack:
  def __init__(self):
    self.mylist=SLL()
    self.item_count=0
  
  def is_empty(self):
    return self.mylist.isEmpty()
  
  def push(self,data):
    self.mylist.insert_at_start(data)
    self.item_count+=1

  def pop(self):
    if not self.is_empty():
      self.mylist.delete_first()
      self.item_count-=1

  def peek(self):
    if not self.is_empty():
      return self.mylist.start.item 

  def size(self):
    return self.item_count

S = Stack()
S.push(10)
S.push(20)
S.push(30)
S.push(40)
S.push(50)
print(S.peek())
S.pop()
print(S.peek())
print(S.size())
print(S.is_empty())


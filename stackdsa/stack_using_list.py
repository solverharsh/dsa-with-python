# Implementation of Stack using List :

class Stack:
  def __init__(self):
    self.items=[]

  def is_empty(self):
    return len(self.items)==0

  def push(self,data):
    self.items.append(data)

  def pop(self):
    if not self.is_empty():
      return self.items.pop()
    else:
      raise IndexError("Stack is empty")
    
  def peek(self):
    if not self.is_empty():
      return self.items[-1]
    else:
      raise IndexError("Stack is empty")
    
  def size(self):
    return len(self.items)
  
  def print_elements(self):
    if self.is_empty():
      return 
    
    print(self.peek(),end=' ')
    self.pop()
    self.print_elements()
    
  
S = Stack()
S.push(10)
S.push(20)
S.push(30)
S.push(40)
S.push(50)
print("Top element is : ",S.peek())
print("Removed Element is : ",S.pop())
print("Top Element is : ",S.peek())
print("Size of stack is : ",S.size())
# S.print_elements()
# print(f"Top element is {S.peek()}")







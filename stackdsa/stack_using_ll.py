# Implementation of Stack using linked list concept:

class Node :
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Stack:
    def __init__(self):
        self.top =None
        self.item_count=0

    def is_empty(self):
        return self.top==None
    
    def push(self,data):
        n=Node(data,self.top)
        self.top=n
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
          temp=self.top.item
          self.top=self.top.next
          self.item_count-=1
          return temp
        else:
            raise IndexError("Stack is Empty/Underflow")
        
    def peek(self):
        if not self.is_empty():
          return self.top.item
        else:
            raise IndexError("Stack is Empty")

    def size(self):
        return self.item_count 

S =Stack()
S.push(10)
S.push(20)
S.push(30)
S.push(40)
S.push(50)
print("Number of Elements in stack is: ",S.size())
print("Top elementis : ",S.peek())
S.pop()
print("Size of stack: ",S.size())
print("Top element is : ",S.peek())

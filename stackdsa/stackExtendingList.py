# Stack using extending List :

class Stack(list):
    def is_empty(self):
        return len(self)==0
    
    def push(self,data):
        self.append(data)

    def pop(self):
        if not self.is_empty():
          return super().pop()
        else:
            raise IndexError("Stack is empty")
        
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty")
    
    def size(self):
        return len(self)
    
    #Restricting any functionality of parent class when inheriting :
    def insert(self,index,data):
        raise AttributeError("No attribute insert in stack")
    
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
# S.print_elements()
# S.insert(3,100)
S.pop()
S.print_elements()

        
class Stack():
    def __init__(self, maxSize) -> None:
        self.maxSize = maxSize
        self.list = []

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True 
        else:
            return False
        
    
    def push(self, value):
        if self.isFull():
            return "Full"
        else:
            self.list.append(value)
            return "Inserted"
    
     
    def pop(self):
        if self.isEmpty():
            return "Empty"
        else:
            self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Empty"
        else:
            return self.list[len(self.list) -1]
    
    def delete(self):
        self.list = None
    

customStack = Stack(5)
print(customStack.isFull())
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
# print(customStack)
customStack.pop()
print(customStack)
class Stack:
    def __init__(self):
        self.list = []

    def __str__(self) -> str:
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values )
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"
    
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

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.isEmpty())
print(customStack.peek())
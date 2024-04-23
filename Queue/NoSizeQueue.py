class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def enqueue(self, value):
        self.items.append(value)
        return "Inserted"
    
    def dequeue(self):
        if self.isEmpty():
            return "Empty"
        else:
            #remove first item in queue
            return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Empty"
        else:
            #grab first item in queue
            return self.items[0]
    
    def delete(self):
        # why not []??
        self.items = None




customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.peek())
customQueue.delete()

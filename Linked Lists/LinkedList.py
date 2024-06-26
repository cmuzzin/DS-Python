class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            # start string appending
            result += str(temp_node.value)
            #if next is not none add arrr to result and then update temp node for next iteration
            if(temp_node.next is not None):
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            #set new nodes next as previous head
            new_node.next = self.head
            #assign new head as new node
            self.head = new_node

        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            #start at head
            temp_node = self.head
            #loop over list before index and get last item up to insertion index
            for _ in range(index - 1):
                temp_node = temp_node.next
            # new node next ref points to the temp node next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

        return True
    
    def traverse(self):
        current = self.head
        index = 0
        while current:
            print(current.value)
            current = current.next
    
    def search(self, target):
        current = self.head
        while current:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1
    
    def get(self, index):
        if (index == -1):
            return self.tail.value
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        print(current.value)
        return current.value
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                #keeps moving over while not tail - second to last to tail
                temp = temp.next
                self.tail = temp
                temp.next = None
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1 or index == -1:
            self.pop()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length =- 1
        return popped_node
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)
# linked_list.prepend(5)
# linked_list.insert(2, 45)
# print(linked_list)
# linked_list.traverse()
# linked_list.search(45)

linked_list.get(2)
# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# Erin O'Connell

class LinkedList:

    def __init__(self, value = None):
        self.next = self 
        self.prev = self 
        self.value = value

    def is_sentinel(self): 
        return self.value is None
      
    def is_empty(self):
        return self.next is self and self.prev is self

    def is_last(self): 
        return self.next.is_sentinel()
   
    def last(self): 
        if self.is_last():
           return self 
        return self.next.last()   
  
    def append(self, appendee):
        if self.is_empty():
            self.prev = appendee
            appendee.next = self
            self.next = appendee
            appendee.prev = self
            return
        if self.is_sentinel():
            self.prev = appendee
            appendee.next = self
            self = self.last()
            self.next = appendee
            appendee.prev = self
            return
        return self.next.append(appendee)    
    
    def delete(self):
        self = self.next
        self.prev = self.prev.prev
        self = self.prev
        self.next = self.next.next

    def insert(self,insertee):
        self.next.prev = insertee
        insertee.next = self.next
        self.next = insertee
        insertee.prev = self 

    def at(self, index):
        i = 0
        if self.is_sentinel():
            while i < index:
                self = self.next
                i += 1
            return self 
        return self.next.at(index)   

    def search(self, value):
        if self.value == value:
            return self
        elif self.next.value is None:
            return None
        return self.next.search(value)

    def insert_in_order(self, insertee):
        if self.is_empty():
            self.append(insertee)
            return
        elif self.next.value is None: 
            self.insert(insertee)
            return
        elif insertee.value < self.next.value:
            self.insert(insertee)
            return                        



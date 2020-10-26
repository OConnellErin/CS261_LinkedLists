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
        return self.next.is_last()   

    def append(self, appendee):
        self.prev = appendee
        self.next = appendee
        appendee.prev = self
        appendee.next = self 

        # self.prev.next = appendee
        # appendee.next = self
        #needs two more  


#for insert put the passed node one after the sential node
#delete just make the pointers point at different stuff 

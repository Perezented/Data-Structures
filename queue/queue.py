"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        # set the set size of the array so the program does not need to count everything.
        return self.size

    def enqueue(self, value):
        # add an item to the back of the line, index 0
        self.storage.insert(0, value)
        # set the size ot the length of the storage array.
        self.size = len(self.storage)

    def dequeue(self):
        # if you cannot dequeue because there is nothing in the array, return
        if self.size == 0:
            return
        # otherwise we want the length of the array to change.
        else:
            # and remove the item in the front, index -1
            self.size = self.size - 1
            return self.storage.pop()




# needing to make a node for Queue.
# class QueueNode:
#     # Have normal head and tail
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0

#     # def get_next(self):
#     #     return self.next

#     def set_next(self, new_next):
#         self.next = new_next

#     # adding to tail

#     def enqueue(self, value):
#         # set the size of the array up.
#         self.size += 1
#         # make a new node item from value
#         new_node = Queue(value)
#         # add the node item to the end of the Node list
#         if self.head is None and self.tail is None:
#             self.head = new_node
#             # set the new node ot be the tail
#             self.tail = new_node
#         else:
#             # set the old tail's next to refer to the new Node
#             self.tail.set_next(new_node)
#             # reassign self.tail to refer to the new Node
#             self.tail = new_node

#     def __len__(self):
#         return self.size

#     def dequeue(self):
#         # if there is nothing in the list to dequeue, then return
#         if self.head is None and self.tail is None:
#             return
#         # else
#         # remove 1 number from the size count
#         self.size -= 1
#         # we want to remove the old tail
#         current = self.head
#         while current.next is not self.tail:
#             current = current.next
#         val = self.tail
#         # set the tail to the previous item in the node list
#         self.tail = current
#         return val



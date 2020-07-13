"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        # returning the length of the array.
        return len(self.storage)

    def push(self, value):
        # want to append the value to the array
        return self.storage.append(value)

    def pop(self, value):
        # if there are no items in the array, just return
        if self.storage is None:
            return
        # want to return the top of the stack and delete the item.
        else:
            return self.storage.pop()

"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # label a new node for the value
        newNode = Node(value)
        # if there is no current head
        if self.head is None:
            # set it as the head and tail
            self.head = newNode
            self.tail = newNode
        else:
            # otherwise just set it as the node before the head node
            self.head.prev = newNode
            self.head = newNode
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
        # # if there is no head node, just return 
        # if self.head is None:
        #     return
        # else:
        #     # make the next node the head node
        #     self.head.next = self.head
        #     # set a const to the previous node, which was the head node not no more
        #     oldHead = self.head.prev
        #     # remove the previous node
        #     self.head.prev = None
        #     # return said const
        #     return oldHead


    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        pass
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # FROM EARLIER...
        # if we have an emply linked list
        if self.head is None and self.tail is None:
            return
        # if we have a non empty list
        # set the tail to be none
        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
        val = self.tail.get_value() 
        # move self.tail to the Node right before
        self.tail = current
        return val
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # FROM EARLIER...
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value

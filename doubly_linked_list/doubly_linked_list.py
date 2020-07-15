"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.next = new_prev
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
        newNode = ListNode(value)
        # if there is no current head
        if self.head is None:
            # set it as the head and tail
            self.length = 1
            self.head = newNode
            self.tail = newNode
        # else if the self head is the self tail, only 1 item
        elif not self.head.get_next():

            self.length += 1
            self.head = newNode
            self.head.next = self.tail
            self.tail.prev = newNode
        else:
            # otherwise, there are multiple items
            # add one item to the length
            self.length += 1
            # the previous head will need to connect to the new node
            self.head.prev = newNode
            # self.head will need to connect to the previous head
            self.head.prev.next = self.head
            # have the self head be new node
            self.head = newNode


    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # if we have an empty list, no head and no tail, length is 0,  return
        if self.head is None:
            return
        # else there is items afterward
        else:
            self.head = self.head.get_next()
            self.length -= 1
            return self.head.get_prev()




        # set the next item to the head


    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # set the value to a node
        addingTail = ListNode(value)
        # add it as the tail of the node list
        self.tail.set_next(addingTail)
        # remove the old tail and set it as the new node value.
        self.tail = addingTail
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    # FROM EARLIER...
    def remove_tail(self):
        if self.head is None:
            return

        current = self.head

        while current.get_next() and current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        self.tail.set_next(None)
        return value
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # selecting the head as the current. attempting to locate the node
        current = self.head
        while current:
            if current.get_value() == node:
                self.head = current
                current = None
            return False
        
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

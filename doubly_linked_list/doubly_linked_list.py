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
            # set the next item to the head
            oldHead = self.head.value
            if self.tail == self.head:
                self.tail = None
            self.head = self.head.next
            # remove an number from length
            self.length -= 1
            return oldHead



    """
    Wraps the given value in a ListNode
     and inserts it as the new tail of the list.
      Don't forget to handle the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # if there is no tail, make item tail and head
        new_node = ListNode(value)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
            self.length += 1
        # elif there is a tail already
        else:
            # make old tail have new tail as next
            self.tail.next = new_node
            # make new node the new tail
            new_node.prev = self.tail
            # make the old tail this new tails prev
            self.tail = new_node
            # add a number
            self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    # FROM EARLIER...
    def remove_from_tail(self):
        # if there is no tail, return
        if self.tail is None:
            return
        # else if there is only 1 item
        elif not self.tail.get_prev():
            # remove tail and head to None
            self.head = None
            returnMe = self.tail.value
            self.tail = None
            # remove digit from length
            self.length -= 1
            return returnMe
        # else if there is mult items
        else:
            # make tail prev the new tail
            returnMe = self.tail.value
            self.tail = self.tail.prev
            # returnMe = self.tail.next.value
            # make new tail next to none
            self.tail.next = None
            self.length -= 1
            return returnMe
        # return removed node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
            self.add_to_head(value)
        else:
            self.delete(node)
            self.add_to_head(value)
        

        """
        Removes the input node from its current spot in the 
        List and inserts it as the new tail node of the List.
        """

    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        if node is self.head:
            self.remove_from_head()
            self.add_to_tail(value)
        else:
            self.delete(node)
            self.add_to_tail(value)
        # if self.tail is None:
        #     return
        # # if the item is the tail, just return
        # if self.tail == node:
        #     return
        # # elif the item is the head, move it to the tail
        # h = self.head
        # t = self.tail
        # if self.head == node:
        #     self.head.set_prev(self.tail)
        #     self.add_to_tail(self.head.value)
        #     self.remove_from_head()
        # else:
        #     current = self.head.next
        #     if current == node:
        #         current.set_prev(self.tail)
        #         current.set_next(None)
        #         self.tail.set_next(current)
        #         self.delete(node)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):

        currently = self.head.get_next()
        if self.head == node:
            self.remove_from_head()
        elif self.tail == node:
            self.remove_from_tail()
        elif self.head != node:
            if self.head.get_next() is not None:
                if currently.get_value() == node:
                    currently.get_prev().set_next(currently.get_next())
                    currently.get_next().set_prev(currently.get_prev())
                    currently.set_next(None)
                    currently.set_prev(None)
                    self.length -= 1
                else:
                    currently = currently.get_next()
                    self.length -= 1


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

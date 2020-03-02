# Howard Lichtman
# February 21, 2020
# Second representation of a Linked List

"""
The ListNode is only used in the SingleLinkedList so
it has been added in the same file.  If this were to
be used elsewhere, it would have been added to its
own file.
"""


class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)


class NewLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return str(nodes)

    def push_head(self, data):
        new_node = ListNode(data=data)
        new_node.next = self.head
        self.head = new_node

    def push_end(self, data):
        new_node = ListNode(data=data)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def pop_head(self):
        removed_value = self.head
        self.head = self.head.next
        return removed_value.data

    def pop_end(self):
        current_node = self.head
        previous_node = self.head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        return current_node.data

    def delete_node(self, key):
        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if temp == None:
            return

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None

    def contains(self, value):
        current_node = self.head
        while current_node.next or current_node.data == value:
            if current_node.data == value:
                return True
            current_node = current_node.next

        return False

    def clear(self):
        self.head = None


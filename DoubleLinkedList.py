# Howard Lichtman
# February 26, 2020
# Representation of a Double Linked List

"""
The ListNode is only used in the DoubleLinkedList so
it has been added in the same file.  If this were to
be used elsewhere, it would have been added to its
own file.
"""


class ListNode:
    """
    A node in a double-linked list.
    """
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

    def __repr__(self):
        return repr(self.data)


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return str(nodes)

    def push_head(self, new_data):
        new_node = ListNode(data=new_data)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def push_end(self, data):
        # 1. allocate node 2. put in the data
        new_node = ListNode(data = data)
        current = self.head

        # 3. This new node is going to be the
        # last node, so make next of it as NULL
        new_node.next = None

        # 4. If the Linked List is empty, then
        #  make the new node as head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        # 5. Else traverse till the last node
        while current.next is not None:
            current = current.next

        # 6. Change the next of last node
        current.next = new_node

        # 7. Make last node as previous of new node */
        new_node.prev = current

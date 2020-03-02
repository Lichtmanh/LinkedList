# Howard Lichtman
# March 1, 2020
# Driver to test Double Linked List

from DoubleLinkedList import DoubleLinkedList

lst = DoubleLinkedList()
print(lst)
lst.push_head(25)
lst.push_head(55)
lst.push_head(100)
print(lst)

lst.push_end(30)
print(lst)

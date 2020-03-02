# Howard Lichtman
# February 17, 2020
# Driver to test Linked List

from NewLinkedList import NewLinkedList

# Create the empty list
lst = NewLinkedList()
print("Here is the empty list:")
print(lst)

print("10 is added to the head")
lst.push_head(10)
print("50 is added to the head")
lst.push_head(50)
print("Here is the list with two values added")
print(lst)
lst.push_head(30)
lst.push_head(40)
print(lst)
lst.delete_node(50)
print(lst)

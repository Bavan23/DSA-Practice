class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")


def remove_nth_from_end(my_linked_list, n):
    dummy = Node(0)  
    dummy.next = my_linked_list.head  # Point dummy to the head
    slow = fast = dummy  # Initialize slow and fast pointers

    # Move fast pointer ahead by n+1 steps
    for _ in range(n + 1):
        if fast:
            fast = fast.next

    # Move both pointers until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next

    # Remove the nth node
    slow.next = slow.next.next

    # Update the head in case the first node was removed
    my_linked_list.head = dummy.next


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print("Original Linked List:")
my_linked_list.print_list()

n = 2
remove_nth_from_end(my_linked_list, n)

print("\nLinked List after removing {}-th node from end:".format(n))
my_linked_list.print_list()


























# for returing value i.e- LL: Find Kth Node From End ( ** Interview Question)

""" class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  
  
def find_kth_from_end(my_linked_list,k):
    slow=fast=my_linked_list.head
    
    for _ in range(k):
        if fast is None:
            return None
        fast=fast.next
    
    while fast:
        slow=slow.next
        fast=fast.next
        
    return slow
    
    




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4



"""

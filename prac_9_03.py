class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()

# Main program
ll = LinkedList()

# Take input from user to add nodes to the linked list
while True:
    user_input = input("Enter a value to add to the linked list (or press enter to finish): ")
    if user_input == "":
        break
    ll.insert(int(user_input))

# Print the linked list
print("Linked list:")
ll.print_list()

'''
1.We define a Node class that represents a single node in the linked list.
Each node contains a data attribute and a next attribute that points to the next node in the list.

2.We define a LinkedList class that represents the linked list itself.
Each linked list has a head attribute that points to the first node in the list.

3.The insert method of the LinkedList class adds a new node to the end of the linked list.
If the linked list is empty, the new node becomes the head. Otherwise, 
we traverse the list to find the last node and append the new node to the end.

4.The print_list method of the LinkedList class prints the values of all the nodes in the
list by traversing the list from the head to the end and printing each node's data attribute.

5.In the main program, we create a new LinkedList object and use a loop to take user input and add it to the list.
We exit the loop when the user enters an empty value (i.e., presses enter without typing anything).

Finally, we print the linked list by calling the print_list method of the LinkedList object.
'''

class Node:
    def __init__(self, data):
        self.data = data                                   # Storing the data
        self.next = None                                   # Pointing to the next node
        self.prev = None                                   # Pointing to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None                                  

    def insert(self, data):                                # Inserting a new node at the end of the list
        new_node = Node(data)
        if self.head is None:                              # If the list is empty, make the new node the head
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:                         
                last_node = last_node.next
            last_node.next = new_node                      # Linking the last node to the new node
            new_node.prev = last_node                      # Linking the new node to the last node

    def display_forward(self):                             # Displaying the list in forward order
        if self.head is None:
            print("List is empty")
        else:
            current_node = self.head
            while current_node: 
                print(current_node.data, end=" -> ")
                current_node = current_node.next
            print("None")  

    def display_reverse(self):                             # Displaying the list in reverse order
        if self.head is None:
            print("List is empty")
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            while last_node:
                print(last_node.data, end=" -> ")
                last_node = last_node.prev
            print("None")  

def main():
    doubly_linked_list = DoublyLinkedList()                # Creating an empty doubly linked list
    n = int(input("Enter the number of elements you want to insert: "))
    for i in range(n):
        data = int(input(f"Enter element {i+1}: "))
        doubly_linked_list.insert(data)
    print("\nList in forward order:")
    doubly_linked_list.display_forward()
    print("\nList in reverse order:")
    doubly_linked_list.display_reverse()
if __name__ == "__main__":
    main()

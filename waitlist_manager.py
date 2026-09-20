# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''

    def __init__(self, name):
        self.name = name
        self.next = None
    
    
# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''

    def __init__(self):
        self.head = None

    def add_front(self, name):

        #Create new node object
        new_node = Node(name)

        #Set the new node's next attribute to the previous head
        new_node.next = self.head

        #Set the head to the new node
        self.head = new_node


    def add_end(self, name):

        #Create new node object
        new_node = Node(name)

        #Check if the list is empty
        if self.head == None:
            self.head = new_node

        #Find the end of the list
        else:
            last_node = self.head
            while last_node.next:  #Iterate through the list until final node is reached
                last_node = last_node.next

            #Set the final node's next attribute to the new node
            last_node.next = new_node


    def remove(self, name):
        #Check if the list is empty
        if self.head == None:
            print("The list is empty.")
            return

        #Check if the list only contains one node
        elif self.head.next == None:
            print(self.head.name, "removed from waitlist.")
            self.head = None
            return

        #Check if the argument is the head
        elif self.head.name == name:
            print(self.head.name, "removed from waitlist." )
            self.head = self.head.next
            return

        #Otherwise, iterate through the list until the node is located.
        else:
            #Create variables to keep track of current place in the list and the previous node accessed. Start with the head
            current_node = self.head
            previous_node = None

            #Iterate through the list and check for a match using the node's name attribute
            while current_node:
                if current_node.name == name:
                    print(current_node.name, "removed from waitlist.")

                    previous_node.next = current_node.next  #Remove the current node from the list by setting the previous node's next attribute to the current node's next attribute
                    return

                #Keep track of the previous node   
                previous_node = current_node

                #Set the current_node to the next node in the list
                current_node = current_node.next

            print("No matches found.")

    def print_list(self):

        #Check if the list is empty
        if self.head == None:
            print("The list is empty.")
            
        #Create variable to keep track of current place in the list. Start with the head
        current_node = self.head

        #Iterate through the list and print each node's name attribute
        while current_node:
            print(current_node.name)

            #Set current_node to the next node in the list
            current_node = current_node.next


def waitlist_generator():
    # Create a new linked list instance
    linked_list = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            linked_list.add_front(name.lower())
            

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            linked_list.add_end(name.lower())
            

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            linked_list.remove(name.lower())
            
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            linked_list.print_list()

            
        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()


'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:

1. How does your list work?

The list works by linking together objects, called nodes, using an attribute that specifies the next node in the list. Each node object has a value attribute and an attribute pointing to the next node in the list. Additionally, nodes in the list are not accessed using indexes. In Python, this can be done by creating a LinkedList class with a head attribute. Node objects can created using a Node class, with an attribute for a value and the next node in the list.

2. What role does the head play?

The head specifies the beginning of the linked list. It can be used as a starting point when adding new nodes or when iterating through the linked list. 

3. When might a real engineer need a custom list like this?

It is faster to insert and delete nodes from the middle of a linked list than from a Python list. Since each node in the list has memory allocated separately, adding and removing items from the list is more efficient than in a Python list. A software engineer may choose linked lists for applications such as waitlists, bookshelves, or anything where objects will be frequently added and removed from any part of the list. A bookshelf is a good example of a practical use for linked lists, since books can be added and removed from any part of the shelf. For example, a library could use an application that uses linked lists to keep track of what books are on the shelf and their position on the shelf. 

'''

#Define the node class
class node:
    def __init__(self,data=None):
        self.data = data
        """
        Last element in a linked list will always have its pointer set to none
        Update this when child node is attached
        """
        self.next=None

#Creating a linkedlist class that wraps over the nodes 
class linked_list:
    def __init__(self):
        """
        user can't interact with head node but will be placeholder
        to point to the first element in the list
        """
        self.head = node()

    #define append function to creat the first element of the list
    def append(self,data):
        new_node = node(data)
        #create variable for the node we are currently looking at
        current_node = self.head
        #iterating over list of nodes to know when to append new node once next node equals none
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    #Function to determine the length of the linked list to see how large data strcuture is
    def length(self):
        current_node = self.head
        total = 0
        while current_node.next != None:
            #total variable will contain number of elements in linked list
            total += 1
            current_node = current_node.next
        return total

    #Function to display the current contents of the list
    def display():
        elements = []
        current_node = self.head
        while current_node != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print (elements)
    
    #Extracting function to extract data from certain index
    def extract(self,index):
        if index >= self.length():
            print ("Extract Index Is Out of Range!")
            return None
        #Variable to contain current index
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index: 
                return current_node.data
            #increment current index if it doesn't equal
            current_index += 1

        #Function to erase a node at a certain index
    def erase(self,index):
        if index >= self.length():
            print ("Erase Index Is Out of Range!")
            return 
        current_index = 0
        current_node = self.head
        while True:
            #Saving last node as current node because erasing node to make sure nodes connect properly
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                #Change pointer to skip past node
                last_node.next = current_node.next
                return
            current_index += 1
        



#Creating instance of linked_list
my_list = linked_list()

#Appending numbers to test in console
my_list.append(1)
my_list.append(2)

my_list.display()

#Test extracting case
print ("element at 2nd index: %d" % my_list.extract(2))

#Test erase function
my_list.erase(1)
my_list.display()


#Code Binary Tree Data Structure

#Create a Node Class 
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        #Converting data, int or string, and storing it as a Node for the root of tree
        self.root = Node(root)

    #Print out the tree with appropriate algorithm
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    #Preorder print function
    def preorder_print(self, start, traversal):
        """Root -> Left -> Right"""
        if start != None:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    #Inorder print function
    def inorder_print(self, start, traversal):
        """Left -> Root -> Right"""
        if start != None:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    #Postorder print function
    def postorder_print(self, start, traversal):
        """ Left -> Right -> Root"""
        if start != None:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal


#Starting our tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

#Tree Traversal
#DFS (Pre, In, and Post order)

"""
Pre:
1) Check if the current Node is Empty
2) Display the data part of the root (or current node)
3) Traverse the left subtree by recursively calling the pre-order function
4) Traverse the right subtree by recursively calling the pre-order function
"""

print(tree.print_tree("preorder"))
# 1-2-4-5-3-6-7-

"""
In: (left -> Root -> right)
1) Check if the current node is empty / null
2) Traverse the left subtree by recursively calling the in-order function
3) Display the data part of the root (or current node)
4) Traverse the right subtree by recursively calling the in-order function
"""

print(tree.print_tree("inorder"))
# 4-2-5-1-6-3-7-

print(tree.print_tree("postorder"))
#4-5-2-6-7-3-1-

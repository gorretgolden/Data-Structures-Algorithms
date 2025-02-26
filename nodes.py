# 🔹 What Is a Node?
# A node is the basic building block of a tree. In a binary tree, each node contains:

# A value (or data) → The actual information stored in the node.
# A left child (or left pointer) → Points to the left node (or None if no left child).
# A right child (or right pointer) → Points to the right node (or None if no right child).

# 🔹 Example of a Node in a Binary Tree
    #     10
    #    /  \
    #   5    15
    #  / \     \
    # 2   7     20

# Here, each circle is a node:

# The root node is 10.
# 10 has a left child 5 and a right child 15.
# 5 has children 2 and 7.
# 15 has only a right child 20.


# 🔹 How Do We Create a Node in Python?
# A node in Python is just a class with three attributes:
class Node:
  def __init__(self,value):
    self.value = value
    self.left  = None
    self.right = None
# self.value: Holds the data (e.g., 10, 5, 15).
# self.left: Holds the left child (another node or None).
# self.right: Holds the right child (another node or None).
#Creating a node
node1= Node(12)
print(node1.value)
print(node1.left)
print(node1.right)


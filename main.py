from tree import Tree
from node import Node

# Start the program

tree = Tree()

while True:
    try:
        value = input("Enter a value to add to the tree (or 't' to end): ")
        if value.lower() == 't':
            break
        value = int(value)
        tree.add(value)
    except ValueError:
        print("Invalid input! Please enter an integer value or 't' to end.")

tree.printTree()

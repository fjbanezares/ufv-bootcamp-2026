print("\nExample 6: Sentinel Value")

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

# Creating a simple linked list where 'None' is used to indicate the end of the list.
node1 = Node(1)  # The last node in the list; next_node is None by default
node2 = Node(2, node1)  # This node points to node1
node3 = Node(3, node2)  # This node points to node2, making node3 the head of the list

# Traversing the linked list until we reach 'None'
current_node = node3
while current_node is not None:  # None acts as a sentinel value to terminate the loop
    print(f"Node data: {current_node.data}")
    current_node = current_node.next_node

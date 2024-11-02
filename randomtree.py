from random import randint
from matplotlib import pyplot as plt

class Node:
    def __init__(self, label=None, parent=None):
        self.parent = parent
        self.label=label
        self.children = set()
        self.degree = 0
        
        if parent != None: 
            self.degree += 1
    
    def append(self, child):
        self.children.add(child)
        child.parent = self
        child.degree += 1
        self.degree += 1
        
        return self.degree
    
    def remove_child(self, child):
        try:
            self.children.remove(child)
            self.degree -= 1
            return self.degree
        except KeyError:
            return -1
    
    def remove_self(self):
        if self.parent != None:
            self.parent.remove_child(self)
    
    def get_child(self, index=0):
        if len(self.children) == 0:
            return self
        
        return list(self.children)[index % len(self.children)]
    
    def get_subtree_nodes(self):
        tree = [self]
        for child in self.children:
            tree += child.get_subtree_nodes()
        
        return tree
    
    def render_depth_labled_tree(self):
        yield
        #TODO
    
    def deep_copy(self):
        if len(self.children) == 0:
            return Node(self.label)
        
        new_copy = Node(self.label)
        
        for child in self.children:
            new_copy.append(child.deep_copy())
        
        return new_copy
    
    def __str__(self, depth = 0):
        print('    ' * depth, end='')
        print('- label: ', self.label, ' degree: ', self.degree)
        for child in self.children:
            child.__str__(depth + 1)
        return ''

def split_nodes(node: Node, n=2, root=None): 
    new_label = node.label + 1
    
    if root == None:
        root = node
    
    if len(node.children) == 0:
        for _ in range(n):
            node.append(Node(new_label, node))
    else:
        for child in node.children:
            split_nodes(child, n, root)
            
    return root

def generate_random_tree(order):
    root = Node(0)
    tree_nodes = [root]
    
    for i in range(order - 1):
        new_parent = randint(0, len(tree_nodes) - 1)
        new_child = Node(tree_nodes[new_parent].label + 1)
        tree_nodes[new_parent].append(new_child)
        tree_nodes += [new_child]
    
    return root


# top_node = Node(label=0)
# split_nodes(split_nodes(split_nodes(top_node, 2), 3), 5)
# top_node.get_child().get_child().append(Node(label="UwU"))
# top_node.get_child().append(Node(label="UwU"))
# print(top_node)

# print([vert.degree for vert in top_node.get_subtree_nodes()])

new_tree = generate_random_tree(50)
copy_tree = new_tree.deep_copy()
# copy_tree.get_child().get_child().remove_self()
print(new_tree)
print(copy_tree)


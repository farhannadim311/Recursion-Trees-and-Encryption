# Problem Set 4A
# Name:
# Collaborators:

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))) , Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    # TODO: Remove pass and write your code here
    if(tree == None):
        return 0
    if(tree.get_left_child() == None and tree.get_right_child() == None):
        return 0
    else:
        left_length = 1 + find_tree_height(tree.get_left_child())
        right_length = 1 + find_tree_height(tree.get_right_child())
        return max(left_length, right_length)

def is_heap(tree, compare_func):
    """
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    """
    # TODO: Remove pass and write your code here
    cond1 = True
    cond2 = True
    if(tree == None):
        return True
    if(tree.get_left_child() == None and tree.get_right_child() == None):
        return True
    else:
        if(tree.get_left_child()):
            cond1 = compare_func(tree.get_left_child().get_value(), tree.get_value())
        if(tree.get_right_child()):
            cond2 = compare_func(tree.get_right_child().get_value(),tree.get_value())
        cond3 = is_heap(tree.get_left_child(), compare_func)
        cond4 = is_heap(tree.get_right_child(), compare_func)        
        if(cond1 and cond2 and cond3 and cond4):
            return True
        else:
            return False
    


if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    tr2 = Node(2,Node(3,Node(4),Node(5,Node(6))),Node(7,None,Node(8,Node(9),Node(1))))
    print(tr2)
    compare_func = lambda x,y: x > y
    print(is_heap(tr2, compare_func))
    
          
    

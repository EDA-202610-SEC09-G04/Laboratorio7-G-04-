def put(my_bst, key, value):
    """
    Inserta un nodo en el BST. Si la llave ya existe, actualiza el valor.
    """
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst
from DataStructures.Tree import bst_node as node


def insert_node(root, key, value):
    """
    Inserta recursivamente un nodo en el BST.
    """

  
    if root is None:
        return node.new_node(key, value)

  
    root_key = node.get_key(root)

   
    if key < root_key:
        root["left"] = insert_node(root["left"], key, value)

  
    elif key > root_key:
        root["right"] = insert_node(root["right"], key, value)

   
    else:
        root["value"] = value


    left_size = root["left"]["size"] if root["left"] else 0
    right_size = root["right"]["size"] if root["right"] else 0
    root["size"] = 1 + left_size + right_size

    return root
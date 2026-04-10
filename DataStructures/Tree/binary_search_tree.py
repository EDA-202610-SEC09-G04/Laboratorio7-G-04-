from DataStructures.Tree import bst_node as node

def put(my_bst, key, value):
    cmp_function = my_bst["cmp_function"]
    my_bst["root"] = insert_node(my_bst["root"], key, value, cmp_function)
    return my_bst

def insert_node(root, key, value, cmp_function):
    if root is None:
        return node.new_node(key, value)
    root_key = node.get_key(root)
    cmp = cmp_function(key, root_key)
    if cmp < 0:
        root["left"] = insert_node(root["left"], key, value, cmp_function)
    elif cmp > 0:
        root["right"] = insert_node(root["right"], key, value, cmp_function)
    else:
        root["value"] = value
    left_size = root["left"]["size"] if root["left"] is not None else 0
    right_size = root["right"]["size"] if root["right"] is not None else 0
    root["size"] = 1 + left_size + right_size
    return root

def get(my_bst, key):
    return get_node(my_bst["root"], key, my_bst["cmp_function"])


def get_node(root, key, cmp_function):
    if root is None:
        return None
    root_key = node.get_key(root)
    cmp = cmp_function(key, root_key)
    if cmp == 0:
        return node.get_value(root)
    elif cmp < 0:
        return get_node(root["left"], key, cmp_function)
    else:
        return get_node(root["right"], key, cmp_function)

def size(my_bst):
    return size_tree(my_bst["root"])

def size_tree(root):
    if root is None:
        return 0
    return 1 + size_tree(root["left"]) + size_tree(root["right"])
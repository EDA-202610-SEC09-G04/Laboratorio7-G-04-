from DataStructures.Tree import bst_node as node
from DataStructures.List import single_linked_list as lt

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
    result = get_node(my_bst["root"], key, my_bst["cmp_function"])
    if result is None:
        return None
    else:
        return node.get_value(result)

    
def get_node(root, key, cmp_function):
    if root is None:
        return None
    root_key = node.get_key(root)
    cmp = cmp_function(key, root_key)
    if cmp == 0:
        return root  
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

def default_compare(key1, key2):
    if key1 < key2:
        return -1
    elif key1 > key2:
        return 1
    else:
        return 0


def new_map():
    bst = {
        "root": None,
        "cmp_function": default_compare
    }
    return bst

def contains(my_bst, key):
    return get(my_bst, key) is not None


def is_empty(my_bst):
    return my_bst["root"] is None


def get_min(my_bst):
    if my_bst["root"] is None:
        return None
    return get_min_node(my_bst["root"])


def get_min_node(root):
    if root["left"] is None:
        return root["key"]
    return get_min_node(root["left"])


def get_max(my_bst):
    if my_bst["root"] is None:
        return None
    return get_max_node(my_bst["root"])


def get_max_node(root):
    if root["right"] is None:
        return root["key"]
    return get_max_node(root["right"])


def height(my_bst):
    return height_tree(my_bst["root"])


def height_tree(root):
    if root is None:
        return 0
    return 1 + max(height_tree(root["left"]), height_tree(root["right"]))


def key_set(my_bst):
    lst = lt.new_list()
    key_set_tree(my_bst["root"], lst)
    return lst


def key_set_tree(root, lst):
    if root is None:
        return
    key_set_tree(root["left"], lst)
    lt.add_last(lst, root["key"])
    key_set_tree(root["right"], lst)


def value_set(my_bst):
    lst = lt.new_list()
    value_set_tree(my_bst["root"], lst)
    return lst


def value_set_tree(root, lst):
    if root is None:
        return
    value_set_tree(root["left"], lst)
    lt.add_last(lst, root["value"])
    value_set_tree(root["right"], lst)


def keys(my_bst, low, high):
    lst = lt.new_list()
    keys_range(my_bst["root"], low, high, lst, my_bst["cmp_function"])
    return lst


def keys_range(root, low, high, lst, cmp_function):
    if root is None:
        return

    cmp_low = cmp_function(low, root["key"])
    cmp_high = cmp_function(high, root["key"])

    if cmp_low < 0:
        keys_range(root["left"], low, high, lst, cmp_function)

    if cmp_low <= 0 and cmp_high >= 0:
        lt.add_last(lst, root["key"])

    if cmp_high > 0:
        keys_range(root["right"], low, high, lst, cmp_function)


def values(my_bst, low, high):
    lst = lt.new_list()
    values_range(my_bst["root"], low, high, lst, my_bst["cmp_function"])
    return lst


def values_range(root, low, high, lst, cmp_function):
    if root is None:
        return

    cmp_low = cmp_function(low, root["key"])
    cmp_high = cmp_function(high, root["key"])

    if cmp_low < 0:
        values_range(root["left"], low, high, lst, cmp_function)

    if cmp_low <= 0 and cmp_high >= 0:
        lt.add_last(lst, root["value"])

    if cmp_high > 0:
        values_range(root["right"], low, high, lst, cmp_function)
        
def delete_min(my_bst):
    if my_bst["root"] is not None:
        my_bst["root"] = delete_min_tree(my_bst["root"])
    return my_bst


def delete_min_tree(root):
    if root["left"] is None:
        return root["right"]

    root["left"] = delete_min_tree(root["left"])

    left_size = root["left"]["size"] if root["left"] else 0
    right_size = root["right"]["size"] if root["right"] else 0
    root["size"] = 1 + left_size + right_size

    return root


def delete_max(my_bst):
    if my_bst["root"] is not None:
        my_bst["root"] = delete_max_tree(my_bst["root"])
    return my_bst


def delete_max_tree(root):
    if root["right"] is None:
        return root["left"]

    root["right"] = delete_max_tree(root["right"])

    left_size = root["left"]["size"] if root["left"] else 0
    right_size = root["right"]["size"] if root["right"] else 0
    root["size"] = 1 + left_size + right_size

    return root
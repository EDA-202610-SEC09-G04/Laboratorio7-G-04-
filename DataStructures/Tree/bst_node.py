def new_node(key, value):
    node = {
        "key": key,
        "value": value,
        "size": 1,
        "left": None,
        "right": None,
        "type": "BST",
    }
    return node


def get_value(my_node):
    value = None
    if my_node is not None:
        value = my_node["value"]
    return value


def get_key(my_node):
    key = None
    if my_node is not None:
        key = my_node["key"]
    return key

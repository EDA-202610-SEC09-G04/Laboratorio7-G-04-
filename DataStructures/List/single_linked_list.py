from DataStructures.List import list_node as ln

def new_list():
    return {"size": 0, "first": None, "last": None}

def is_empty(my_list):
    return my_list["size"] == 0

def size(my_list):
    return my_list["size"]

def add_first(my_list, element):
    node = ln.new_single_node(element) 
    node["next"] = my_list["first"]
    my_list["first"] = node
    if my_list["size"] == 0:
        my_list["last"] = node
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    node = ln.new_single_node(element)  
    if my_list["size"] == 0:
        my_list["first"] = node
        my_list["last"] = node
    else:
        my_list["last"]["next"] = node
        my_list["last"] = node

    my_list["size"] += 1
    return my_list

def first_element(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    return my_list["first"]["info"]

def last_element(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    return my_list["last"]["info"]

def get_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception("IndexError: list index out of range")

    node = my_list["first"]
    i = 0
    while i < pos:
        node = node["next"]
        i += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    temp = my_list["first"]
    pos = 0
    while temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            return pos
        temp = temp["next"]
        pos += 1
    return -1

def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception("IndexError: list index out of range")
    if pos == 0:
        my_list["first"] = my_list["first"]["next"]
        my_list["size"] -= 1
        if my_list["size"] == 0:
            my_list["last"] = None
        return my_list
    prev = my_list["first"]
    i = 0
    while i < pos - 1:
        prev = prev["next"]
        i += 1
    target = prev["next"]
    prev["next"] = target["next"]
    if target == my_list["last"]:
        my_list["last"] = prev

    my_list["size"] -= 1
    return my_list

def remove_first(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    removed = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= 1
    if my_list["size"] == 0:
        my_list["last"] = None
    return removed

def remove_last(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    removed = my_list["last"]["info"]
    if my_list["size"] == 1:
        my_list["first"] = None
        my_list["last"] = None
        my_list["size"] = 0
        return removed
    prev = my_list["first"]
    while prev["next"] != my_list["last"]:
        prev = prev["next"]
    prev["next"] = None
    my_list["last"] = prev
    my_list["size"] -= 1
    return removed

def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list):
        raise Exception("IndexError: list index out of range")
    if pos == 0:
        return add_first(my_list, element)
    if pos == size(my_list):
        return add_last(my_list, element)
    new_node = ln.new_single_node(element) 
    prev = my_list["first"]
    i = 0
    while i < pos - 1:
        prev = prev["next"]
        i += 1
    new_node["next"] = prev["next"]
    prev["next"] = new_node
    my_list["size"] += 1
    return my_list

def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= size(my_list):
        raise Exception("IndexError: list index out of range")
    node = my_list["first"]
    i = 0
    while i < pos:
        node = node["next"]
        i += 1
    node["info"] = new_info
    return my_list

def exchange(my_list, pos_1, pos_2):
    if pos_1 < 0 or pos_1 >= size(my_list) or pos_2 < 0 or pos_2 >= size(my_list):
        raise Exception("IndexError: list index out of range")
    if pos_1 == pos_2:
        return my_list
    n1 = my_list["first"]
    i = 0
    while i < pos_1:
        n1 = n1["next"]
        i += 1
    n2 = my_list["first"]
    j = 0
    while j < pos_2:
        n2 = n2["next"]
        j += 1
    n1["info"], n2["info"] = n2["info"], n1["info"]
    return my_list

def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= size(my_list):
        raise Exception("IndexError: list index out of range")
    sub = new_list()
    count = 0
    idx = pos
    while count < num_elements and idx < size(my_list):
        add_last(sub, get_element(my_list, idx))
        idx += 1
        count += 1
    return sub




"""
FUNCIONES DE ORDENAMIENTOS
"""

def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list, sort_crit=default_sort_criteria):
    if my_list["size"] <= 1:
        return my_list
    start = my_list["first"]
    while start is not None:
        min_node = start
        current = start["next"]
        while current is not None:
            if sort_crit(current["info"], min_node["info"]):
                min_node = current
            current = current["next"]
        start["info"], min_node["info"] = min_node["info"], start["info"]
        start = start["next"]
    return my_list

def insertion_sort(my_list, sort_crit=default_sort_criteria):
    if my_list["size"] <= 1:
        return my_list

    sorted_list = new_list()
    current = my_list["first"]
    while current is not None:
        element = current["info"]
        if is_empty(sorted_list):
            add_first(sorted_list, element)
        else:
            node = sorted_list["first"]
            pos = 0
            while node is not None and not sort_crit(element, node["info"]):
                node = node["next"]
                pos += 1
            insert_element(sorted_list, element, pos)
        current = current["next"]
    my_list["first"] = sorted_list["first"]
    my_list["last"] = sorted_list["last"]
    my_list["size"] = sorted_list["size"]
    return my_list

def shell_sort(my_list, sort_crit=default_sort_criteria):
    n = size(my_list)
    gap = n // 2
    while gap > 0:
        i = gap
        while i < n:
            temp = get_element(my_list, i)
            j = i
            while j >= gap and sort_crit(temp, get_element(my_list, j-gap)):
                change_info(my_list, j, get_element(my_list, j-gap))
                j -= gap
            change_info(my_list, j, temp)
            i += 1
        gap //= 2
    return my_list

def merge_sort(my_list, sort_crit=default_sort_criteria):
    if size(my_list) <= 1:
        return my_list

    mid = size(my_list) // 2
    left = new_list()
    right = new_list()
    current = my_list["first"]
    count = 0
    while current is not None:
        if count < mid:
            add_last(left, current["info"])
        else:
            add_last(right, current["info"])
        current = current["next"]
        count += 1
    left = merge_sort(left, sort_crit)
    right = merge_sort(right, sort_crit)
    return merge(left, right, sort_crit)

def merge(left, right, sort_crit=default_sort_criteria):
    result = new_list()
    node_l = left["first"]
    node_r = right["first"]
    while node_l is not None and node_r is not None:
        if sort_crit(node_l["info"], node_r["info"]):
            add_last(result, node_l["info"])
            node_l = node_l["next"]
        else:
            add_last(result, node_r["info"])
            node_r = node_r["next"]
    while node_l is not None:
        add_last(result, node_l["info"])
        node_l = node_l["next"]
    while node_r is not None:
        add_last(result, node_r["info"])
        node_r = node_r["next"]
    return result

def quick_sort(my_list, sort_crit=default_sort_criteria):
    if size(my_list) <= 1:
        return my_list

    pivot = first_element(my_list)
    less = new_list()
    greater = new_list()
    equal = new_list()
    add_last(equal, pivot)
    node = my_list["first"]["next"]   
    while node is not None:
        elem = node["info"]
        if sort_crit(elem, pivot):
            add_last(less, elem)
        elif sort_crit(pivot, elem):
            add_last(greater, elem)
        else:
            add_last(equal, elem)
        node = node["next"]
    less = quick_sort(less, sort_crit)
    greater = quick_sort(greater, sort_crit)
    sorted_list = concatenate(less, equal, greater)
    my_list["first"] = sorted_list["first"]
    my_list["last"] = sorted_list["last"]
    my_list["size"] = sorted_list["size"]
    return my_list

def concatenate(a, b, c):
    result = new_list()
    node = a["first"]
    while node is not None:
        add_last(result, node["info"])
        node = node["next"]
    node = b["first"]
    while node is not None:
        add_last(result, node["info"])
        node = node["next"]
    node = c["first"]
    while node is not None:
        add_last(result, node["info"])
        node = node["next"]
    return result
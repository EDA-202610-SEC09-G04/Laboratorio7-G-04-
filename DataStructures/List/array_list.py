def new_list():
    newlist = {
    'elements': [],
    'size': 0,
    }
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def size(my_list):
    return my_list["size"]

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def first_element(my_list):
    return my_list["elements"][0]

def is_empty(my_list):
    return my_list["size"] == 0

def last_element(my_list):
    return my_list["elements"][-1]

def delete_element(my_list, pos):
    del my_list["elements"][pos]
    my_list["size"] -= 1
    return my_list

def remove_first(my_list):
    removed = my_list["elements"][0]
    my_list["elements"].pop(0)
    my_list["size"] -= 1
    return removed

def remove_last(my_list):
    removed = my_list["elements"][-1]
    my_list["elements"].pop()
    my_list["size"] -= 1
    return removed

def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list["size"]:
        raise IndexError("list index out of range")
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list

def change_info(my_list, pos, new_info):
    _ = my_list["elements"][pos]
    my_list["elements"][pos] = new_info
    return my_list


def exchange(my_list, pos_1, pos_2):
    _ = my_list["elements"][pos_1]
    _ = my_list["elements"][pos_2]
    my_list["elements"][pos_1], my_list["elements"][pos_2] = my_list["elements"][pos_2], my_list["elements"][pos_1]
    return my_list

def sub_list(my_list, pos_i, num_elements):
    _ = my_list["elements"][pos_i]
    sub_elems = my_list["elements"][pos_i: pos_i + num_elements]
    return {"size": len(sub_elems), "elements": sub_elems}

# Laboratorio 5

def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list, sort_criteria=default_sort_criteria):
    size = my_list["size"]
    elements = my_list["elements"]
    for i in range(size - 1):
        min_index = i
        for j in range(i + 1, size):
            if sort_criteria(elements[j], elements[min_index]):
                min_index = j
        if min_index != i:
            elements[i], elements[min_index] = elements[min_index], elements[i]
    return my_list

def insertion_sort(my_list, sort_criteria=default_sort_criteria):
    elements = my_list["elements"]
    size = my_list["size"]
    for i in range(1, size):
        current = elements[i]
        j = i - 1
        while j >= 0 and sort_criteria(current, elements[j]):
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = current
    return my_list

def shell_sort(my_list, sort_criteria=default_sort_criteria):
    elements = my_list["elements"]
    size = my_list["size"]
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            temp = elements[i]
            j = i
            while j >= gap and sort_criteria(temp, elements[j - gap]):
                elements[j] = elements[j - gap]
                j -= gap
            elements[j] = temp
        gap //= 2
    return my_list

def quick_sort(my_list, sort_criteria=default_sort_criteria):
    elements = my_list["elements"]
    
    def partition(low, high):
        pivot = elements[high]
        i = low - 1
        for j in range(low, high):
            if sort_criteria(elements[j], pivot):
                i += 1
                elements[i], elements[j] = elements[j], elements[i]
        elements[i + 1], elements[high] = elements[high], elements[i + 1]
        return i + 1

    def quick(low, high):
        if low < high:
            pi = partition(low, high)
            quick(low, pi - 1)
            quick(pi + 1, high)
    if my_list["size"] > 1:
        quick(0, my_list["size"] - 1)
    return my_list

def merge_sort(my_list, sort_criteria=default_sort_criteria):
    if my_list["size"] <= 1:
        return my_list
    elements = my_list["elements"]
    mid = my_list["size"] // 2
    left = {
        "elements": elements[:mid],
        "size": mid
    }
    right = {
        "elements": elements[mid:],
        "size": my_list["size"] - mid
    }
    merge_sort(left, sort_criteria)
    merge_sort(right, sort_criteria)
    i = 0
    j = 0
    k = 0
    while i < left["size"] and j < right["size"]:
        if sort_criteria(left["elements"][i], right["elements"][j]):
            elements[k] = left["elements"][i]
            i += 1
        else:
            elements[k] = right["elements"][j]
            j += 1
        k += 1
    while i < left["size"]:
        elements[k] = left["elements"][i]
        i += 1
        k += 1
    while j < right["size"]:
        elements[k] = right["elements"][j]
        j += 1
        k += 1
    return my_list
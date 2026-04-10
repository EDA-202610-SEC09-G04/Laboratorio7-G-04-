from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl

import random as r

def new_map(num_elements, load_factor, prime=109345121):

    capacidad = mf.next_prime(int(num_elements / load_factor))

    scale = r.randint(1, prime - 1)
    shift = r.randint(0, prime - 1)

    table = al.new_list()

    for i in range(capacidad):
        lista = sl.new_list()  
        al.add_last(table, lista)

    nuevo_mapa = {
        "prime": prime,
        "capacity": capacidad,
        "scale": scale,
        "shift": shift,
        "table": table,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0
    }

    return nuevo_mapa

def rehash(my_map):

    old_table = my_map["table"]
    old_capacity = my_map["capacity"]
    new_capacity = mf.next_prime(old_capacity * 2)
    my_map["capacity"] = new_capacity

    new_table = al.new_list()
    for i in range(new_capacity):
        bucket = sl.new_list()
        al.add_last(new_table, bucket)

    my_map["table"] = new_table
    my_map["size"] = 0

    for i in range(al.size(old_table)):

        bucket = al.get_element(old_table, i)
        current = bucket["first"]

        while current is not None:
            entry = current["info"]
            key = me.get_key(entry)
            value = me.get_value(entry)

            put(my_map, key, value)

            current = current["next"]

    return my_map

def put(my_map, key, value):

    table = my_map["table"]
    index = mf.hash_value(my_map, key)
    bucket = al.get_element(table, index)

    encontrado = False
    current = bucket["first"]

    while current is not None:
        entry = current["info"]

        if me.get_key(entry) == key:
            me.set_value(entry, value)
            encontrado = True
            break

        current = current["next"]

    if not encontrado:
        entry = me.new_map_entry(key, value)
        sl.add_last(bucket, entry)

        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

        if my_map["current_factor"] > my_map["limit_factor"]:
            my_map = rehash(my_map)

    return my_map

def contains(my_map, key):

    pos = mf.hash_value(my_map, key)
    bucket = al.get_element(my_map["table"], pos)

    current = bucket["first"]

    while current is not None:
        entry = current["info"]

        if me.get_key(entry) == key:
            return True

        current = current["next"]

    return False

def get(my_map, key):

    pos = mf.hash_value(my_map, key)
    bucket = al.get_element(my_map["table"], pos)

    current = bucket["first"]

    while current is not None:
        entry = current["info"]

        if me.get_key(entry) == key:
            return me.get_value(entry)

        current = current["next"]

    return None



def size(my_map):
    
    return my_map['size']

def is_empty(my_map):
    
    if size(my_map) == 0:
       return True
    return False

def remove(my_map, key):

    pos = mf.hash_value(my_map, key)

    bucket = al.get_element(my_map["table"], pos)

    prev = None
    current = bucket["first"]

    while current is not None:

        entry = current["info"]

        if me.get_key(entry) == key:

           
            if prev is None:
                bucket["first"] = current["next"]
            else:
                prev["next"] = current["next"]

           
            if current == bucket["last"]:
                bucket["last"] = prev

            bucket["size"] -= 1

            my_map["size"] -= 1
            my_map["current_factor"] = my_map["size"] / my_map["capacity"]

            return my_map

        prev = current
        current = current["next"]

    return my_map

def key_set(my_map):

    table = my_map["table"]
    keys = al.new_list()

    for i in range(al.size(table)):

        bucket = al.get_element(table, i)
        current = bucket["first"]

        while current is not None:
            entry = current["info"]
            key = me.get_key(entry)

            al.add_last(keys, key)

            current = current["next"]

    return keys

def value_set(my_map):
    
    table = my_map["table"]
    values = al.new_list()

    for i in range(al.size(table)):

        bucket = al.get_element(table, i)
        current = bucket["first"]

        while current is not None:
            entry = current["info"]
            value = me.get_value(entry)

            al.add_last(values, value)

            current = current["next"]

    return values
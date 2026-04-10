from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as al
import random as r

def new_map(num_elements, load_factor, prime=109345121):

    capacidad = mf.next_prime(int(num_elements / load_factor))

    scale = r.randint(1, prime - 1)
    shift = r.randint(0, prime - 1)

    table = al.new_list()

    for i in range(capacidad):
        al.add_last(table, me.new_map_entry(None, None))

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
 
def put(my_map, key, value):

    table = my_map["table"]

    hash_value = mf.hash_value(my_map, key)

    found, slot = find_slot(my_map, key, hash_value)

    entry = me.new_map_entry(key, value)

    if found:
        al.change_info(table, slot, entry)

    else:
        al.change_info(table, slot, entry)

        my_map["size"] += 1

        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

        if my_map["current_factor"] > my_map["limit_factor"]:
            my_map = rehash(my_map)

    return my_map
 
def rehash(my_map):

    old_table = my_map["table"]
    old_capacity = my_map["capacity"]

    new_capacity = old_capacity * 2
    my_map["capacity"] = new_capacity

    new_table = al.new_list()

    for i in range(new_capacity):
        al.add_last(new_table, me.new_map_entry(None, None))

    my_map["table"] = new_table
    my_map["size"] = 0

    for i in range(al.size(old_table)):

        entry = al.get_element(old_table, i)

        key = me.get_key(entry)

        if key is not None and key != "__EMPTY__":
            value = me.get_value(entry)
            put(my_map, key, value)

    return my_map
 
def is_available(table, pos):

   entry = al.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def find_slot(my_map, key, hash_value):
   
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = al.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
      
   return ocupied, first_avail

def contains(my_map, key):

    pos = mf.hash_value(my_map, key)

    found, slot = find_slot(my_map, key, pos)

    return found

def get(my_map, key):

    pos = mf.hash_value(my_map, key)

    found, slot = find_slot(my_map, key, pos)

    if found:
        entry = al.get_element(my_map["table"], slot)
        return me.get_value(entry)

    return None
 
def remove(my_map, key):

    pos = mf.hash_value(my_map, key)

    found, slot = find_slot(my_map, key, pos)

    if found:

        table = my_map["table"]

        entry = al.get_element(table, slot)

        me.set_key(entry, "__EMPTY__")
        me.set_value(entry, None)

        my_map["size"] -= 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

    return my_map
    

def size(my_map):
    
    return my_map['size']
 
def is_empty(my_map):
    
    if size(my_map) == 0:
       return True
    return False
 
def key_set(my_map):

    table = my_map["table"]

    keys = al.new_list()

    for i in range(al.size(table)):

        entry = al.get_element(table, i)

        key = me.get_key(entry)

        if key is not None and key != "__EMPTY__":
            al.add_last(keys, key)

    return keys
 
def value_set(my_map):
    
    table = my_map["table"]

    values = al.new_list()

    for i in range(al.size(table)):

        entry = al.get_element(table, i)

        value = me.get_value(entry)

        if value is not None and value != "__EMPTY__":
            al.add_last(values, value)

    return values
    
   
   


"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones
 *
 * Dario Correal
 """

import os
import csv
import datetime
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Tree import binary_search_tree as bst
from DataStructures.List import array_list as al
from DataStructures.Map import map_separate_chaining as sp

# TODO Realice la importación del Árbol Binario Ordenado
# TODO Realice la importación de ArrayList (al) como estructura de datos auxiliar para sus requerimientos
# TODO Realice la importación de LinearProbing (lp) como estructura de datos auxiliar para sus requerimientos

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def new_logic():
    analyzer = {'crimes': None,
                'dateIndex': None
                }
    analyzer['crimes'] = al.new_list()
    analyzer['dateIndex'] = bst.new_map()
    return analyzer

# Funciones para realizar la carga

def load_data(analyzer, crimesfile):
    crimesfile = data_dir + crimesfile
    input_file = csv.DictReader(open(crimesfile, encoding="utf-8"), delimiter=",")
    for crime in input_file:
        add_crime(analyzer, crime)
    return analyzer

# Funciones para agregar informacion al analizador

def add_crime(analyzer, crime):
    al.add_last(analyzer['crimes'], crime)
    update_date_index(analyzer['dateIndex'], crime)
    return analyzer

def update_date_index(map, crime):
    occurreddate = crime['OCCURRED_ON_DATE']
    crimedate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    entry = bst.get(map, crimedate.date())
    if entry is None:
        datentry = new_data_entry(crime)
        bst.put(map, crimedate.date(), datentry)
    else:
        datentry = entry
    add_date_index(datentry, crime)
    return map

def add_date_index(datentry, crime):
    lst = datentry['lstcrimes']
    al.add_last(lst, crime)
    offenseIndex = datentry['offenseIndex']
    offentry = lp.get(offenseIndex, crime['OFFENSE_CODE_GROUP'])
    if offentry is None:
        new_entry = new_offense_entry(crime['OFFENSE_CODE_GROUP'], crime)
        al.add_last(new_entry['lstoffenses'], crime)
        lp.put(offenseIndex, crime['OFFENSE_CODE_GROUP'], new_entry)
    else:
        al.add_last(offentry['lstoffenses'], crime)
    return datentry

def new_data_entry(crime):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'offenseIndex': None, 'lstcrimes': None}
    entry['offenseIndex'] = lp.new_map(num_elements=30,
                                        load_factor=0.5)
    entry['lstcrimes'] = al.new_list()
    return entry

def new_offense_entry(offensegrp, crime):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {'offense': None, 'lstoffenses': None}
    ofentry['offense'] = offensegrp
    ofentry['lstoffenses'] = al.new_list()
    return ofentry

def get_crimes_by_range_code(analyzer, initialDate, offensecode):
    initialDate = datetime.datetime.strptime(initialDate, "%Y-%m-%d").date()
    entry = bst.get(analyzer['dateIndex'], initialDate)
    if entry is None:
        return 0
    offentry = lp.get(entry['offenseIndex'], offensecode)
    if offentry is None:
        return 0
    return al.size(offentry['lstoffenses'])

# ==============================
# Funciones de consulta
# ==============================

def crimes_size(analyzer):
    """
    Número de crimenes
    """
    return al.size(analyzer['crimes'])

def index_height(analyzer):
    """
    Altura del arbol
    """
    return bst.height(analyzer['dateIndex'])-1

def index_size(analyzer):
    """
    Numero de elementos en el indice
    """
    return bst.size(analyzer['dateIndex'])

def min_key(analyzer):
    """
    Llave mas pequena
    """
    return bst.get_min(analyzer['dateIndex'])

def max_key(analyzer):
    """
    Llave mas grande
    """
    return bst.get_max(analyzer['dateIndex'])

def get_crimes_by_range(analyzer, initialDate, finalDate):
    """
    Retorna el numero de crimenes en un rago de fechas.
    """
    initialDate = datetime.datetime.strptime(initialDate, "%Y-%m-%d").date()
    finalDate = datetime.datetime.strptime(finalDate, "%Y-%m-%d").date()
    keys = bst.keys(analyzer['dateIndex'], initialDate, finalDate)
    total = 0
    node = keys["first"]
    while node is not None:
        key = node["info"]
        entry = bst.get(analyzer['dateIndex'], key)
        total += al.size(entry['lstcrimes'])
        node = node["next"]
    return total
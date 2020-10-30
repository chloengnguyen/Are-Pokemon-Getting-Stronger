import pprint
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import json
import time
import requests


url = 'https://pokemondb.net/pokedex/all'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

def get_headers(soup):
    '''
    Get the headers from the table 
    '''
    header = soup.find_all("th",{"class":"sorting"})
    cols = []
    for i in range(len(header)):
        cols.append(header[i].text)

def get_name(soup):
    names = soup.find_all("td",{"class":"cell-name"})
    pokemon_names = []
    for i in range(len(names)):
        pokemon_names.append(names[i].text)
    return pokemon_names

def get_total(soup):
    '''
    Get the total stat  
    '''
    base = soup.find_all("td",class_ = "cell-total"})
    base_total = []
    for i in range(len(base)):
        base_total.append(base[i].text)
    return base_total 

def get_type(soup):
    '''
    Get pokemon type
    '''
    types = soup.find_all('td',class_ = "cell-icon")
    pokemon_types = []
    for x in types:
        pokemon_types.append(x.text)
    return pokemon_types

def multiple_stats(soup):
    '''
    Individual stats are stored in nested list. 
    A function which stores all the numerical stats in a single list.  
    '''
    nums = soup.find_all('td',attrs ={'class':'cell-num'})
    stats = []
    for i in nums:
        stats.append(i.text)
    return stats

def get_individual_stat(stats,):
    '''
    Extract individual stats from multiple_stats
    ++++++++++++
    Parameters: 
    ++++++++++++
    Return list of a specific stat 

    '''
    pokemon_num = []
    pokemon_hp = []
    pokemon_att = []
    pokemon_def = []
    pokemon_spatt = []
    pokemon_spdef = []
    pokemon_speed = []
    # National index  
    for i in range(0, len(stats), 7):
        pokemon_num.append(stats[i])
    # HP
    for i in range(1, len(stats), 7):
        pokemon_hp.append(stats[i])
    # Attack 
    for i in range(2, len(stats), 7):
        pokemon_att.append(stats[i])
    # Defense
    for i in range(3, len(stats), 7):
        pokemon_def.append(stats[i])
    # Sp. Att 
    for i in range(4, len(stats), 7):
        pokemon_spatt.append(stats[i])
    # Sp. Def 
    for i in range(5, len(stats), 7):
        pokemon_spdef.append(stats[i])   
    # Speed
    for i in range(6, len(stats), 7):
        pokemon_speed.append(stats[i])
    return pokemon_num, pokemon_hp, pokemon_att, pokemon_def, pokemon_spatt,pokemon_spdef,pokemon_speed
# Unpack 
pokemon_num, pokemon_hp, pokemon_att, pokemon_def, pokemon_spatt,pokemon_spdef,pokemon_speed = get_individual_stat(stats = multiple_stats(soup))


def convert_int(poke_stat):
    '''
    Convert all elements in a specific stat list into an integer
    ++++++
    Parameter: any stat (pokemon_num, pokemon_total, pokemon_hp, pokemon_speed etc.)
    '''
    result = [int(i) if i != '' else "NaN" for i in poke_stat]
    return result

# Constructing a dataframe from data collected from web scraping 
pokemon_data = {
    "ID" : pokemon_num,
    "NAME": pokemon_names, 
    "TYPE": pokemon_types,
    "BASE STAT": pokemon_total, 
    "HP" : pokemon_hp,
    "ATTACK" : pokemon_att,
    "DEFENSE" : pokemon_def,
    "SP ATTACK": pokemon_spatt,
    "SP DEFENSE": pokemon_spdef,
    "SPEED": pokemon_speed
}


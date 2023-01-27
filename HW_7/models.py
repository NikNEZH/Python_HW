import numpy as np
import re

def get_data_tel_spravki(files):
    with open(str(files),"r", encoding="utf-8") as file:
        data = file.read()
        list_of_words = re.sub("[\n]", ",", data)
        mas_Tel_Sprav = list_of_words.split(',')
    return mas_Tel_Sprav

def data_tel_spravka(data):
    lst = np.array(data)
    b = np.hsplit(lst, 4)
    av = []
    for i in range(len(b)):
        av.append(b[i].tolist())
    return av






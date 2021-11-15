# Run pip install feather-format if you dont have the module installed

from pymatreader import read_mat
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import feather

import os
os.mkdir('data')

def create_dataset(data):
	X, Y = [], []
	for i in range(len(dataset)-2):
		a = dataset[i:(i+1), 0]
		X.append(a)
		Y.append(dataset[i + 1, 0])
	return np.array(X), np.array(Y)

def get_from_indices(df, row, type):
    row_data = df['cycle'][row]
    req_data = []
    for i in sep_indices[type]: 
        req_data.append(row_data[i])

    return req_data

def df_subpart(df, type):
    df_info = {'temp': get_from_indices(df,0,type), 
               'data': get_from_indices(df,1,type)}

    return pd.DataFrame.from_dict(df_info)

def save_dc(mat, type, drop_time = False):
    global sep_indices

    data = read_mat(mat)
    df = pd.DataFrame(data[mat[:-4]])
    df = df.transpose().drop(columns = 'time').transpose()
    
    sep_indices = {'impedance': [], 'charge': [], 'discharge': []}
    for i in range(len(df['cycle'][2])):
        for j in ['discharge', 'charge', 'impedance']:
            if df['cycle'][2][i] == j: sep_indices[j].append(i)

    if type == 'charge': prefix = '_c'
    elif type == 'discharge': prefix = '_dc'
    else: prefix = '_imp'

    df_sub = df_subpart(df, type)
    feather.write_dataframe(df_sub, 'data/' + mat[:-4] + prefix + '.feather')

names = ['B0005.mat','B0006.mat','B0007.mat','B0018.mat']
for i in names: 
    save_dc(i, 'discharge')
    save_dc(i, 'charge')
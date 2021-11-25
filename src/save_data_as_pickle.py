# Run pip install feather-format if you dont have the module installed
from pymatreader import read_mat
import pandas as pd
import numpy as np

import os
if not 'data' in os.listdir(): os.mkdir('data')

def to_sec(vec):
    mon, day, hr, min, sec = vec[1:]
    return (mon*30*86400 + day*86400 + hr*3600 + min*60 + sec)

def save(mat):
    data = read_mat("C:/Users/bhavy/Courses/DS_203/Project/" + mat)
    df = pd.DataFrame(data[mat[:-4]]['cycle'])

    times_fromzero = [np.array(df['time'])[i] - np.array(df['time'][0]) for i in range(len(df))]
    times = []
    for i in times_fromzero:
        times.append(to_sec(i))
    df['time'] = times
    df['data'] = np.array([[df['data'][i]] for i in range(len(df))])
    df.to_pickle('data/' + mat[:-4] + '.pkl')

names = ['B0005.mat','B0006.mat','B0007.mat','B0018.mat']
for i in names: 
    save(i)
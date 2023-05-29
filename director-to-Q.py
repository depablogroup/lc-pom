# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:01:58 2023

@author: chenc
"""
# In[]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
import numpy.linalg as la
import re
import pandas as pd

cmap = plt.get_cmap('jet')
plt.style.use('./large_plot.mplstyle')
np.set_printoptions(precision=5)
np.set_printoptions(suppress=True)


# In[]:
def read_vtk(filename, folder):
    filepath = folder+filename
    df = pd.read_csv(filepath)
    print ("S, min, max, mean  %.2f, %.2f, %.2f" %(np.min(df["scalar"]), np.max(df["scalar"]) ,np.mean(df["scalar"])))
    return df

def director_to_Q(df):
    df ["q1"] = (df["director_0"]*df["director_0"]-1.0/3.0)*df["scalar"]
    df ["q2"] = df["director_0"]*df["director_1"]*df["scalar"]
    df ["q3"] = df["director_0"]*df["director_2"]*df["scalar"]
    df ["q4"] = (df["director_1"]*df["director_1"]-1.0/3.0)*df["scalar"]
    df ["q5"] = df["director_1"]*df["director_2"]*df["scalar"]
    return df

def write_Q_csv(df, filename, folder):
    filepath = folder + filename
    df.to_csv (filepath, columns = ["Points_0","Points_1","Points_2","q1" ,"q2" ,"q3","q4","q5"])
    return
if __name__ == "__main__":
    plt.close("all")
    # Read
    folder = "./vtks/"
    #filename = "radial.csv"
    #filename = "bipolar.csv"
    #filename = "radial-mediumring.csv"
    filename = "chol_spiral.csv"
    df = read_vtk(filename, folder)
    print (df.columns)
    # Form Q tensor
    df = director_to_Q(df)
    #savename = "radial_Q.csv"
    savename = "chol_spiral_Q.csv"
    # Save
    savefolder = "./Original_Director_Field/"
    write_Q_csv(df, savename, savefolder)
    print (df.columns)
    
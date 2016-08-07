# -*- coding: utf-8 -*-
"""
Spyder Editor

Input - CSV of student data. 
Output - Plots and text info

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def csvimport(csvname):
    df = pd.read_csv(csvname)
    df = df.dropna()
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    dfn = df.select_dtypes(include=numerics)
    dfn = dfn.drop('Student Id', axis=1)
    return dfn, df

def plothist(df, filename):
    c = df.columns
    with PdfPages(filename + '.pdf') as pdf:
        for i in c:
            plt.figure()
            plt.title('Distribution of marks for' + i)
            sns.distplot(df[i])
            save_name = 'histogram:' + i +'.png'
            pdf.attach_note(save_name)
            pdf.savefig()
            plt.close()
            
            
def plotbox(df, g, filename):
    c = df.columns
    with PdfPages(filename + '.pdf') as pdf:
        for i in c:
            plt.figure()
            plt.title('Boxplot of ' + i)
            sns.boxplot(df[i], g)
            save_name = 'boxplot' + i +'.png'
            pdf.attach_note(save_name)
            pdf.savefig()
            plt.close()

def main(csv, yeargroup):
    dfn, df = csvimport(csv)
    plothist(dfn, yeargroup + 'Distribution of marks')
    plotbox(dfn, df['Class'], yeargroup + 'Boxplots')

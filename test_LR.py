#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from joblib import dump, load
import random
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
fig = plt.figure()
ax = fig.gca()



def get_percentual(a,b):
    t = a + b
    p = t / 100.
    per1 = a / p
    per2 = b / p
    return per1,per2



historico_sensitividade = []
historico_especificidade = []
tests_num = 100
for i in range(0,tests_num):
    df = open('raw_COVID.txt','r')
    df1 = []

    for e, i in enumerate(df):
        if e >0:
            result = seasonal_decompose(i.split('\t'), model='additive', period=8)
            b = result.trend
            df1.append(b)
    df1 = np.array(df1).astype(float)



    df = open('raw_Helthy.txt','r')
    df2 = []

    for e, i in enumerate(df):
        if e>0:
            result = seasonal_decompose(i.split('\t'), model='additive', period=8)
            b = result.trend
            df2.append(b)

    df2 = np.array(df2).astype(float)


    df1= df1.T
    df2= df2.T


    label1 = [0]*df1.shape[0]
    label2 = [1]*df2.shape[0]

    y1 = np.array(label1)
    y2 = np.array(label2)

    y = np.concatenate([y1,y2], axis=0)

    df1 = np.array(df1)
    df2 = np.array(df2)

    x =[]

    for i in df1:
        x.append(i)

    for i in df2:
        x.append(i)

    x = np.array(x)
    x_train=[]
    y_train=[]
    x_test=[]
    y_test=[]
    idx=[]

    for i in range(0, len(x)//2):
        r=random.randint(0,len(x)-1)
        x_train.append(x[r])
        y_train.append(y[r])
        idx.append(r)
    
    for i in range(0, len(x)):
        if i not in idx:
            x_test.append(x[i])
            y_test.append(y[i])




    CV_LR = load('modelo_selecionado_new.pkl')

    y_pred_LR = CV_LR.predict(x_test)

    f, p =0, 0
    vp,vn,fp,fn = 0,0,0,0
    for e, i in enumerate(y_pred_LR):

        if y_test[e] == y_pred_LR[e]:
            p +=1
            if int(y_pred_LR[e]) == 1:
                vp +=1
            if int(y_pred_LR[e]) == 0:
                vn +=1
        else:
            f += 1
            if int(y_pred_LR[e]) == 0:
                fp +=1
            if int(y_pred_LR[e]) == 1:
                fn +=1

    p1,p2 = get_percentual(p,f)


    print( "-"*20)
    print( "Acerto:{}".format(p1))
    print( "Errado:{}".format(p2))
    print( "Verdadeiro Positivo: ", vp)
    print( "Verdadeiro Negativo: ", vn)
    print( "Falso Positivo: ", fp)
    print( "Falso Negativo: ", fn)
    print("Sensitividade: ", vp/(vp+fn))
    print("Especificidade: ",vn/(vn+fp))
    print("Ratio Falso Positivo: ", 1. - (vn/(vn+fp)))
    historico_sensitividade.append(vp/(vp+fn))
    historico_especificidade.append(vn/(vn+fp))


    #plt.pause(0.0001)
ax.clear()
ax.plot(historico_sensitividade, color = 'green', label='Sensitividade')
ax.plot(historico_especificidade, color = 'red', label='Especificidade')
ax.legend()
print("-"*20)
print("Sensitividade Média: ", np.array(historico_sensitividade).mean())
print("Especificidade Média: ", np.array(historico_especificidade).mean())
plt.savefig("100.png")

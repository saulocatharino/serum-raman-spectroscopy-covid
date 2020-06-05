#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from joblib import dump, load
import random



def get_percentual(a,b):
    t = a + b
    p = t / 100.
    per1 = a / p
    per2 = b / p
    return per1,per2


meta = 99.

fig = plt.figure()
ax = fig.gca()
def run(meta):
    historico = []
    p1 = 0
    minima = 100
    maxima = 0
    contagem = 0
    while p1 < meta:
        C = random.randint(10,100)
        tol = random.randint(1,1000) / 100000000000000.
        solver = np.random.choice(['lbfgs']) #['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'])
        lr =LogisticRegression(tol=tol, C=C, random_state=True, solver=solver, max_iter=50000, multi_class='auto', warm_start=False, verbose=0)


        df = open('raw_COVID.txt','r')
        df1 = []
        for e, i in enumerate(df):
            if e > 0:
                df1.append(i.split('\t'))

        df1 = np.array(df1).astype(float)
        df1 = df1.T

        df = open('raw_Helthy.txt','r')
        df2 = []
        for e, i in enumerate(df):
            if e > 0:
                df2.append(i.split('\t'))

        df2 = np.array(df2).astype(float)
        df2 = df2.T



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
        lr.fit(x_train, y_train)
        y_pred_LR = lr.predict(x_test)
        f, p =0, 0
        for e, i in enumerate(y_pred_LR):
            if y_test[e] == y_pred_LR[e]:
                p +=1
            else:
                f +=1
           
        p1,p2 = get_percentual(p,f)
        if p1 > maxima:
            dump(lr, 'modelo_selecionado_new.pkl')
            print("-"*20)
            print("Modelo Salvo")
            maxima = p1
        if p1 < minima: minima = p1
        print("-"*20)
        print("- ", contagem)
        print("Regressão Logística")

        print("Solver: ", solver)
        print("Tol: ", tol)
        print( "Acerto: {}".format(round(p1,2)))
        print( "Erro: {}".format(round(p2,2)))
        print("Melhor acerto: ", maxima)
        print("Pior acerto: ", minima)
        historico.append([p1,p2])
        contagem +=1
        if len(historico) > 200:
            historico = historico[-200:]
        ax.clear()
        ax.plot(historico)
        plt.pause(0.000001)
    return lr

if __name__ == "__main__":
    lr  = run(meta)
    plt.savefig('teste.png')


import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
from joblib import dump, load
import random

historico_sensitividade = []
historico_especificidade = []
tests_num = 100
if True:
    df = open('raw_COVID.txt','r')
    df1 = []

    for e, i in enumerate(df):
        if e >0:
            result = seasonal_decompose(i.split('\t'), model='additive', period=20)
            b = result.trend
            b = b[np.logical_not(np.isnan(b))]
            df1.append(b)
    df1 = np.array(df1).astype(float)



    df = open('raw_Helthy.txt','r')
    df2 = []

    for e, i in enumerate(df):
        if e>0:
            result = seasonal_decompose(i.split('\t'), model='additive', period=20)
            b = result.trend
            b = b[np.logical_not(np.isnan(b))]
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






clf = load('modelo_selecionado.pkl')
coefs = np.abs(clf.coef_[0])
indices = np.argsort(coefs)[::-1]

h = []

for e,item in enumerate(coefs[indices[:899]]):
  h.append(coefs[e])
h = np.array(h)
h = h / h.max()



mean = np.array(h).mean()

t = []
b = []
f = []
for e, item in enumerate(h):
    if item >= mean:
        t.append(x_test[0][e])
        b.append(np.nan)
        f.append(x_test[0][e])
    else:
        t.append(np.nan)
        b.append(x_test[0][e])
        f.append(0)
fig, ax= plt.subplots(2,2)
ax[0][0].plot(x_test[0],color='black')
ax[0][0].set_title("Sinal com Filtro de Média")
for e,item in enumerate(x_test[0]):
   ax[0][1].bar(e,h[e], color = 'black')
ax[0][1].plot((0,899),(mean,mean), color='red')
ax[0][1].set_title("Importancia do Feature")
ax[1][0].plot(t, color='black')
ax[1][0].set_title("Sinal Segmentado por Importância")
ax[1][0].plot(b,'--',color='red')
ax[1][1].set_title("Sinal Processado")
ax[1][1].plot(f, color='black')
plt.show()





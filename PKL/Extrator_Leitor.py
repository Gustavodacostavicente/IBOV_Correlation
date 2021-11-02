
from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd
import pytz





if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 

Ativos = ['ABEV3','B3SA3','BBSE3','BRML3','BBDC3','BBDC4','BRAP4','BBAS3',
           'BRKM5','BRFS3','CCRO3','CMIG4','HGTX3','CIEL3','COGN3','CPLE6','CSAN3','CPFE3',
           'CVCB3','CYRE3','ECOR3','ELET3','EMBR3','ENBR3','ENEV3','EGIE3','EQTL3','EZTC3','FLRY3',
           'GGBR4','GOAU4','GOLL4','NTCO3','HYPE3','IGTA3','ITSA4','ITUB4','JBSS3',
           'JHSF3','KLBN11','RENT3','LCAM3','LAME4','LREN3','MGLU3','MRFG3','BEEF3','MRVE3','MULT3',
           'PETR3','PETR4','PRIO3','QUAL3','RADL3','RAIL3','SBSP3','SANB11','CSNA3','SULA11',
           'SUZB3','TAEE11','VIVT3','TIMS3','TOTS3','UGPA3','USIM5','VALE3','WEGE3','YDUQ3']

timezone = pytz.timezone("Brazil/West")

for i in range(0,len(Ativos)):
    
    try:
        Ativo = mt5.copy_rates_from(Ativos[i], mt5.TIMEFRAME_D1, datetime.today(), 5000)
        Ativo_Frame = pd.DataFrame(Ativo)
        Ativo_Frame['time']=pd.to_datetime(Ativo_Frame['time'], unit='s')
        Ativo_Frame.to_pickle(str(Ativos[i])+"_D1.pkl")
    except:
        pass

mt5.shutdown()


 


#%%   

from sklearn.preprocessing import minmax_scale
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

Ativos = ['ABEV3','B3SA3','BBSE3','BRML3','BBDC3','BBDC4','BRAP4','BBAS3',
           'BRKM5','BRFS3','CCRO3','CMIG4','HGTX3','CIEL3','COGN3','CPLE6','CSAN3','CPFE3',
           'CVCB3','CYRE3','ECOR3','ELET3','EMBR3','ENBR3','ENEV3','EGIE3','EQTL3','EZTC3','FLRY3',
           'GGBR4','GOAU4','GOLL4','NTCO3','HYPE3','IGTA3','ITSA4','ITUB4','JBSS3',
           'JHSF3','KLBN11','RENT3','LCAM3','LAME4','LREN3','MGLU3','MRFG3','BEEF3','MRVE3','MULT3',
           'PETR3','PETR4','PRIO3','QUAL3','RADL3','RAIL3','SBSP3','SANB11','CSNA3','SULA11',
           'SUZB3','TAEE11','VIVT3','TIMS3','TOTS3','UGPA3','USIM5','VALE3','WEGE3','YDUQ3']

Lista = pd.DataFrame()   
for i in range(0,len(Ativos)):
    Ativo_Lido = pd.read_pickle(str(Ativos[i])+"_D1.pkl")
    Ativo_Normalizado = minmax_scale(Ativo_Lido['close'], feature_range=(0,1))
    Ativo_Normalizado_Cortado = Ativo_Normalizado[len(Ativo_Normalizado)-1000:]
    Lista.insert(i,Ativos[i],Ativo_Normalizado_Cortado,True)



corr_lista = Lista.corr(method='pearson')
#sns.heatmap(corr_lista, annot=True)


Corr_Array = np.array(corr_lista)
Lista_Selecionada = []
for j in range(0,len(Corr_Array)):
    for i in range(0,len(Corr_Array)):
        if (abs(Corr_Array[j,i])>0.8):
            Lista_Selecionada.append(str("{:.2f}".format(Corr_Array[j,i])) + ' ' + Ativos[j] + '-' + Ativos[i])
            
Lista_Filtrada = []
for i in range(0, len(Lista_Selecionada)):
    
    if(Lista_Selecionada[i][0] != '1'):
        Lista_Filtrada.append(Lista_Selecionada[i])

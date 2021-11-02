import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.preprocessing import MinMaxScaler


Ativos = ['ABEV3','B3SA3','BBSE3','BRML3','BBDC3','BBDC4','BRAP4','BBAS3',
           'BRKM5','BRFS3','CCRO3','CMIG4','HGTX3','CIEL3','COGN3','CPLE6','CSAN3','CPFE3',
           'CVCB3','CYRE3','ECOR3','ELET3','EMBR3','ENBR3','ENEV3','EGIE3','EQTL3','EZTC3','FLRY3',
           'GGBR4','GOAU4','GOLL4','NTCO3','HYPE3','IGTA3','ITSA4','ITUB4','JBSS3',
           'JHSF3','KLBN11','RENT3','LCAM3','LAME4','LREN3','MGLU3','MRFG3','BEEF3','MRVE3','MULT3',
           'PETR3','PETR4','PRIO3','QUAL3','RADL3','RAIL3','SBSP3','SANB11','CSNA3','SULA11',
           'SUZB3','TAEE11','VIVT3','TIMS3','TOTS3','UGPA3','USIM5','VALE3','WEGE3','YDUQ3']

# Faltantes --> 'ASAI3','LWSA3','PCAR3','BIDI11','HAPV3','GNDI3',BRDT3,'IRBR3','CRFB3','AZUL4','BPAC11','VIIA3','ENGI11'

Planilhas_de_Dados = []
Ativos_Novos = []
Lista = pd.DataFrame()
z = 0
for i in range(0, len(Ativos)):
    Ativos_Novos.append(Ativos[i]+'_Daily.csv')
    Planilhas_de_Dados.append(Ativos_Novos[i])
    Dados_Ativo =  pd.read_csv(Planilhas_de_Dados[i],  delimiter=r"\s+")
    print(str(len(Dados_Ativo))+ '_' + Ativos[i])
    z = len(Dados_Ativo) + z
    Lista.insert(i,Ativos[i],Dados_Ativo['<CLOSE>'],True)
    

print('Total é: ', z/len(Ativos))
corr_lista = Lista.corr(method='pearson')

# plt.figure(figsize=(8, 6))
# sns.heatmap(corr_lista, annot=True)
# plt.show()

print('\n')
print('\n')
print('\n')
print('\n')
#%%

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
            
            
#%%
Planilha_Lista_Filtrada =  pd.read_csv('Lista_Filtrada.csv',delimiter=';')


   
Maiores_20_Ibov = ['VALE3','ITUB4','PETR4','B3SA3','BBDC4','PETR3','ABEV3','MGLU3','WEGE3','SUZB3','CSAN3',
                    'ITSA4','JBSS3','NTCO3','RENT3','BBAS3','GGBR4','LREN3','CSNA3','RADL3']









Classificacao =  pd.read_csv('Classificacao.csv',  delimiter=";")


# Lista_Maiores = pd.DataFrame()
# for i in range(0,len(Planilha_Lista_Filtrada)):
#     if(Planilha_Lista_Filtrada['Ativo1'][i]=='VALE3'):
#         print(Planilha_Lista_Filtrada['Corr'][i])
#         Lista_Maiores.insert(i,Planilha_Lista_Filtrada['Corr'][i],Planilha_Lista_Filtrada['Ativo2'][i],True)



Normaliza = MinMaxScaler(feature_range=(0, 1))# Função de Normalização entre 0 e 1
VALE3 = np.array(Lista['VALE3'])
VALE3 = Normaliza.fit_transform(VALE3) # Normaliza os valores de entrada

plt.plot(Lista['VALE3'])
plt.plot(VALE3)
# for j in range(0,len(Maiores_20_Ibov)):
#     Count = 0
#     Lista_Ativo_Selecionada=[]
#     plt.figure(j)
#     for i in range(1,len(Planilha_Lista_Filtrada)):
#         if(Planilha_Lista_Filtrada['Ativo1'][i] == Maiores_20_Ibov[j]):
#             Lista_Ativo_Selecionada.append(Planilha_Lista_Filtrada['Ativo2'][i])
#             #print(str(j)+','+str(i))
#             Count = Count+1
            
#             plt.plot(Lista[Planilha_Lista_Filtrada['Ativo2'][i]])
#             plt.legend(Lista[Planilha_Lista_Filtrada['Ativo2'][i]])
#     Lista_Ativo_Selecionada.append(Maiores_20_Ibov[j])
#     print(Lista_Ativo_Selecionada)
            
                
                
                
                
                
                
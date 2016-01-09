# -*- coding: utf-8 -*-
"""
Created on Tue May  5 22:21:24 2015

@author: João Frederico Vieira de Oliveira | R3 Patologia Clínica, UNICAMP 
"""

import pandas as pd
import numpy as np
import scipy as sp
import statsmodels as sm
import random as ra
import seaborn as sns
import matplotlib.pyplot as plt
import csv
from pandas import DataFrame, Series, qcut, cut, crosstab, concat
from scipy.stats.stats import pearsonr, spearmanr
from statsmodels.stats.inter_rater import *
from statsmodels.sandbox.stats.runs import mcnemar


################################################################################################
#
#                                         DATAFRAMES
#
################################################################################################


df = pd.read_csv("./URI_TOTAL_DATA.csv")

###########################################################

sg_amb = df[(df.EXAME == "SG") & (df.LOCAL == "AMB")]
sg_gel = df[(df.EXAME == "SG") & (df.LOCAL == "GEL")]

ph_amb = df[(df.EXAME == "PH") & (df.LOCAL == "AMB")]
ph_gel = df[(df.EXAME == "PH") & (df.LOCAL == "GEL")]

leu_amb = df[(df.EXAME == "LEU") & (df.LOCAL == "AMB")]
leu_gel = df[(df.EXAME == "LEU") & (df.LOCAL == "GEL")] 

nit_amb = df[(df.EXAME == "NIT") & (df.LOCAL == "AMB")]
nit_gel = df[(df.EXAME == "NIT") & (df.LOCAL == "GEL")]

pro_amb = df[(df.EXAME == "PRO") & (df.LOCAL == "AMB")]
pro_gel = df[(df.EXAME == "PRO") & (df.LOCAL == "GEL")]

glu_amb = df[(df.EXAME == "GLU") & (df.LOCAL == "AMB")]
glu_gel = df[(df.EXAME == "GLU") & (df.LOCAL == "GEL")]

ket_amb = df[(df.EXAME == "KET") & (df.LOCAL == "AMB")]
ket_gel = df[(df.EXAME == "KET") & (df.LOCAL == "GEL")]

ubg_amb = df[(df.EXAME == "UBG") & (df.LOCAL == "AMB")]
ubg_gel = df[(df.EXAME == "UBG") & (df.LOCAL == "GEL")]

bil_amb = df[(df.EXAME == "BIL") & (df.LOCAL == "AMB")]
bil_gel = df[(df.EXAME == "BIL") & (df.LOCAL == "GEL")]

bld_amb = df[(df.EXAME == "BLD") & (df.LOCAL == "AMB")]
bld_gel = df[(df.EXAME == "BLD") & (df.LOCAL == "GEL")]

###########################################################

rbc_amb = df[(df.EXAME == "RBC") & (df.LOCAL == "AMB")]
rbc_gel = df[(df.EXAME == "RBC") & (df.LOCAL == "GEL")]
rbc_amb[["H0", "H4", "H8", "H12", "H24"]] = rbc_amb[["H0", "H4", "H8", "H12", "H24"]].astype(float)
rbc_gel[["H0", "H4", "H8", "H12", "H24"]] = rbc_gel[["H0", "H4", "H8", "H12", "H24"]].astype(float)

muc_amb = df[(df.EXAME == "MUC") & (df.LOCAL == "AMB")]
muc_gel = df[(df.EXAME == "MUC") & (df.LOCAL == "GEL")]
muc_amb[["H0", "H4", "H8", "H12", "H24"]] = muc_amb[["H0", "H4", "H8", "H12", "H24"]].astype(float)
muc_gel[["H0", "H4", "H8", "H12", "H24"]] = muc_gel[["H0", "H4", "H8", "H12", "H24"]].astype(float)

caoxd_amb = df[(df.EXAME == "CAOXD") & (df.LOCAL == "AMB")]
caoxd_gel = df[(df.EXAME == "CAOXD") & (df.LOCAL == "GEL")]
caoxd_amb[["H0", "H4", "H8", "H12", "H24"]] = caoxd_amb[["H0", "H4", "H8", "H12", "H24"]].astype(float)
caoxd_gel[["H0", "H4", "H8", "H12", "H24"]] = caoxd_gel[["H0", "H4", "H8", "H12", "H24"]].astype(float)

hya_amb = df[(df.EXAME == "HYA") & (df.LOCAL == "AMB")]
hya_gel = df[(df.EXAME == "HYA") & (df.LOCAL == "GEL")]
hya_amb[["H0", "H4", "H8", "H12", "H24"]] = hya_amb[["H0", "H4", "H8", "H12", "H24"]].astype(float)
hya_gel[["H0", "H4", "H8", "H12", "H24"]] = hya_gel[["H0", "H4", "H8", "H12", "H24"]].astype(float)


bac_amb = df[(df.EXAME == "BAC") & (df.LOCAL == "AMB")]
bac_gel = df[(df.EXAME == "BAC") & (df.LOCAL == "GEL")]
bac_amb[["H0", "H4", "H8", "H12", "H24"]] = bac_amb[["H0", "H4", "H8", "H12", "H24"]].astype(float)
bac_gel[["H0", "H4", "H8", "H12", "H24"]] = bac_gel[["H0", "H4", "H8", "H12", "H24"]].astype(float)


pat_amb = df[(df.EXAME == "PAT") & (df.LOCAL == "AMB")]
pat_gel = df[(df.EXAME == "PAT") & (df.LOCAL == "GEL")]
pat_amb[["H0", "H4", "H8", "H12", "H24"]] = pat_amb[["H0", "H4", "H8", "H12", "H24"]].astype(float)
pat_gel[["H0", "H4", "H8", "H12", "H24"]] = pat_gel[["H0", "H4", "H8", "H12", "H24"]].astype(float)

wbc_amb = df[(df.EXAME == "WBC") & (df.LOCAL == "AMB")]
wbc_gel = df[(df.EXAME == "WBC") & (df.LOCAL == "GEL")]
wbc_amb[["H0", "H4", "H8", "H12", "H24"]] = wbc_amb[["H0", "H4", "H8", "H12", "H24"]].astype(float)
wbc_gel[["H0", "H4", "H8", "H12", "H24"]] = wbc_gel[["H0", "H4", "H8", "H12", "H24"]].astype(float)

epi_amb = df[(df.EXAME == "EPI") & (df.LOCAL == "AMB")]
epi_gel = df[(df.EXAME == "EPI") & (df.LOCAL == "GEL")]
epi_amb[["H0", "H4", "H8", "H12", "H24"]] = epi_amb[["H0", "H4", "H8", "H12", "H24"]].astype(float)
epi_gel[["H0", "H4", "H8", "H12", "H24"]] = epi_gel[["H0", "H4", "H8", "H12", "H24"]].astype(float)

tri_amb = df[(df.EXAME == "TRI") & (df.LOCAL == "AMB")]
tri_gel = df[(df.EXAME == "TRI") & (df.LOCAL == "GEL")]
tri_amb[["H0", "H4", "H8", "H12", "H24"]] = tri_amb[["H0", "H4", "H8", "H12", "H24"]].astype(float)
tri_gel[["H0", "H4", "H8", "H12", "H24"]] = tri_gel[["H0", "H4", "H8", "H12", "H24"]].astype(float)

uri_amb = df[(df.EXAME == "URI") & (df.LOCAL == "AMB")]
uri_gel = df[(df.EXAME == "URI") & (df.LOCAL == "GEL")]
uri_amb[["H0", "H4", "H8", "H12", "H24"]] = uri_amb[["H0", "H4", "H8", "H12", "H24"]].astype(float)
uri_gel[["H0", "H4", "H8", "H12", "H24"]] = uri_gel[["H0", "H4", "H8", "H12", "H24"]].astype(float)

yea_amb = df[(df.EXAME == "YEA") & (df.LOCAL == "AMB")]
yea_gel = df[(df.EXAME == "YEA") & (df.LOCAL == "GEL")]
yea_amb[["H0", "H4", "H8", "H12", "H24"]] = yea_amb[["H0", "H4", "H8", "H12", "H24"]].astype(float)
yea_gel[["H0", "H4", "H8", "H12", "H24"]] = yea_gel[["H0", "H4", "H8", "H12", "H24"]].astype(float)

amo_amb = df[(df.EXAME == "AMO") & (df.LOCAL == "AMB")]
amo_gel = df[(df.EXAME == "AMO") & (df.LOCAL == "GEL")]
amo_amb[["H0", "H4", "H8", "H12", "H24"]] = amo_amb[["H0", "H4", "H8", "H12", "H24"]].astype(float)
amo_gel[["H0", "H4", "H8", "H12", "H24"]] = amo_gel[["H0", "H4", "H8", "H12", "H24"]].astype(float)


###########################################################


dfcont = df[df.EXAME.isin(["BAC", "RBC", "MUC", "CAOXD", "HYA", "PAT", "WBC", 
                           "EPI","TRI", "URI", "YEA", "AMO"])]
dfcont[["H0", "H4", "H8", "H12", "H24"]] = dfcont[["H0", "H4", "H8", "H12", "H24"]].astype(float)
dfcontmelt = pd.melt(dfcont, id_vars=['KEY', 'EXAME', 'LOCAL']) 
dfcontmelt.columns = ['KEY', 'EXAME', 'LOCAL', 'HORA', 'MEDIDA']
        
def caixas():
    for i in ["BAC", "RBC", "MUC", "CAOXD", "HYA", "PAT", "WBC", "EPI","TRI", "URI", "YEA", "AMO"]:
        plt.clf()
        plt.close()
        filename = "boxplot"+i+".png"
        sns.boxplot(x="HORA", y="MEDIDA", hue="LOCAL", 
                data=dfcontmelt[dfcontmelt.EXAME == i], palette="PRGn", sym="")
        plt.savefig(filename)


dfcate = df[df.EXAME.isin(["BLD", "BIL", "UBG", "KET", "GLU", "PRO", "NIT", 
                           "LEU","PH", "SG"])]

dfcatemelt = pd.melt(dfcate, id_vars=['KEY', 'EXAME', 'LOCAL'])
dfcatemelt.columns = ['KEY', 'EXAME', 'LOCAL', 'HORA', 'MEDIDA']

#sns.factorplot(x="MEDIDA", kind="count", hue="HORA", 
#               data=testesg, order = [1000,1005,1010,1015,1020,1025,1030])

#sns.factorplot(x="MEDIDA", kind="count", hue="HORA", data=testesg, 
#               order = sorted( testesg.MEDIDA.unique()))

#sns.factorplot(x="MEDIDA", kind="count", hue="HORA", 
#               data=dfcatemelt[dfcatemelt.EXAME == "SG"], 
#               order = sorted(dfcatemelt[dfcatemelt.EXAME=="SG"].MEDIDA.unique()))

#sns.factorplot(x="MEDIDA", kind="count", hue="HORA", 
#               data=dfcatemelt[dfcatemelt.EXAME == "BLD"], 
#               order = ["neg", "C1", "C2", "C3"])

def plotsbarra(exames = ["BLD", "BIL", "UBG", "KET", "GLU", "PRO", "NIT", "LEU","PH"]):
    for i in exames:
        filename = "barplot"+i+".png"        
        ordem = sorted(dfcatemelt[dfcatemelt.EXAME==i].MEDIDA.unique())
        if "neg" in ordem:
            ordem.remove("neg")
            ordem.insert(0, "neg")
        print(":: para",i)
        sns.factorplot(x="MEDIDA", kind="count", hue="HORA", 
                       data=dfcatemelt[dfcatemelt.EXAME == i], 
                       order = ordem)
        plt.savefig(filename)


def procurarduplicatas():
    contador = 0
    for i in sorted(df.KEY.unique()):
        if len(df.KEY[df.KEY == i]) != 44: 
            print(":: Duplicata em",i)
        contador += 1
    print("total de contagens feitas:",contador)





'''
################################################################################################

                                  DICIONÁRIOS E CONSTANTES

################################################################################################
'''
def namestr(obj, namespace=globals()): return([name for name in namespace if namespace[name] is obj][0])

_dicsed = {"RBC": 5, "WBC": 5, "CAOXD": 1.82, "TRI": 1.82, "AMO": 1.82,"HYA": 0.2, 
           "EPI": 0.37, "YEA": 0.2, "BAC": 8.33, "MUC": 25, "PAT": 0.3, "URI": 1.82}

_dic_cruzes = {"neg": 0, "pos": 1, "C1" : 1, "C2" : 2, "C3" : 3, "C4" : 4}
__l = "................................................................."
___l = "................................................................................"
_par_paula = [[wbc_amb, wbc_gel],[bac_amb, bac_gel],[rbc_amb, rbc_gel],[pat_amb, pat_gel],[amo_amb, amo_gel],]
_grupo_continuo = [wbc_amb, wbc_gel,bac_amb, bac_gel,rbc_amb, rbc_gel,pat_amb, pat_gel,amo_amb, amo_gel]
_grupo_discreto1 = [leu_amb, leu_gel, nit_amb, nit_gel, pro_amb, pro_gel, glu_amb, 
                   glu_gel, ket_amb, ket_gel, bil_amb, bil_gel, bld_amb, bld_gel, ubg_gel, ubg_amb]
_grupo_discreto2 = [ph_gel, ph_amb, sg_amb, sg_gel]

_dic_continuo = {namestr(wbc_amb):"Leucócitos", namestr(wbc_gel): "Leucócitos", namestr(bac_amb):"Bactérias", 
                 namestr(bac_gel):"Bactérias",namestr(rbc_amb):"Eritrócitos", namestr(rbc_gel): "Eritrócitos",
                 namestr(pat_amb):"Cilindros Pat.", namestr(pat_gel):"Cilindros Pat.",
                 namestr(amo_amb): "Cristais Amorfos", namestr(amo_gel): "Cristais Amorfos"}
_dic_discreto = {namestr(ph_amb):"pH", namestr(ph_gel): "pH", namestr(sg_amb):"Densidade", namestr(sg_gel):"Densidade", 
                 namestr(leu_amb):"Leucócitos", namestr(leu_gel):"Leucócitos", namestr(nit_amb):"Nitrito", 
                 namestr(nit_gel): "Nitrito", namestr(pro_amb): "Proteínas", namestr(pro_gel):"Proteínas", 
                 namestr(glu_amb):"Glicose", namestr(glu_gel): "Glicose", namestr(ket_amb):"Corpos cetônicos", 
                 namestr(ket_gel):"Corpos cetônicos", namestr(ubg_amb): "Urobilinogênio",
                 namestr(ubg_gel): "Urobilinogênio", namestr(bil_amb):"Bilirrubina", namestr(bil_gel): "Bilirrubina",
                 namestr(bld_amb): "Hemoglobina", namestr(bld_gel): "Hemoglobina"}


'''    
################################################################################################

                                          FUNÇÕES

################################################################################################
'''
fontetamanho = 20

def filtrased1(data, linha):
    amostra = data._slice(slice(linha,linha+1))
    if list(amostra.EXAME)[0] in _dicsed:
        if list(amostra.MEDIDA)[0] < _dicsed[list(amostra.EXAME)[0]]: return("neg")
        elif list(amostra.MEDIDA)[0] >= _dicsed[list(amostra.EXAME)[0]]: return("pos")
        else: print("deu erro em", amostra.index)
    else: return(list(amostra.MEDIDA)[0])

def filtrasedmini1(data, linha, horario):
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",linha)
    #amostra = data._slice(slice(linha,linha+1))
    amostra = data[horario][linha]
    if list(data.EXAME)[0] in _dicsed:
        print("OK!")
        if list(amostra[horario])[0] < _dicsed[list(amostra.EXAME)[0]]: return("neg")
        elif list(amostra[horario])[0] >= _dicsed[list(amostra.EXAME)[0]]: return("pos")
        else: print("deu erro em", amostra.index)
    else: return(list(amostra[hora])[0])

#filtrasedmini1(yea_amb, 42, "H0")

def filtrased(data):
    for i in data.index:
        data.MEDIDA[i] = filtrased1(data, i)
    return(data)

def filtrasedmini(data):
    for indice in data.index[0:10]:
        for hora in ["H0", "H4", "H8", "H12", "H24"]:    
            data[hora][indice] = filtrasedmini1(data, indice, hora)
    return(data)



#yea_amb = filtrasedmini(yea_amb)

def namestr(obj, namespace=globals()): return([name for name in namespace if namespace[name] is obj][0])

def grafico_j(conjunto, xl=None, yl=None, titulox="", tituloy="", filename="", tamanho=5, titulo=""):
    a = np.array(conjunto[0].map(float))
    b = np.array(conjunto[1].map(float))
    c = DataFrame([a,b]).transpose()
    c.columns = ["A", "B"]
    g = sns.jointplot("A", "B", c, xlim=xl, ylim=yl, kind = "reg", stat_func=stats.spearmanr, 
                      marginal_kws={"bins": 25}, size=tamanho)
    # marginal_kws={"bins": 297}
    sns.axlabel(titulox, tituloy, fontsize=fontetamanho)
    plt.title(titulo, y=1.22, fontsize=20)
    plt.savefig(filename, bbox_inches="tight", format = "png");

def grafico_l(conjunto, xl=None, yl=None, titulox="", tituloy="", titulo="", filename="", tamanho=5):
    a = np.array(conjunto[0].map(float))
    b = np.array(conjunto[1].map(float))
    c = DataFrame([a,b]).transpose()
    c.columns = ["A", "B"]
    sns.lmplot("A", "B", c, x_jitter=0.2, y_jitter=0.3, size=tamanho)
    plt.title(titulo, fontsize=16)
    sns.axlabel(titulox, tituloy, fontsize=fontetamanho)
    plt.savefig(filename);

def grafico_l2(conjunto, xl=None, yl=None, titulox="", tituloy="", titulo="", filename="", tamanho=5):
    a = np.array(conjunto[0].map(_dic_cruzes))
    b = np.array(conjunto[1].map(_dic_cruzes))
    c = DataFrame([a,b]).transpose()
    c.columns = ["A", "B"]
    sns.lmplot("A", "B", c, x_jitter=0.2, y_jitter=0.3, size=tamanho)
    plt.title(titulo, fontsize=16)
    sns.axlabel(titulox, tituloy, fontsize=fontetamanho)
    plt.savefig(filename);


def graficos_jp(grupo):
    dic_horas = {"H4":"4h", "H8":"8h", "H12":"12h", "H24":"24h"}
    for i in grupo:
        for p in ["H4", "H8", "H12", "H24"]:
            nome = namestr(i)
            porextenso = _dic_continuo[nome]            
            if nome[-3:] == "amb": local = "Temperatura Ambiente"
            if nome[-3:] == "gel": local = "Sob Refrigeração"
            tity = porextenso+" | "+local+" ("+dic_horas[p]+")"
            titx = porextenso+" | "+local+" (0h)"
            titulomaior = ""
            fn = "["+nome+"]_[H0 x"+p+"].png"
            grafico_j([i["H0"],i[p]], titulox=titx, tituloy=tity, 
                      titulo = titulomaior, filename=fn, tamanho=10)

def graficos_lp(grupo):
    dic_horas = {"H4":"4h", "H8":"8h", "H12":"12h", "H24":"24h"}
    for i in grupo:
        for p in ["H4", "H8", "H12", "H24"]:
            nome = namestr(i)
            porextenso = _dic_discreto[nome]            
            if nome[-3:] == "amb": local = "Temperatura Ambiente"
            if nome[-3:] == "gel": local = "Sob Refrigeração"
            tity = porextenso+" | "+local+" ("+dic_horas[p]+")"
            titx = porextenso+" | "+local+" (0h)"
            titulomaior = ""
            fn = "["+nome+"]_[H0 x"+p+"].png"
            grafico_l2([i["H0"],i[p]], titulox=titx, tituloy=tity, 
                      titulo = titulomaior, filename=fn, tamanho=10)

grupoo = [ph_amb]

#graficos_lp(_grupo_discreto1)

#grafico_l([ph_amb["H0"], ph_amb["H24"]], titulox = "Temperatura Ambiente (0h)", 
#          tituloy = "Temperatura Ambiente (24h)", titulo="pH", filename = "")
# "[AMO]_[GELxAMB]_[24x24].png" [0,4], [0,4],



#graficos_jp(_grupo_continuo)

################################################################################################

def meu_applymap(dataframe, dicionario):
    fatia1, fatia2 = [0,1,2], [3, 4,5,6,7]
    df1, df2 = dataframe[fatia1], dataframe[fatia2]
    df3 = concat([df1, df2.applymap(lambda x: dicionario[x])], axis = 1)    
    return(df3)    

def mycontingency(par, neg):
    s1, s2 = np.array(par[0]), np.array(par[1])
    cc, cd, dc, dd = 0,0,0,0
    if len(s1) != len(s2): return("erro")
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            if s1[i] == neg: dd += 1
            elif s1[i] != neg: cc += 1
        elif s1[i] != s2[i]:
            if s1[i] != neg: cd += 1
            elif s1[i] == neg: dc += 1
    return(np.array([[cc,cd],[dc,dd]]))

def checar_normalidade():
    lista = [rbc_amb, rbc_gel, muc_amb, muc_gel, caoxd_amb, caoxd_gel, hya_amb, hya_gel, bac_amb, bac_gel, 
             pat_amb, pat_gel, wbc_amb, wbc_gel, epi_amb, epi_gel, tri_amb, tri_gel, uri_amb, uri_gel, 
             yea_amb, yea_gel, amo_amb, amo_gel]
    for i in lista:
        p = ""        
        ku, pv = stats.normaltest(i["H0"].map(float))
        if pv > 0.05: p = "***"
        print(list(Series(i["EXAME"]))[0], "", list(Series(i["LOCAL"]))[0],"| Curtose:",ku,"; Valor de p:",pv, p)

################################################################################################

def checarmcnemar1(t="H24"):
    print()
    print(__l)
    print()
    print("Avaliação de McNemar",t,"(GEL) x",t,"(AMB) para os diversos exames")    
    print()
    print(__l)
    for i in a_indice_cruzes_pares:
        p, p1 = i[0], ""
        k = [i[0][t], i[1][t]]
        mc = mcnemar(mycontingency(k, "neg"))
        if mc[1] < 0.05: p1 = "***"
        print("RESULTADOS PARA ", list(Series(p["EXAME"]))[0], ":", mc[0],"(X²); ",mc[1],"(valor de p)", p1)
    print(__l)

def checarmcnemar2(t="H24"):
    print()
    print(__l)
    print()
    print("Avaliação de McNemar H0 x",t,"para os diversos exames")    
    print()
    print(__l)
    for i in a_indice_cruzes_pares:        
        p, p1, p2 = i[0], "", ""
        k = [i[0]["H0"], i[0][t]]
        l = [i[1]["H0"], i[1][t]]
        mc1 = mcnemar(mycontingency(k, "neg"))        
        mc2 = mcnemar(mycontingency(l, "neg"))
        if mc1[1] < 0.05: p1 = "***"
        if mc2[1] < 0.05: p2 = "***"
        print("RESULTADOS PARA", list(Series(p["EXAME"]))[0], "(AMB):", 
                                              mc1[0],"(X²); ",mc1[1],"(valor de p)", p1)
        print("RESULTADOS PARA", list(Series(p["EXAME"]))[0], "(GEL):",
                                              mc2[0],"(X²); ",mc2[1],"(valor de p)", p2)
    print(__l)


################################################################################################

def checarkappa1(t="H24"):
    print()
    print(__l)
    print()
    print("Avaliação de Kappa",t,"(GEL) x",t,"(AMB) para os diversos exames")    
    print()
    for i in a_indice_cruzes_pares:
        print(__l)
        p, p1 = i[0], ""
        k = [i[0][t], i[1][t]]
        cokappa = cohens_kappa(mycontingency(k, "neg"))
        if cokappa.pvalue_two_sided < 0.05: p1 = "(OBS: ESTE TESTE TEVE p < 0.05)"
        print("RESULTADOS PARA ", list(Series(p["EXAME"]))[0], ":", p1)
        print()
        print(cokappa)
    print(__l)

def checarkappa2(t="H24"):
    print()
    print(__l)
    print()
    print("Avaliação de Kappa H0 x",t,"para os diversos exames")    
    print()
    for i in a_indice_cruzes_pares:
        print(__l)
        p = i[0]
        k = [i[0]["H0"], i[0][t]]
        l = [i[1]["H0"], i[1][t]]
        print("RESULTADOS PARA ", list(Series(p["EXAME"]))[0], " EM TEMPERATURA AMBIENTE (AMB):")
        print(cohens_kappa(mycontingency(k, "neg")))
        print(__l)
        print("RESULTADOS PARA ", list(Series(p["EXAME"]))[0], " SOB REFRIGERAÇÃO (GEL):")
        print(cohens_kappa(mycontingency(l, "neg")))
    print(__l)
    
def checarkappa_neu(t="H24"):
    print()
    print(__l)
    print()
    print("Avaliação de Kappa H0 x",t,"para os diversos exames")    
    print()
    for i in a_indice_cruzes_pares:
        print(__l)
        p = i[0]
        k = [i[0]["H0"], i[0][t]]
        l = [i[1]["H0"], i[1][t]]
        p11, p12, p21, p22 = "","","",""
        amb, gel = cohens_kappa(mycontingency(k, "neg")), cohens_kappa(mycontingency(l, "neg")) 
        if amb.pvalue_one_sided > 0.05: p11 = "***"
        if amb.pvalue_two_sided > 0.05: p12 = "***"
        if gel.pvalue_one_sided > 0.05: p21 = "***"
        if gel.pvalue_two_sided > 0.05: p22 = "***"
        print("RESULTADOS PARA ", list(Series(p["EXAME"]))[0], " EM TEMPERATURA AMBIENTE (AMB):")
        print("Kappa:",amb.kappa,"; Valor de p:",amb.pvalue_one_sided,p11,p12)
        #print(__l)
        print()
        print("RESULTADOS PARA ", list(Series(p["EXAME"]))[0], " SOB REFRIGERAÇÃO (GEL):")
        print("Kappa:",gel.kappa,"; Valor de p:",gel.pvalue_one_sided,p21,p22)
    print(__l)
    
def checarkappa_reto(t=["H4", "H8", "H12", "H24"]):
    print()
    print(__l)
    print()
    print("            Relatório Kappa linear")    
    print()
    for i in a_indice_cruzes_pares:
        for v in t:
            print(__l)
            p = i[0]
            k = [i[0]["H0"], i[0][v]]
            l = [i[1]["H0"], i[1][v]]
            p11, p12, p21, p22 = "","","",""
            amb, gel = cohens_kappa(mycontingency(k, "neg")), cohens_kappa(mycontingency(l, "neg")) 
            if amb.pvalue_one_sided > 0.05: p11 = "***"
            if amb.pvalue_two_sided > 0.05: p12 = "***"
            if gel.pvalue_one_sided > 0.05: p21 = "***"
            if gel.pvalue_two_sided > 0.05: p22 = "***"
            print("RESULTADOS PARA ", list(Series(p["EXAME"]))[0], " EM TEMPERATURA AMBIENTE (AMB), EM,",v,":")
            print("Kappa:",amb.kappa,"; Valor de p:",amb.pvalue_one_sided,p11,p12)
            #print(__l)
            print()
            print("RESULTADOS PARA ", list(Series(p["EXAME"]))[0], " SOB REFRIGERAÇÃO (GEL), EM,",v,":")
            print("Kappa:",gel.kappa,"; Valor de p:",gel.pvalue_one_sided,p21,p22)
    print(__l)

def checarkappa_csv_cis():
    t = ["H0", "H4", "H8", "H12", "H24"]
    relatorio = csv.writer(open("./resultados_kappa_cis.csv", 'w'))
    relatorio.writerow(["", "H0", "H4", "H8", "H12", "H24"])
    for i in a_indice_cruzes:
        loc, exa = list(i["LOCAL"])[0], list(i["EXAME"])[0]
        abertura = exa+" "+loc+" | H0"
        novalinha = [abertura]
        for v in t:
            k = [i["H0"], i[v]]
            novalinha.append(cohens_kappa(mycontingency(k, "neg")).kappa)
        relatorio.writerow(novalinha)

dfcontmelt2 = pd.read_csv("./posneg_sed.csv")

def checarkappa_csv_cis2(df=dfcontmelt2):
    t = ["H0", "H4", "H8", "H12", "H24"]
    relatorio = csv.writer(open("./resultados_kappa_cis2.csv", 'w'))
    relatorio.writerow(["", "H0", "H4", "H8", "H12", "H24"])
    for i in df:
        loc, exa = list(i["LOCAL"])[0], list(i["EXAME"])[0]
        abertura = exa+" "+loc+" | H0"
        novalinha = [abertura]
        for v in t:
            k = [i["H0"], i[v]]
            novalinha.append(cohens_kappa(mycontingency(k, "neg")).kappa)
        relatorio.writerow(novalinha)



def checarspearman_csv_cis():
    t = ["H0", "H4", "H8", "H12", "H24"]
    relatorio = csv.writer(open("./resultados_spearman_cis.csv", 'w'))
    relatorio.writerow(["", "H0", "H4", "H8", "H12", "H24"])

    lista = [rbc_amb, rbc_gel, muc_amb, muc_gel, caoxd_amb, caoxd_gel, hya_amb, hya_gel, bac_amb, bac_gel, 
             pat_amb, pat_gel, wbc_amb, wbc_gel, epi_amb, epi_gel, tri_amb, tri_gel, uri_amb, uri_gel, 
             yea_amb, yea_gel, amo_amb, amo_gel, sg_amb, sg_gel, ph_amb, ph_gel] #mudei aqui
    for i in lista:
        correlraw = checarspearman(i)
        loc, exa = list(i["LOCAL"])[0], list(i["EXAME"])[0]
        abertura = exa+" "+loc+" | H0"
        novalinha = [abertura]
        for v in correlraw:
            novalinha.append(v[0])
        relatorio.writerow(novalinha)
        



'''
def checarkappa_csv_trans():
    t = ["H0", "H4", "H8", "H12", "H24"]
    relatorio = csv.writer(open("/home/fred/Dropbox/CC/DBs/URI/SOURCE/Relatórios/resultados_cis.csv", 'w'))
    relatorio.writerow(["", "H0", "H4", "H8", "H12", "H24"])
    for i in a_indice_cruzes_pares:
        loc, exa = list(i["LOCAL"])[0], list(i["EXAME"])[0]
        abertura = exa+" "+loc+" | H0"
        novalinha = [abertura]
        for v in t:
            k = [i["H0"], i[v]]
            novalinha.append(cohens_kappa(mycontingency(k, "neg")).kappa)
        relatorio.writerow(novalinha)
'''

################################################################################################

def checarspearman(exame):
    relatorio = []
##    print()    
##    print("RESULTADOS DE ", list(Series(exame["EXAME"]))[0], "", list(Series(exame["LOCAL"]))[0], ":")
    for i in ["H4", "H8", "H12", "H24"]:
        p = ""        
        resultado = spearmanr(exame["H0"].map(float), exame[i].map(float))
        relatorio.append(resultado)
        if resultado[1] > 0.05: p = "***"        
##        print("Entre H0 e", i,":", resultado[0], "(Spearman r), e ", resultado[1],"(valor de p)", p)
##    print(___l)
    return(relatorio)


def checarspearman_paralelo_(par):
    relatorio = []    
    for ex in par:
        exame1, exame2 = ex[0], ex[1]
        print()    
        print("RESULTADOS DE", list(Series(exame1["EXAME"]))[0],":")        
        for i in ["H4", "H8", "H12", "H24"]:
            p = ""        
            resultado = spearmanr(exame1[i], exame2[i])
            relatorio.append(resultado)
            if resultado[1] < 0.05: p = "***"        
            print("Entre",i,"e", i,":", resultado[0], "(Spearman r), e ", resultado[1],"(valor de p)", p)
    print(___l)
    return(relatorio)

def checarspearman_paralelo():
    lista = [[rbc_gel, rbc_amb], [muc_amb, muc_gel], [caoxd_amb, caoxd_gel], [hya_amb, hya_gel], [bac_amb, bac_gel], 
         [pat_amb, pat_gel], [wbc_amb, wbc_gel], [epi_amb, epi_gel], [tri_amb, tri_gel], [uri_amb, uri_gel], 
         [yea_amb, yea_gel], [amo_amb, amo_gel]]
    relatorio = []    
    print(___l)
    print()
    print("             RELATÓRIO DE CORRELAÇÕES (SPEARMAN) PARALELO")
    print()
    print(___l)
    for ex in lista:
        exame1, exame2 = ex[0], ex[1]
        print()    
        print("RESULTADOS DE", list(Series(exame1["EXAME"]))[0],":")        
        for i in ["H4", "H8", "H12", "H24"]:
            p = ""        
            resultado = spearmanr(np.array(exame1[i].map(float)), np.array(exame2[i].map(float)))
            relatorio.append(resultado)
            if resultado[1] > 0.05: p = "***"        
            print("Entre",i,"e", i,":", resultado[0], "(Spearman ρ), e ", resultado[1],"(valor de p)", p)
    print(___l)
    return(relatorio)

def checarspearman_todos():
    lista = [rbc_amb, rbc_gel, muc_amb, muc_gel, caoxd_amb, caoxd_gel, hya_amb, hya_gel, bac_amb, bac_gel, 
             pat_amb, pat_gel, wbc_amb, wbc_gel, epi_amb, epi_gel, tri_amb, tri_gel, uri_amb, uri_gel, 
             yea_amb, yea_gel, amo_amb, amo_gel]
    relatorio = []
##    print(___l)
##    print()
##    print("                     RELATÓRIO DE CORRELAÇÕES (SPEARMAN)")
##    print()
##    print(___l)
    for i in lista:
        checarspearman(i)


def relatorios():
    checarspearman_csv_cis()
    checarkappa_csv_cis()

'''
################################################################################################
                                        FÍSICO-QUÍMICA
################################################################################################
'''
a_indice_cruzes = [leu_amb, leu_gel, nit_amb, nit_gel, pro_amb, pro_gel, ket_amb, ket_gel, bil_amb, bil_gel, 
                   bld_amb, bld_gel, glu_amb, glu_gel, ubg_amb, ubg_gel]

a_indice_cruzes_pares = [[leu_amb, leu_gel], [nit_amb, nit_gel], [pro_amb, pro_gel],
           [ket_amb, ket_gel], [bil_amb, bil_gel], [bld_amb, bld_gel], [glu_amb, glu_gel], [ubg_amb, ubg_gel]]
 
a_indice_fq = [[sg_amb, sg_gel], [ph_amb, ph_gel], [leu_amb, leu_gel], [nit_amb, nit_gel], [pro_amb, pro_gel],
           [glu_amb, glu_gel], [ket_amb, ket_gel], [ubg_amb, ubg_gel], [bil_amb, bil_gel], [bld_amb, bld_gel]]

           

# checarkappa1()


'''
################################################################################################
                                          SEDIMENTO
################################################################################################
'''





'''
grafico_j([wbc_amb["H0"], wbc_amb["H4"]], titulox = "Temperatura Ambiente (0h)", 
          tituloy = "Temperatura Ambiente (4h)", filename = "wbc_amb_0x4.jpg", tamanho=10)
          #[0,15], [0,15],
          #titulox = "Refrigerada (24h)", tituloy = "Temperatura Ambiente (24h)",
'''

'''
################################################################################################
                                           OUTROS
################################################################################################
'''

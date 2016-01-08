# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 10:51:53 2015

@author: joaofred
"""

import os
from subprocess import call
import re
import pandas as pd
#import numpy as np
#import scipy as sp
#import statsmodels as sm
#import random as ra
#import seaborn as sns
#import matplotlib.pyplot as plt
#import csv
#from pandas import DataFrame, Series, qcut, cut, crosstab, concat



from os import listdir
from os.path import isfile, join


def tess():
    onlyfiles = [ f for f in listdir("./OCR/") if isfile(join("./OCR/",f)) ]
    onlyjpgs = [p for p in onlyfiles if p[-4:]==".png"]
    for i in onlyjpgs:
        call(['tesseract', "-l", "eng", "./OCR/"+i, "./OCR/"+i])
        print(":: REALIZADO:",i)

def juntar():
    davez= ["-H00-AMB","-H04-AMB","-H04-GEL","-H08-AMB","-H08-GEL","-H12-AMB","-H12-GEL","-H24-AMB","-H24-GEL"]
    davez_ALTERADO = ["-H00-AMB","-H04-AMB","-H04-AMB","-H04-GEL","-H08-AMB","-H08-GEL","-H12-AMB","-H12-GEL","-H24-AMB","-H24-GEL"]
    call(['touch', './OCR/output'])
    onlyfiles = [ f for f in listdir("./OCR/") if isfile(join("./OCR/",f)) ]
    onlytxts = [p for p in onlyfiles if p[-4:]==".txt"]
    onlytxts = sorted(onlytxts)
    #print(onlytxts)
    textao = ''
    c = 0
    for i in onlytxts:
        textao += "-"*150+davez[c]+"\n"      
        texto = open("./OCR/"+i).read()
        textao += texto
        c+=1         
    output = open('./OCR/output', 'a')
    output.write(textao)
    print(":: REALIZADO: output")

    
#os.system
    
#-------------------------------------------------------------------------------------------------------------------------------
    


def clean():
    global pct
    x = 0
    while x < len(pct):
        
        pct[x] = pct[x].replace("EP1", "EPI")
        pct[x] = pct[x].replace("EP!", "EPI")
        pct[x] = pct[x].replace("TR1", "TRI")
        pct[x] = pct[x].replace("TR!", "TRI")
        pct[x] = pct[x].replace("WC", "WBC")
        pct[x] = pct[x].replace("EP!", "EPI")
        pct[x] = pct[x].replace("RE3C", "RBC")
        pct[x] = pct[x].replace("LEM", "LEU")
        pct[x] = pct[x].replace("BlL", "BIL")
        pct[x] = pct[x].replace("YER", "YEA")
        pct[x] = pct[x].replace("8A8", "BAC")
        pct[x] = pct[x].replace("mus", "MUC")
        pct[x] = pct[x].replace("EPE", "EPI")
        pct[x] = pct[x].replace("W06", "WBC")
        pct[x] = pct[x].replace("TRl", "TRI")
        pct[x] = pct[x].replace("URl", "URI")
        pct[x] = pct[x].replace("6A8", "BAC")
        pct[x] = pct[x].replace("M06", "MUC")
        pct[x] = pct[x].replace("ER}", "LEU")
        pct[x] = pct[x].replace("W30", "WBC")
        pct[x] = pct[x].replace("5%", "EPI")
        pct[x] = pct[x].replace("MSG", "MUC")
        pct[x] = pct[x].replace("8A6", "BAC")
        pct[x] = pct[x].replace("6A6", "BAC")
        pct[x] = pct[x].replace("NLL", "NIT")
        pct[x] = pct[x].replace("LEE", "LEU")
        pct[x] = pct[x].replace("M00", "MUC")
        pct[x] = pct[x].replace("W8C", "WBC")
        pct[x] = pct[x].replace("MQC", "MUC")
        pct[x] = pct[x].replace("Bll.", "BIL")
        pct[x] = pct[x].replace("PRU", "PRO")
        pct[x] = pct[x].replace("E??", "EPI")
        pct[x] = pct[x].replace("WEEK", "MUC")
        pct[x] = pct[x].replace("EPS", "EPI")
        pct[x] = pct[x].replace("WW?", "WBC")
        pct[x] = pct[x].replace("WWC", "WBC")
        pct[x] = pct[x].replace("MT", "NIT")
        pct[x] = pct[x].replace("UR1", "URI")
        pct[x] = pct[x].replace("533%", "EPI")
        pct[x] = pct[x].replace("WES", "WBC")
        pct[x] = pct[x].replace("533%", "EPI")
        pct[x] = pct[x].replace("3A0", "BAC")
        pct[x] = pct[x].replace("BAG", "BAC")
        pct[x] = pct[x].replace("EM ", "EPI")
        pct[x] = pct[x].replace("LEO", "LEU")
        pct[x] = pct[x].replace("13%", "BAC")
        pct[x] = pct[x].replace("EPt", "EPI")
        pct[x] = pct[x].replace("MUG", "MUC")
        pct[x] = pct[x].replace("W88", "WBC")
        pct[x] = pct[x].replace("W8C", "WBC")
        pct[x] = pct[x].replace("W66", "WBC")
        pct[x] = pct[x].replace("W3C", "WBC")
        pct[x] = pct[x].replace("HYR", "HYA")
        pct[x] = pct[x].replace("RYA", "HYA")
        pct[x] = pct[x].replace("HYR", "HYA")
        pct[x] = pct[x].replace("Rat", "RBC")
        pct[x] = pct[x].replace("HYR", "HYA")
        pct[x] = pct[x].replace("EPl", "EPI")
        pct[x] = pct[x].replace("nonn", "norm")
        pct[x] = pct[x].replace("nonm", "norm")
        pct[x] = pct[x].replace("nomn", "norm")
        pct[x] = pct[x].replace("norn", "norm")
        '''
        pct[x] = pct[x].replace("l", "1")
'''
        pct[x] = pct[x].replace("—", "-")
        pct[x] = pct[x].replace(".Cand", ".CaOxd")        
        pct[x] = pct[x].replace(",", ".")
        x += 1

def tj():
    tess()
    juntar()
#tess()
#juntar()    

paciente = open('./OCR/output', 'r')
pct = paciente.readlines()
dataframe = pd.read_csv("input.csv")
clean()


def parser(txt = pct, df = dataframe, chave = 299):
    dot = 0
    for i in txt:
        if i[0:100] == ("-"*100):
            hora, lugar = i[151:154], i[155:158]
            
        if i.replace(" ", "")[0:3]=="BIL":
            exame = "BIL"
            
            ilimpo = i.replace(" ", "#")[3:90]
            valor = extraiprimo(ilimpo)           
#            valor = i.replace(" ", "")[3:6]
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1

        if i.replace(" ", "")[0:3]=="UBG":
            exame = "UBG"
            ilimpo = i.replace(" ", "#")[3:90]
            valor = extraiprimo(ilimpo)           
#            valor = i.replace(" ", "")[3:7]
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1

        if i.replace(" ", "")[0:3]=="KET":
            exame = "KET"
            ilimpo = i.replace(" ", "#")[3:90]
            valor = extraiprimo(ilimpo)           
#            valor = i.replace(" ", "")[3:6]
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1

        if i.replace(" ", "")[0:3]=="GLU":
            exame = "GLU"
            ilimpo = i.replace(" ", "#")[3:90]
            valor = extraiprimo(ilimpo)           
#            valor = i.replace(" ", "")[3:7]
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1

        if i.replace(" ", "")[0:3]=="PRO":
            exame = "PRO"
            ilimpo = i.replace(" ", "#")[3:90]
            valor = extraiprimo(ilimpo)
            #valor = i.replace(" ", "")[3:6]
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1

        if i.replace(" ", "")[0:3]=="BLD":
            exame = "BLD"
            ilimpo = i.replace(" ", "#")[3:90]
            valor = extraiprimo(ilimpo)
#            valor = i.replace(" ", "")[3:6]
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1
        
        if i.replace(" ", "")[0:2]=="PH":
            exame = "PH"
            valor = i.replace(" ", "")[2:3]
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1

        if i.replace(" ", "")[0:3]=="NIT":
            exame = "NIT"
            ilimpo = i.replace(" ", "#")[3:90]
            valor = extraiprimo(ilimpo)
            #valor = i.replace(" ", "")[3:6]
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor        
                dot += 1
            dot += 1

        if i.replace(" ", "")[0:3]=="LEU":
            
            exame = "LEU"
            if i.replace(" ", "")[3] == "n":
                valor = i.replace(" ", "")[3:6]
            else: 
                ilimpo = re.sub("[^0-9,. ]", "", i)
                valor = extraiprimo(ilimpo.replace(" ", "#"))            
            
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor        
                dot += 1
            dot += 1
        
        #-----------------------------------------------------------
        
        if i.replace(" ", "")[0:3]=="SG:":
            exame = "SG"
            valor = i.replace(" ", "")[3:9]
            valor = valor.replace(".","")
            valor = float(valor)
            #valor = float(valor)
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1

        #-----------------------------------------------------------
                
        if i.replace(" ", "")[0:3]=="RBC":
            exame = "RBC"
            ilimpo = re.sub("[^0-9,. ]", "", i)[1::]
            ilimpo = ilimpo.replace(" ", "#")  
            valor = float(extraiprimo(ilimpo))
            valor = extraiprimo(ilimpo)
            #ilimpo = re.sub("[^0-9,.]", "", i)
            #valor = float(ilimpo[0:4])
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1
                                
        if i.replace(" ", "")[0:3]=="WBC":
            
            exame = "WBC"
            ilimpo = re.sub("[^0-9,. ]", "", i)[1::]
          
            ilimpo = ilimpo.replace(" ", "#")  
            
            valor = float(extraiprimo(ilimpo))
            
            #ilimpo = re.sub("[^0-9,.]", "", i)
            #valor = float(ilimpo[0:4])
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1
                
        if i.replace(" ", "")[0:3]==".Ca":
            exame = "CAOXD"
            ilimpo = re.sub("[^0-9,. ]", "", i)[1::]
            ilimpo = ilimpo.replace(" ", "#")  
            valor = float(extraiprimo(ilimpo))
            #ilimpo = re.sub("[^0-9,.]", "", i)[1::]
            #valor = float(ilimpo[0:4])
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1
                
        if i.replace(" ", "")[0:3]==".TR":
            exame = "TRI"
            ilimpo = re.sub("[^0-9,. ]", "", i)[1::]
            ilimpo = ilimpo.replace(" ", "#")  
            valor = float(extraiprimo(ilimpo))
            #ilimpo = re.sub("[^0-9,.]", "", i)[1::]
            #valor = float(ilimpo[0:4])
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1
                
        if i.replace(" ", "")[0:3]==".UR":
            exame = "URI"
            ilimpo = re.sub("[^0-9,. ]", "", i)[1::]
            ilimpo = ilimpo.replace(" ", "#")  
            valor = float(extraiprimo(ilimpo))
            #ilimpo = re.sub("[^0-9,.]", "", i)[1::]
            #valor = float(ilimpo[0:4])
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1

        if i.replace(" ", "")[0:3]==".U-":
            exame = "AMO"
            ilimpo = re.sub("[^0-9,. ]", "", i)[1::]
            ilimpo = ilimpo.replace(" ", "#")  
            valor = float(extraiprimo(ilimpo))
            #ilimpo = re.sub("[^0-9,.]", "", i)[1::]
            #valor = float(ilimpo[0:4])
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1

        if i.replace(" ", "")[0:3]=="HYA":
            exame = "HYA"
            #ilimpo = re.sub("[^0-9,. ]", "", i)
            #valor = float(extraiprimo(ilimpo.replace(" ", "#")))
            ilimpo = re.sub("[^0-9,.]", "", i)
            #valor = float(ilimpo[1:3])
            valor = ilimpo[1:3]
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1

        if i.replace(" ", "")[0:3]=="PAT":
            exame = "PAT"
            ilimpo = re.sub("[^0-9,. ]", "", i)
            valor = float(extraiprimo(ilimpo.replace(" ", "#")))
#            ilimpo = re.sub("[^0-9,.]", "", i)
#            valor = float(ilimpo[0:4])
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1


        if i.replace(" ", "")[0:3]=="EPI":
            exame = "EPI"
            ilimpo = re.sub("[^0-9,. ]", "", i)
            valor = float(extraiprimo(ilimpo.replace(" ", "#")))
#            ilimpo = re.sub("[^0-9,.]", "", i)
#            valor = float(ilimpo[0:3])
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1


        if i.replace(" ", "")[0:3]=="YEA":
            exame = "YEA"
            ilimpo = re.sub("[^0-9,. ]", "", i)
            valor = float(extraiprimo(ilimpo.replace(" ", "#")))            
#            ilimpo = re.sub("[^0-9,.]", "", i)
#            valor = float(ilimpo[0:3])
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1


        if i.replace(" ", "")[0:3]=="BAC":                        
            exame = "BAC"
            ilimpo = re.sub("[^0-9,. ]", "", i)
            valor = float(extraiprimo(ilimpo.replace(" ", "#")))
#            ilimpo = re.sub("[^0-9,.]", "", i)
#            valor = float(ilimpo[0:3])
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1

        if i.replace(" ", "")[0:3]=="MUC":
            exame = "MUC"
            ilimpo = re.sub("[^0-9,. ]", "", i)
            valor = float(extraiprimo(ilimpo.replace(" ", "#")))
            #ilimpo = re.sub("[^0-9,.]", "", i)
            #valor = float(ilimpo[0:3])
            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
            if hora == "H00": 
                df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor
                dot += 1
            dot += 1
    print(":: QUANTO FIZEMOS: ",(dot/220)*100,"%")
    return(dot)


def extraiprimo(sequencia):
    seqfin = ""
    reviravolta = False    
    for i in sequencia:
        if i != "#": 
            seqfin+=i
            reviravolta = True
        if reviravolta == True:
            if i == "#": break
    return(seqfin)



print("As funções são: tj() e parser()")




#parser()


#print(dott)
'''
call(['mv', './OCR/output', './OCR/output.old'])

#def tessextract():
    
    
    

'''
#tessextract()

#parser()
















'''
def parser2(txt = pct, df = dataframe, chave = 299):
    for i in txt:
        if i[0:100] == ("-"*100):
            hora, lugar = i[151:154], i[155:158]
            

        if i.replace(" ", "")[0:3]=="BAC":
            exame = "BAC"
            ilimpo = re.sub("[^0-9,. ]", "", i)
            valor = ilimpo.replace(" ", "#")
            print(extraiprimo(valor))
#            df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == lugar), hora] = valor
#            if hora == "H00": df.loc[(df["KEY"] == chave) & (df["EXAME"] == exame) & (df["LOCAL"] == "GEL"), hora] = valor

     



'''


'''
    for p in seqmed:
        if p == "#": print(seqfin)
        if p != "#":
            seqfin+=p
    return(seqfin)
'''

#print(extraiprimo("#####1111######32###"))




































                
                
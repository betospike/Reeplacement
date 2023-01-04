# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 18:37:30 2022

@author: amedi
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 13:18:32 2022

@author: amedi
"""


import glob
import os

def reemplazar(freq,freqA1,freqA2,freqA3,freqA4,freqN19,a,archivo_seleccionado,carpeta_guarda,archivo):
    caracter="R_"
    #input = open("MBA62741S_N600_N2500_1C_Relation.mos","rt")
    #input=open(r"C:\Users\amedi\Desktop\MBA62741S_N600_N2500_1C_Relation.mos","rt")
    
    input=open(archivo_seleccionado,"rt")
    output = open(carpeta_guarda+caracter+archivo,"wt")

    for line in input: 
        #Vamos checando linea por linea
    
        #replace the strings and write to output file
    
        output.write(line.replace(a,freq).replace(freq+"1C",freqA1).replace(freq+"2C",freqA2).replace("Dummy_Freq_N2500_1C",freqA1).replace("Dummy_Freq_N25001C",freqA1).replace("Dummy_Freq_N2500_2C",freqA2).replace("Dummy_Freq_N25002C",freqA2).replace("Dummy_Freq_N600",freq).replace("Dummy_Freq_n1900_1C",freqN19).replace(freq+"3C",freqA3).replace(freq+"4C",freqA4))
    

    input.close()

    output.close()
    
    

#archivo_seleccionado="C:/Users/amedi/Desktop/RELA_3/BA62741S_N600_N2500_Relations/MBA62741S_N600_N2500_2C_Relation.mos"

#carpeta_guarda="C:/Users/amedi/Desktop/RELA_3/BA62741S_N600_N2500_Relations/"

#archivo="MBA62741S_N600_N2500_2C_Relation.mos"

#freq="1269"
#freqA1="54445"
#freqA2="50735"

#a="DummyFreq"

#reemplazar(freq,freqA1,freqA2,a,archivo_seleccionado,carpeta_guarda,archivo)


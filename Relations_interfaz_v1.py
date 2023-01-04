# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:00:03 2022

@author: amedi
"""


import PySimpleGUI as sg

import glob
global archivo


from io import open
import re
import pandas as pd

from datetime import datetime
from datetime import date
from Reemplazar_v2 import reemplazar
from datetime import datetime
import os


   # In[1]: FUNCION RELATIONS


def Relation(folder,freq,freqA1,freqA2,freqA3,freqA4,freqN19):

    print(folder)
    
    print("N600=",freq)
    print("N251C=",freqA1)
    print("N252C=",freqA2)
    print("N253C=",freqA3)
    print("N254C=",freqA4)
    print("N254C=",freqA4)
    print("N19=",freqN19)

    
    
    sg.popup("Completed")
    
    
    
    t=""

    if freq==t:
        freq="DummyFreq"
    
    if freqA1==t:
        freqA1="DummyFreq1C"
        
    if freqA2==t:
        freqA2="DummyFreq2C"
    
    if freqA3==t:
        freqA3="DummyFreq3C"
        
    if freqA4==t:
        freqA4="DummyFreq4C"
        
    if freqN19==t:
        freqN19="DummyFreq1C"
        
    
    print("N600=",freq)
    print("N251C=",freqA1)
    print("N252C=",freqA2)
    print("N253C=",freqA3)
    print("N254C=",freqA4)
    print("N254C=",freqA4)
    print("N19=",freqN19)
    
    a="DummyFreq"
    
    
    ##PROGRAMA
    list_files=os.listdir(folder)


    #Contamos el numero de archivos
    contador=len(list_files)
    
    contador=int(contador)

    #for files_name in list_files:
    #   print(list_files)
       
    prueba=list_files[0]

    
       
    #AQUI VAMOS ENTRANDO A LAS CARPETAS INTERNAS"



    for i in range(contador): #Aqui vamos entrando a cada carpeta
        
        carpeta=folder + "/" + list_files[i] 
        
        
        list_files_3=os.listdir(carpeta) 
        
        contador2=len(list_files_3)
     
        j=0
        for j in range(contador2): #Aqui vamos seleccionando cada archivo dentro de la carpeta
            
            archivo=list_files_3[j]

            folder_o_archivo=archivo.endswith('.mos')
            LTE_RELATION=archivo.find("LTE_LTE") #Filtramos los archivos que sean relaciones de LTE_LTE
            N19_RELATION=archivo.find("LTE_N19") #Filtramos los archivos de relaciones N19
            N19_2_RELATION=archivo.find("N1900_N1900") #Filtramos los archivos de relaciones N19
            N19_3_RELATION=archivo.find("N1900_LTE")
           
                
                
                
            if folder_o_archivo == True and LTE_RELATION==-1:
                
                
                archivo_seleccionado=folder + "/" + list_files[i] + "/" + archivo
                carpeta_guarda=folder + "/" + list_files[i]+"/"
                
                if N19_RELATION>=0 or N19_2_RELATION>=0 or N19_3_RELATION>=0: #Si esta condicion se cumple y encunetra un archivo que sea de N19 remplaza el valor de frecuencia
                    
                    reemplazar(freqN19,freqN19,freqN19,freqN19,freqN19,freqN19,a,archivo_seleccionado,carpeta_guarda,archivo)
            
               
                    
                else:
                    
                    reemplazar(freq,freqA1,freqA2,freqA3,freqA4,freqN19,a,archivo_seleccionado,carpeta_guarda,archivo)
            
    
   # In[1]: INTERFAZ
   # In[1]: LOGIN PASSWORD

def login():
    sg.theme("LightBlue2")
    layout = [[sg.Text("Log In", size =(15, 1), font=40)],
            [sg.Text("Password", size =(15, 1), font=16),sg.InputText(key='-pwd-', password_char='*', font=16)],
            [sg.Button('Ok'),sg.Button('Cancel')]]

    window = sg.Window("Log In", layout)

    while True:
        event,values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Ok":
                if  values['-pwd-'] == 'Amdocs123#':
                    sg.popup("Welcome!")
                    
                    window.close()
                    
                    Interfaz()
                    break
                elif values['-pwd-'] != 'Amdocs123#':
                    sg.popup("Invalid login. Try again")

    window.close()
    

   # In[1]: INTERFAZ DEL PROGRAMA

def Interfaz():

    control_col=sg.Column([
        [sg.Text("Input file"),sg.Input(key='_FILES_'),sg.FolderBrowse(key='Browse')],
        [sg.Text("Enter N600 Ssbfreq"),sg.Input(key='_N600_')],
        [sg.Text("Enter N25 1C Ssbfreq"),sg.Input(key='_N251C_')],
        [sg.Text("Enter N25 2C Ssbfreq"),sg.Input(key='_N252C_')],
        [sg.Text("Enter N25 3C Ssbfreq"),sg.Input(key='_N253C_')],
        [sg.Text("Enter N25 4C Ssbfreq"),sg.Input(key='_N254C_')],
        [sg.Text("Enter N19 Ssbfreq"),sg.Input(key='_N19_')],
        [sg.Button('START'),sg.Button('Cancel')],
        [sg.Exit()]
        
        ])
    

    
    
    image_col=sg.Column([[sg.Text("WELCOME TO THE RELATIONS PROGRAM")]])
    
    
    layout=[[control_col,image_col]]
    
    
    
    #print(values['_FILES_'].split(';'))
    
    window = sg.Window("RELATIONS PROGRAM", layout)
    
    while True:
        
        event,values=window.read()
        
        
        if event=='Exit' or  event==sg.WIN_CLOSED:
            break
        
        if event:
            
            archivos=values['_FILES_']
           
    

            
        if event=="START":
            
            folder=values['_FILES_']
            
            freq=values['_N600_']
            freqA1=values['_N251C_']
            freqA2=values['_N252C_']
            freqA3=values['_N253C_']
            freqA4=values['_N254C_']
            freqN19=values['_N19_']
            
            Relation(folder,freq,freqA1,freqA2,freqA3,freqA4,freqN19)
            
        sg.popup("Completed")
        
    window.close()
    

login()



    
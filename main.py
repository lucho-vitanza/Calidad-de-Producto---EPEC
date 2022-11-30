#-----------------LIBRERIAS---------------------------

import pandas as pd

import math 


#------------------MANIPULACION TABLA-----------------

#----LECTURA CSV------------------------

df = pd.read_csv('bruta_mayor40.csv', delimiter = "," )

RCPT1 = pd.DataFrame()



#print(df.shape)
#print(df.info)

#------RENOMBRADO DE COLUMNAS----------

df.rename(columns={"Servicio":"suministro", "Distrito":"distrito", "Medidor":"medidor"},inplace = True)



#-----CONVERSION DE TIPO DE DATO-------

df = df.astype("Int32")

print(df.dtypes)

#--------SACAR LOS MUERTOS------

df = df.dropna() #Elimina los NaN
# df = df.fillna(0) #rellena los que no tienen datos con 0



#--------declaracion de variables------------------

lista_sum_sorteados = []
lista_med_sorteados = []


op = 0

tamanno_muestra = 0



#---------------PROCESO --------------------
def proceso(Cantsort,lista_med,lista_sum): 
  
  i = 0
  lista_num_sorteados = []
  lista_med_sorteados = []
  lista_sum_sorteados = []
  
  
  while i < Cantsort: 
      
    i += 1

    print("Ingrese " + str(i) + " numero sorteado : ") 
        
    num_sorteado = int(input())


    if num_sorteado <= len(lista_med):
    
      lista_num_sorteados.append(num_sorteado)
        
      lista_med_sorteados.append(lista_med[num_sorteado - 1])
      
      lista_sum_sorteados.append(lista_sum[num_sorteado - 1])
  
      RCPT1 = pd.DataFrame({'Suministros' : lista_sum_sorteados, 'Medidores' : lista_med_sorteados}) 
      
      

      
      
    else:

      print("No te haga el vivo")
      
      i -= 1
    
      
  
  
      
  
  
  return RCPT1

  

  
  


#-------------------MENU---------------------


menu = """

Menu
1-Zona A
2-Zona B
3-Zona C
4-Zona D
5-Zona E
6-Zona F
7-Zona G
8-Zona H
9-Zona I
10-Exportar RCPT1
11-Exportar RCPT1 de ultima zona sorteada
12-Salir

"""

#---------------Iniciador----------------------
pop = True

while pop == True:
  print(menu)
  op = int(input("Elegi la zona a sortear: "))

  
  
  
  
  
  
  
  
  
#---------------------ZONA A----------------------------
  
  if op == 1:

    
    RCPT1t = pd.DataFrame()
    RCPT1a = pd.DataFrame()
  
    print( "*" * 10 + "--------ZONA A----------" + "*" * 10)

    print("Especificar tamaño de la muestra en %: ") 
    tamanno_muestra = float(input()) / 100
    
    condicion = df[ "distrito" ] == 1 
    
    dfA = df[ condicion ]
    
    Cantsort = int(math.ceil(len(dfA) * tamanno_muestra))
    
    lista_med = list(dfA["medidor"])
    
    lista_sum = list(dfA["suministro"])
    
    print("La cantidad de numeros a sortear son " + str(Cantsort) + " de " + str(len(lista_med)))

    
    
    RCPT1a = proceso(Cantsort,lista_med,lista_sum)
    
    RCPT1 = RCPT1a
    
    RCPT1a["zona"] = "A"

  
    
    RCPT1t = pd.concat([RCPT1t,RCPT1a])
    
    print(RCPT1t)
    
    
  #---------------Zona B--------------------
    
  elif op == 2:

    RCPT1b = pd.DataFrame()
    
    print( "*" * 15 + "---------ZONA B----------" + "*" * 15)
    
    
    dfB = df[ (df["distrito" ] == 2) | (df["distrito" ] == 3) | (df["distrito" ] == 4) | (df["distrito" ] == 5) | (df["distrito" ] == 6) | (df["distrito" ] == 7) ]

    print("Especificar tamaño de la muestra en %: ") 
    tamanno_muestra = float(input()) / 100
    
    Cantsort = int(math.ceil(len(dfB) * tamanno_muestra))
    
    lista_med = list(dfB["medidor"])
    
    lista_sum = list(dfB["suministro"])
    
    print("La cantidad de numeros a sortear son " + str(Cantsort) + " de " + str(len(lista_med)))
  
    RCPT1b = proceso(Cantsort,lista_med,lista_sum)
    
    RCPT1 = RCPT1b
    
    RCPT1b["zona"] = "B"
    
    RCPT1t = pd.concat([RCPT1t,RCPT1b])

    print(RCPT1t)
  #---------------Zona C--------------------
    
  elif op == 3:


    RCPT1c = pd.DataFrame()
    
    print( "*" * 15 + "--------ZONA C----------" + "*" * 15)
    
    dfC = df[ (df["distrito" ] == 8) | (df["distrito" ] == 9) | (df["distrito" ] == 10) | (df["distrito" ] == 11) | (df["distrito" ] == 12) | (df["distrito" ] == 13) | (df["distrito" ] == 14) | (df["distrito" ] == 15) | (df["distrito" ] == 16) | (df["distrito" ] == 17)  ]
    
    print("Especificar tamaño de la muestra en (%): ") 
    tamanno_muestra = float(input()) / 100
    
       
    Cantsort = int(math.ceil(len(dfC) * tamanno_muestra))
    
    lista_med = list(dfC["medidor"])
    
    lista_sum = list(dfC["suministro"])
    
    print("La cantidad de numeros a sortear son " + str(Cantsort) + " de " + str(len(lista_med)))
  
    RCPT1c = proceso(Cantsort,lista_med,lista_sum)

    RCPT1 = RCPT1c
    
    RCPT1c["zona"] = "C"
    
    RCPT1t = pd.concat([RCPT1t,RCPT1c])

    print(RCPT1t)

#---------------Zona D--------------------------------------------------------------
  elif op == 4:

    RCPT1d = pd.DataFrame()
    
    print( "*" * 15 + "--------ZONA D----------" + "*" * 15)
    
    dfD = df[ (df["distrito" ] == 18) | (df["distrito" ] == 19) | (df["distrito" ] == 20) | (df["distrito" ] == 21) ]
    
    print("Especificar tamaño de la muestra en (%): ") 
    tamanno_muestra = float(input()) / 100
    
       
    Cantsort = int(math.ceil(len(dfD) * tamanno_muestra))
    
    lista_med = list(dfD["medidor"])
    
    lista_sum = list(dfD["suministro"])
    
    print("La cantidad de numeros a sortear son " + str(Cantsort) + " de " + str(len(lista_med)))
  
    RCPT1d = proceso(Cantsort,lista_med,lista_sum)
    
    RCPT1 = RCPT1d
    
    RCPT1d["zona"] = "D"
    
    RCPT1t = pd.concat([RCPT1t,RCPT1d])

    print(RCPT1t)

#---------------Zona H--------------------------------------------------------------
  elif op == 5:

    RCPT1e = pd.DataFrame()
    
    print( "*" * 15 + "--------ZONA E----------" + "*" * 15)
    
    dfE = df[ (df["distrito" ] == 22) | (df["distrito" ] == 23) | (df["distrito" ] == 24) | (df["distrito" ] == 25) | (df["distrito" ] == 26)| (df["distrito" ] == 27)]
    
    print("Especificar tamaño de la muestra en (%): ") 
    tamanno_muestra = float(input()) / 100
    
       
    Cantsort = int(math.ceil(len(dfE) * tamanno_muestra))
    
    lista_med = list(dfE["medidor"])
    
    lista_sum = list(dfE["suministro"])
    
    print("La cantidad de numeros a sortear son " + str(Cantsort) + " de " + str(len(lista_med)))
  
    RCPT1e = proceso(Cantsort,lista_med,lista_sum)
    
    RCPT1 = RCPT1e
    
    RCPT1e["zona"] = "E"
    
    RCPT1t = pd.concat([RCPT1t,RCPT1e])

    print(RCPT1t)
    
#---------------Zona I--------------------------------------------------------------

  elif op == 6:


    RCPT1f = pd.DataFrame()
    
    print( "*" * 15 + "--------ZONA F----------" + "*" * 15)
    
    dfF = df[ (df["distrito" ] == 28) | (df["distrito" ] == 29) | (df["distrito" ] == 30) | (df["distrito" ] == 31) | (df["distrito" ] == 32)| (df["distrito" ] == 33) | (df["distrito" ] == 34)]
    
    print("Especificar tamaño de la muestra en (%): ") 
    tamanno_muestra = float(input()) / 100
    
       
    Cantsort = int(math.ceil(len(dfF) * tamanno_muestra))
    
    lista_med = list(dfF["medidor"])
    
    lista_sum = list(dfF["suministro"])
    
    print("La cantidad de numeros a sortear son " + str(Cantsort) + " de " + str(len(lista_med)))
  
    RCPT1f = proceso(Cantsort,lista_med,lista_sum)
    
    RCPT1 = RCPT1f
    
    RCPT1f["zona"] = "F"
    
    RCPT1t = pd.concat([RCPT1t,RCPT1f])

    print(RCPT1t)

  elif op == 7:

   

    RCPT1g = pd.DataFrame()
  
    
    print( "*" * 15 + "--------ZONA G----------" + "*" * 15)
    
    dfG = df[ (df["distrito" ] == 35) | (df["distrito" ] == 36) | (df["distrito" ] == 37) | (df["distrito" ] == 38) | (df["distrito" ] == 39)| (df["distrito" ] == 40) | (df["distrito" ] == 41) | (df["distrito" ] == 42) | (df["distrito" ] == 43) | (df["distrito" ] == 44)]
    
    print("Especificar tamaño de la muestra en (%): ") 
    tamanno_muestra = float(input()) / 100
    
       
    Cantsort = int(math.ceil(len(dfG) * tamanno_muestra))
    
    lista_med = list(dfG["medidor"])
    
    lista_sum = list(dfG["suministro"])
    
    print("La cantidad de numeros a sortear son " + str(Cantsort) + " de " + str(len(lista_med)))
  
    RCPT1g = proceso(Cantsort,lista_med,lista_sum)
    
    RCPT1 = RCPT1g
    
    RCPT1g["zona"] = "G"
    
    RCPT1t = pd.concat([RCPT1t,RCPT1g])

    print(RCPT1t)

  elif op == 8:
    
    RCPT1h = pd.DataFrame()
  
    
    print( "*" * 15 + "--------ZONA H----------" + "*" * 15)
    
    dfH = df[ (df["distrito" ] == 45) | (df["distrito" ] == 46)]
    
    print("Especificar tamaño de la muestra en (%): ") 
    tamanno_muestra = float(input()) / 100
    
       
    Cantsort = int(math.ceil(len(dfH) * tamanno_muestra))
    
    lista_med = list(dfH["medidor"])
    
    lista_sum = list(dfH["suministro"])
    
    print("La cantidad de numeros a sortear son " + str(Cantsort) + " de " + str(len(lista_med)))
  
    RCPT1h = proceso(Cantsort,lista_med,lista_sum)
    
    RCPT1 = RCPT1h
    
    RCPT1h["zona"] = "H"
    
    RCPT1t = pd.concat([RCPT1t,RCPT1h])

    print(RCPT1t)

  elif op == 9:

    RCPT1i = pd.DataFrame()
    
    print( "*" * 15 + "--------ZONA I----------" + "*" * 15)
    
    dfI = df[ (df["distrito" ] == 47) | (df["distrito" ] == 49)]
    
    print("Especificar tamaño de la muestra en (%): ") 
    tamanno_muestra = float(input()) / 100
    
       
    Cantsort = int(math.ceil(len(dfI) * tamanno_muestra))
    
    lista_med = list(dfI["medidor"])
    
    lista_sum = list(dfI["suministro"])
    
    print("La cantidad de numeros a sortear son " + str(Cantsort) + " de " + str(len(lista_med)))
  
    RCPT1i = proceso(Cantsort,lista_med,lista_sum)
    
    RCPT1 = RCPT1i
    
    RCPT1i["zona"] = "I"
    
    RCPT1t = pd.concat([RCPT1t,RCPT1i])

    print(RCPT1t)
  
  elif op == 10:

    RCPT1t.to_csv('RCPT1')   # LINEA PARA EXPORTAR

    

  elif op == 11:

    
    
    RCPT1.to_csv('RCPT1')   # LINEA PARA EXPORTAR

  
  elif op == 12:
    
    pop == False
  
  else:
  
    print("--No te hagas el vivo--")

    pop == False


#---------Generacion RCPT1-------------


  
  

  







#---------------EXPORTACION--------------

# RCPT1.to_csv('RCPT1')   # LINEA PARA EXPORTAR




#dfB = df[ (df[ "distrito"] == 2) |
 #         (df[ "distrito"] == 3)
  #        
   # 
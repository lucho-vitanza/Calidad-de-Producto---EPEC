#-----------------LIBRERIAS---------------------------

import pandas as pd

import math 


#------------------MANIPULACION TABLA-----------------

#----LECTURA CSV------------------------

df = pd.read_csv('bruta_mayor40.csv', delimiter = "," )




#print(df.shape)
#print(df.info)

#------RENOMBRADO DE COLUMNAS----------

df.rename(columns={"Servicio":"suministro", "Distrito":"distrito", "Medidor":"medidor"},inplace = True)

#-----CONVERSION DE TIPO DE DATO-------

df = df.astype("Int32")

print(df.dtypes)

#--------SACAR LOS MUERTOS------

df.fillna(method="ffill")



#--------declaracion de variables------------------

lista_num_sorteados = []
lista_med_sorteados = []
lista_sum_sorteados = []

i = 0

tamanno_muestra = 0

print("Especificar tamaño de la muestra en %: ") 

tamanno_muestra = float(input()) / 100

#---------------------ZONA A----------------------------

print( "*" * 10 + "--------ZONA A----------" + "*" * 10)


dfA = df[ (df[ "distrito" ] == 1 ) ]

Cantsort = int(math.ceil(len(dfA) * tamanno_muestra))

listaA_med = list(dfA["medidor"])

listaA_sum = list(dfA["suministro"])

print("La cantidad de numeros a sortear son " + str(Cantsort) + " de " + str(len(listaA_med)))




#---------------PROCESO-------------

while i < Cantsort: 
  
  i += 1
  
  print("Ingrese " + str(i) + " numero sorteado : ") 
  
  num_sorteado = int(input())
  
  lista_num_sorteados.append(num_sorteado)
  
  lista_med_sorteados.append(listaA_med[num_sorteado + 1])

  lista_sum_sorteados.append(listaA_sum[num_sorteado + 1])
   
  

print( "Lista de numeros sorteados: " + str(lista_num_sorteados))
print("Lista de medidores sorteados: "+ str(lista_med_sorteados))
print("Lista de suministros sorteados: "+ str(lista_sum_sorteados))



#---------Generacion RCPT1----------

RCPT1 = pd.DataFrame({'Suministros' : lista_sum_sorteados, 'Medidores' : lista_med_sorteados}) 


#---------------EXPORTACION--------------

# RCPT1.to_csv('RCPT1')   # LINEA PARA EXPORTAR




#dfB = df[ (df[ "distrito"] == 2) |
 #         (df[ "distrito"] == 3)
  #        
   # 
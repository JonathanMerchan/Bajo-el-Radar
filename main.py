""" Programa Apoyo multas#
    incorpora al modulo multas.py
    
#---------------- Zona librerias------------
import multas.py as mult
'''
el archivo esta bien importado y el codigo funcion por que lo probe integrando la funcion, sin embargo dice que no encuentra el archivo pienso que no esta en la misma carpeta 
'''
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================


#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
print("-------------- RADAR -------------- \n")
print("En esta progrmam determinara las multas qa las que es responsable el conductor \n")

dis1 = float(input("Por favor indique la primera distancia \n"))
dis2 = float(input("Por favor indique la segunda distancia \n"))

tiempo = float(input("Indique el lapso de tiempo en que se tomaron las distancias \n"))

print("Dados los datos anteriores se concluye: \n")

t= mult.multar_velocidad(dis1, dis2,tiempo)
##print (t)

if t=="Multa tipo I" or t=="Multa tipo II e inmovilizacion del vehiculo":
  print(t )
  print("\n Dado el resultado anterior es necesario realizar prueba de alcoholemia \n")
  alcohol = float(input("indique cual es el valro de alcohol registrado \n"))
  print("\n ******     Sancion adicional      ****** \n")
  print(mult.multar_alcoholemia(alcohol))
else:
  print(t)

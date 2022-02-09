""" Modulo Multas
    Funciones para el cálculo de multas
    de tránsito 
    
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def multar_velocidad(distancia_uno, distancia_dos,tiempo):
  #TODO: Documentar función 
  texto_multa=""
  #TODO: Implementar función
  velocidad = (distancia_uno-distancia_dos)/tiempo

  if 0<velocidad<20:
    texto_multa="Llamado de atencion por baja velocidad"
  elif 21<velocidad<60:
    texto_multa ="Normal"
  elif 61<velocidad<80:
    texto_multa = "Llamado de atencion por alta velocidad"
  elif 81<velocidad<120:
    texto_multa = "Multa tipo I"
  elif velocidad>120:
    texto_multa = "Multa tipo II e inmovilizacion del vehiculo"
  
  return texto_multa

def multar_alcoholemia(grado_alcohol):
#TODO: Documentar función 
  texto_multa=""
  #TODO: Implementar función
  
  if grado_alcohol<20:
    texto_multa = "---> No hay Multa por alcohol"
  elif 20<grado_alcohol<39:
    texto_multa= "---> Se decretará la suspensión de la licencia de conducción entre seis (6) y doce (12) meses."
  elif 40<grado_alcohol<99:
    texto_multa= "---> Se decretará la suspensión de la Licencia de Conducción entre uno (1) y tres (3) años."
  elif 100<grado_alcohol<149:
    texto_multa= "--->Se decretará la suspensión de la Licencia de Conducción entre tres (3) y cinco (5) años, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de cuarenta (40) horas."
  elif grado_alcohol>150:
    texto_multa= "---> Se decretará la suspensión entre cinco (5) y diez (10) años de la Licencia de Conducción, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de ochenta (80) horas."
  
  return texto_multa


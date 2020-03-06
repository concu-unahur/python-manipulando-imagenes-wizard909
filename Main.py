import logging
from APIclass import PixabayAPI
import threading
import time
from archivos import *
from concatenacion import *

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

carpeta_imagenes = './imagenes'
query = 'gatos'
api = PixabayAPI('15336427-98dc43b484029d2f0562fe03b', carpeta_imagenes)
listas_nombre_imagenes_Pares = []
concatenar_imagen = threading.Thread()

monitor1 = threading.Condition()
monitor2 = threading.Condition()

#Buscando imagenes
logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, 7)

#Descargando Imagenes
for u in urls:
  logging.info(f'Descargando {u}')

  threading.Thread(target = api.descargar_imagen, args= [u]).start()
  
#Espernado para que descargen
#CORREGIR CON THREADS
print("esperando 5 segundos, a que descdarguen las imagenes")
time.sleep(5)

#Iniciando Thread que leen 2 imagenes
threading.Thread(target= leerDosImagenesDescargadas).start()

#Iniciando Thread que leen 2 imagenes
threading.Thread(target= concatenarDosImagenesLeidas).start()


###############################FUNCIONES#######################################

#LEER IMAGEN
#Creando una lista con 2 rutas de imagen como elementos y agregandolas a otra lista
def leerDosImagenesDescargadas():
  global listas_nombre_imagenes_Pares

  while (len(api.lista_nombre_imagenes) > 2):
    monitor1.wait()
    monitor1.wait()
    logging.info("Leyendo 2 imagenes")
    #tiene que quedar asi/////lista = [[imagen1,imagen2],[imagen3,imagen4],[imagen5,imagen6]
    listas_nombre_imagenes_Pares.append([leer_imagen(api.lista_nombre_imagenes.pop(0)),leer_imagen(api.lista_nombre_imagenes.pop(0))])

#Concatenando de a listas con 2 imagenes [imagen1,imagen2]
def concatenarDosImagenesLeidas(imagenes):
  global listas_nombre_imagenes_Pares

  with monitor2:
    i = 1
    for l in (listas_nombre_imagenes_Pares):
      logging.info("Concatenando")
      escribir_imagen(f'concatenada-vertical{i}.jpg', concatenar_vertical(l))  
      escribir_imagen(f'concatenada-horizontal{i}.jpg', concatenar_horizontal(l)) 
      i+=1
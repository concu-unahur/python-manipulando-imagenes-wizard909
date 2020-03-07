import logging
from APIclass import *
import threading
import time
from archivos import *
from concatenacion import *

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

monitor0 = threading.Condition()
monitor1 = threading.Condition()
monitor2 = threading.Condition()
carpeta_imagenes = './imagenes'
query = 'gatos'
api = PixabayAPI('15336427-98dc43b484029d2f0562fe03b', carpeta_imagenes,monitor0)
cantidadImagenesDescargar = 4
cantidadImagenesPorConcatenacion = 2
imagenes_leidas = []
indiceNombreImagenConcatenada = 1

###############################FUNCIONES#######################################

#LEER IMAGEN
#Creando una lista con 2 rutas de imagen como elementos y agregandolas a otra lista
def leerDosImagenesDescargadas():
  global imagenes_leidas
  global cantidadImagenesPorConcatenacion

  while True:
    with monitor0:
      while (len(api.lista_nombre_imagenes) < cantidadImagenesPorConcatenacion):
        monitor0.wait()
      logging.info("Leyendo 2 imagenes descargadas")
      imagenes_leidas.append([leer_imagen(api.lista_nombre_imagenes.pop(0)),leer_imagen(api.lista_nombre_imagenes.pop(0))])
      logging.info(len(imagenes_leidas))
      monitor1.notify()

#Concatenando de a listas con 2 imagenes [imagen1,imagen2]
def concatenarDosImagenesLeidas():
  global imagenes_leidas
  global cantidadImagenesPorConcatenacion
  global indiceNombreImagenConcatenada
  while True:
    with monitor1:
      while (len(imagenes_leidas) < 1):
        monitor1.wait()
      logging.info("Concatenando 2 imagenes leidas")
      escribir_imagen(f'concatenada-vertical{indiceNombreImagenConcatenada}.jpg', concatenar_vertical(imagenes_leidas.pop(0)))  
      escribir_imagen(f'concatenada-horizontal{indiceNombreImagenConcatenada}.jpg', concatenar_horizontal(imagenes_leidas.pop(0))) 
      indiceNombreImagenConcatenada+=1
      

##############################################################################################
#Buscando imagenes
logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, cantidadImagenesDescargar)

#Descargando Imagenes
for u in urls:
  logging.info(f'Descargando {u}')
  threading.Thread(target = api.descargar_imagen, args= [u]).start()
  
#Espernado para que descargen
logging.info("esperando 1 segundos a que descarguen las imagenes")
time.sleep(1)

#Iniciando Thread que leen 2 imagenes
for u in range (2):
  threading.Thread(target= leerDosImagenesDescargadas).start()

#Espernado a que se lean
time.sleep(1)
logging.info("esperando 1 segundo a que lean")

#Iniciando Thread que leen 2 imagenes
for i in range (2):
  threading.Thread(target= concatenarDosImagenesLeidas).start()
     


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
imagenes_leidas = []
indiceNombreImagenConcatenada = 1
monitor0 = threading.Condition()
monitor1 = threading.Condition()
monitor2 = threading.Condition()

#Buscando imagenes
logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, 4)

###############################FUNCIONES#######################################

#LEER IMAGEN
#Creando una lista con 2 rutas de imagen como elementos y agregandolas a otra lista
def leerDosImagenesDescargadas(imagen1,imagen2):
  global imagenes_leidas
  logging.info("Leyendo 2 imagenes")
  imagenes_leidas.append([leer_imagen(imagen1),leer_imagen(imagen2)])
  #imagenes_leidas.append(leer_imagen(imagen1))
  #imagenes_leidas.append(leer_imagen(imagen2))

#Concatenando de a listas con 2 imagenes [imagen1,imagen2]
def concatenarDosImagenesLeidas(dosImagenesLeidas):
  global imagenes_leidas
  global indiceNombreImagenConcatenada
  with monitor2:
    logging.info("Concatenando")
    escribir_imagen(f'concatenada-vertical{indiceNombreImagenConcatenada}.jpg', concatenar_vertical(dosImagenesLeidas))  
    escribir_imagen(f'concatenada-horizontal{indiceNombreImagenConcatenada}.jpg', concatenar_horizontal(dosImagenesLeidas)) 
    indiceNombreImagenConcatenada+=1
      

##############################################################################################
#Descargando Imagenes
for u in urls:
  logging.info(f'Descargando {u}')
  threading.Thread(target = api.descargar_imagen, args= [u]).start()
  
#Espernado para que descargen
print("esperando 3 segundos a que descarguen las imagenes")
time.sleep(3)

#Iniciando Thread que leen 2 imagenes
while (len(api.lista_nombre_imagenes) >= 2):
  threading.Thread(target= leerDosImagenesDescargadas, args= [api.lista_nombre_imagenes.pop(0),api.lista_nombre_imagenes.pop(0)]).start()

#Espernado a que se lean
time.sleep(3)
logging.info("esperando 3 segundo a que lean")

#Iniciando Thread que leen 2 imagenes
while (len(imagenes_leidas) >= 1):
  logging.info("Concatenando 2 imagenes")
  threading.Thread(target= concatenarDosImagenesLeidas, args= [imagenes_leidas.pop(0)]).start()
     


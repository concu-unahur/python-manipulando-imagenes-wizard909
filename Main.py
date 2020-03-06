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
concatenar_imagen = threading.Thread()

monitor0 = threading.Condition()
monitor1 = threading.Condition()
monitor2 = threading.Condition()

#Buscando imagenes
logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, 4)

#Descargando Imagenes
for u in urls:
  logging.info(f'Descargando {u}')

  threading.Thread(target = api.descargar_imagen, args= [u]).start()
  
#Espernado para que descargen
#CORREGIR CON THREADS
print("esperando 3 segundos, a que descdarguen las imagenes")
time.sleep(3)

#Iniciando Thread que leen 2 imagenes
with monitor0:
  while True:
    while (len(api.lista_nombre_imagenes) >= 2):
      imagenDescargada1= api.lista_nombre_imagenes[0]
      imagenDescargada2= api.lista_nombre_imagenes[1]
      threading.Thread(target= leerDosImagenesDescargadas, args= [imagenDescargada1,imagenDescargada2]).start()

#Iniciando Thread que leen 2 imagenes
with monitor1:
  p = 0
  while True:
    while (len(imagenes_leidas) >= 2):

      imagenleida1 = imagenes_leidas[p]
      imagenleida2 = imagenes_leidas[p+1]
      threading.Thread(target= concatenarDosImagenesLeidas, args= [[imagenleida1,imagenleida2]]).start()
      p += 2


###############################FUNCIONES#######################################

#LEER IMAGEN
#Creando una lista con 2 rutas de imagen como elementos y agregandolas a otra lista
def leerDosImagenesDescargadas(imagen1,imagen2):
  global imagenes_leidas
  logging.info("Leyendo 2 imagenes")
  imagenes_leidas.append([leer_imagen(imagen1),leer_imagen(imagen2)])

#Concatenando de a listas con 2 imagenes [imagen1,imagen2]
def concatenarDosImagenesLeidas(DosImagenesLeidas):
  global imagenes_leidas

  with monitor2:
    i = 1
    for l in (imagenes_leidas):
      logging.info("Concatenando")
      escribir_imagen(f'concatenada-vertical{i}.jpg', concatenar_vertical(l))  
      escribir_imagen(f'concatenada-horizontal{i}.jpg', concatenar_horizontal(l)) 
      i+=1
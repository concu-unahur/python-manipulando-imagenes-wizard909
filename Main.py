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


logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, 7)


for u in urls:
  logging.info(f'Descargando {u}')

  threading.Thread(target = api.descargar_imagen, args= [u]).start()

print("esperando 5 segundos, a que descdarguen las imagenes")
time.sleep(5)

#creando una lista de 2 rutas de las imagenes y agregandolas a un lista
listas_nombre_imagenes_Pares = []
aux = []
while (len(api.lista_nombre_imagenes) > 2):
  #tiene que quedar asi/////lista = [[imagen1,imagen2],[imagen3,imagen4],[imagen5,imagen6]
  """
  aux = list(map( leer_imagen(api.lista_nombre_imagenes.pop(i)),leer_imagen(api.lista_nombre_imagenes.pop(i))))
  aux.append(leer_imagen(api.lista_nombre_imagenes.pop(0)))
  aux.append(leer_imagen(api.lista_nombre_imagenes.pop(0)))
  listas_nombre_imagenes_Pares.append(aux)
  aux.clear()
  """

  listas_nombre_imagenes_Pares.append([leer_imagen(api.lista_nombre_imagenes.pop(0)),leer_imagen(api.lista_nombre_imagenes.pop(0))])
  #listas_nombre_imagenes_Pares.append([armar_ruta(api.lista_nombre_imagenes.pop(0)),armar_ruta(api.lista_nombre_imagenes.pop(0))])
  
print(listas_nombre_imagenes_Pares)

#concatenando de a listas con 2 imagens [imagen1,imagen2]

i = 1
for l in (listas_nombre_imagenes_Pares):
  
  escribir_imagen(f'concatenada-vertical{i}.jpg', concatenar_vertical(l))  
  escribir_imagen(f'concatenada-horizontal{i}.jpg', concatenar_horizontal(l)) 
  i+=1
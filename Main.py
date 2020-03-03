import logging
from APIclass import PixabayAPI
import threading

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

carpeta_imagenes = './imagenes'
query = 'gatos'
api = PixabayAPI('15336427-98dc43b484029d2f0562fe03b', carpeta_imagenes)


logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, 5)


for u in urls:
  logging.info(f'Descargando {u}')

  threading.Thread(target = api.descargar_imagen, args= [u]).start()


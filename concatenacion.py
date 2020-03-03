import cv2
from archivos import leer_imagen, escribir_imagen
from APIclass import *
from Main import *


def concatenar_horizontal(imagenes):
  # Buscamos el alto menor entre todas las imágenes
  alto_minimo = min(im.shape[0] for im in imagenes)

  # Redimensionamos las imágenes para que tengan todas el mismo alto
  imagenes_redimensionadas = [cv2.resize(im, (int(im.shape[1] * alto_minimo / im.shape[0]), alto_minimo))
                    for im in imagenes]

  # Concatenamos
  return cv2.hconcat(imagenes_redimensionadas)

def concatenar_vertical(imagenes):
  # Buscamos el ancho menor entre todas las imágenes
  ancho_minimo = min(im.shape[1] for im in imagenes)

  # Redimensionamos las imágenes para que tengan todas el mismo ancho
  imagenes_redimensionadas = [cv2.resize(im, (ancho_minimo, int(im.shape[0] * ancho_minimo / im.shape[1])))
                    for im in imagenes]

  # Concatenamos
  return cv2.vconcat(imagenes_redimensionadas)
"""
imagen1 = leer_imagen('1.jpg')
imagen2 = leer_imagen('2.jpg')
"""

listas_nombre_imagenes_Pares = []
aux = []
i = 0
while (len(api.lista_nombre_imagenes) < 2):

  #lista_nombre_imagenes = [[imagen1, imagen2], [imagen3,imagen4], etc]
  #aux = [leer_imagen(api.lista_nombre_imagenes.pop(i)),leer_imagen(api.lista_nombre_imagenes.pop(i))]
  listas_nombre_imagenes_Pares.append(leer_imagen(api.lista_nombre_imagenes[0]))
  #aux.append(leer_imagen(api.lista_nombre_imagenes[i+1]))
  print("creando ruta imagen")
  #api.lista_nombre_imagenes.pop(i)
  api.lista_nombre_imagenes.pop(i)
  i = 0
  #listas_nombre_imagenes_Pares.append(aux)
  #aux.clear()


"""
escribir_imagen('concatenada-vertical.jpg', concatenar_vertical([imagen1, imagen2]))    
escribir_imagen('concatenada-horizontal.jpg', concatenar_horizontal([imagen1, imagen2]))    
"""

for i in (api.lista_nombre_imagenes):
  print("Concatenando en vertical")
  escribir_imagen(f'concatenada-vertical{i}.jpg', concatenar_vertical(i))  
  print("Concatenando en horizontal")
  escribir_imagen(f'concatenada-horizontal{i}.jpg', concatenar_horizontal(i)) 
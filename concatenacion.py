import cv2
from archivos import leer_imagen, escribir_imagen
from APIclass import *

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


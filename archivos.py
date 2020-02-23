import os
from skimage import io, img_as_ubyte

carpeta_imagenes = './imagenes'

def armar_ruta(nombre):
  return os.path.join(carpeta_imagenes, nombre)

def leer_imagen(nombre):
  return io.imread(armar_ruta(nombre))

def escribir_imagen(nombre, imagen):
  io.imsave(armar_ruta(nombre), img_as_ubyte(imagen))

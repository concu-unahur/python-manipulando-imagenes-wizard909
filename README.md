# Ejemplos de manipulación de imágenes

## Instalación

Para instalar las dependencias del proyecto ejecutar lo siguiente:

```
pip3 install -r requirements.txt
```

## Organización

Cada archivo `.py` tiene un ejemplo sencillo de alguna manipulación posible, utilizando alguna o varias de las siguientes bibliotecas:
* [scikit-image](https://scikit-image.org/) 
* [opencv2](https://docs.opencv.org/master/index.html)

Todos los ejemplos leen y escriben en la carpeta `imagenes` que está en este mismo repo. Incluimos dos imágenes de ejemplo, pero pueden agregar las que quieran.

## Concatenando imágenes

Fijate `concatenacion.py` y familiarizate con su uso. Concantená varias imágenes (pueden ser más de 2), tanto horizontal como verticalmente.

Luego lo siguiente:
* Usando la clase pasada `python-buscando-imagenes` armate una lista con `nombre_archivo_img` de unas cuántas imágenes (20, 30, o algo así)
* Recorré la lista y andá concatenando (de a 2 o de a 3, por ejemplo).
* Medí el tiempo que tardás desde bajar hasta terminar de concatenar.
* Ahora lo mismo pero con threads: uno que baja y otro que concatena.
* Medí de nuevo el tiempo.

## Efectos en imágenes

Finalmente, mirá `contraste-rotacion-redimensiona.py` y usalo para familiarizarte con aplicar esos efectos a las imágenes.
import cv2

# Leer la imagen en color
imagen_color = cv2.imread('ruta/a/tu/juggernaut.jpg')

# Verificar si la imagen fue cargada correctamente
if imagen_color is None:
    print("Error al cargar la imagen.")
    exit()

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)

# Aplicar la ecualización de histograma
imagen_ecualizada = cv2.equalizeHist(imagen_gris)

# Guardar la imagen resultante
cv2.imwrite('imagen_ecualizada.jpg', imagen_ecualizada)

# Mostrar la imagen original y la imagen ecualizada
cv2.imshow('Imagen Original en Grises', imagen_gris)
cv2.imshow('Imagen Ecualizada', imagen_ecualizada)

# Esperar a que se presione una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
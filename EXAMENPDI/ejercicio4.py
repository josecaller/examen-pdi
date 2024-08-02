import cv2

# Leer la imagen
imagen = cv2.imread('rubick.jpg')

# Verificar si la imagen fue cargada correctamente
if imagen is None:
    print("Error al cargar la imagen.")
    exit()

# Aplicar el filtro de suavizado gaussiano con un kernel de 5x5
imagen_suavizada = cv2.GaussianBlur(imagen, (5, 5), 0)

# Guardar la imagen suavizada
cv2.imwrite('imagen_suavizada.jpg', imagen_suavizada)

# Mostrar la imagen original y la imagen suavizada
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Suavizada', imagen_suavizada)

# Esperar a que se presione una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()



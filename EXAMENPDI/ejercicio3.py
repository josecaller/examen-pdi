import cv2

# Cargar la imagen desde un archivo
imagen = cv2.imread('ursa.jpg')

# Verificar si la imagen se cargó correctamente
if imagen is None:
    print("Error: La imagen no se pudo cargar.")
    exit()

# Redimensionar la imagen a 300x300 píxeles
dimensiones = (300, 300)
imagen_redimensionada = cv2.resize(imagen, dimensiones)

# Mostrar la imagen redimensionada
cv2.imshow('Imagen Redimensionada', imagen_redimensionada)

# Guardar la imagen redimensionada
cv2.imwrite('imagen_redimensionada.jpg', imagen_redimensionada)

# Esperar a que se presione una tecla y cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()


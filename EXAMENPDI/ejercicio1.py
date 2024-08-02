import cv2

def convertir_a_escala_de_grises(ruta_imagen):
    """
    Convierte una imagen en color a escala de grises.
    
    Parámetros:
    ruta_imagen (str): Ruta de la imagen en color.
    """
    # Leer la imagen en color desde un archivo
    imagen_color = cv2.imread("juggernaut.jpg")

    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)

    # Guardar la imagen en escala de grises
    ruta_imagen_gris = 'imagen_gris.png'
    cv2.imwrite(ruta_imagen_gris, imagen_gris)

    # Mostrar la imagen en escala de grises
    cv2.imshow('Imagen en Escala de Grises', imagen_gris)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f'Imagen convertida a escala de grises guardada en: {ruta_imagen_gris}')

# Ruta de la imagen a convertir
ruta_imagen = 'ruta/a/tu/imagen.png'  # Cambia esto a la ruta de tu imagen


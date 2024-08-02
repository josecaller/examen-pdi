import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_edges(image):
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar el detector de bordes de Canny
    edges_canny = cv2.Canny(gray, 100, 200)

    # Aplicar el detector de bordes de Sobel
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    edges_sobel = cv2.magnitude(sobelx, sobely)
    edges_sobel = np.uint8(edges_sobel)

    return edges_canny, edges_sobel

def main(image_path):
    # Cargar la imagen
    image = cv2.imread("void.jpg")
    if image is None:
        print("Error al cargar la imagen.")
        return

    # Detectar bordes usando los métodos de Canny y Sobel
    edges_canny, edges_sobel = detect_edges(image)

    # Mostrar las imágenes originales y de bordes
    plt.figure(figsize=(12, 6))

    # Mostrar la imagen original
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Imagen Original')
    plt.axis('off')

    # Mostrar los bordes detectados por Canny
    plt.subplot(1, 3, 2)
    plt.imshow(edges_canny, cmap='gray')
    plt.title('Bordes con Canny')
    plt.axis('off')


    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    image_path = 'ruta/a/tu/void.jpg'  # Cambia esto a la ruta de tu imagen
    main(image_path)
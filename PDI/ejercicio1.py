import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Leer una imagen
image = cv2.imread('variasCaras.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convertir la imagen de RGB a L*a*b*
image_lab = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2LAB)

# Reshape la imagen para que sea una lista de píxeles
pixel_values = image_lab.reshape((-1, 3))
pixel_values = np.float32(pixel_values)

# Definir el criterio de k-means
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

# Número de clusters (k)
k = 5
_, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convertir los centros a entero de 8 bits
centers = np.uint8(centers)

# Convertir las etiquetas a la imagen de la misma forma que la imagen original
segmented_image = centers[labels.flatten()]
segmented_image = segmented_image.reshape(image_lab.shape)

# Convertir la imagen segmentada de L*a*b* a RGB
segmented_image_rgb = cv2.cvtColor(segmented_image, cv2.COLOR_LAB2RGB)

# Visualizar la imagen original y la segmentada
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Imagen Original')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Imagen Segmentada')
plt.imshow(segmented_image_rgb)
plt.axis('off')

plt.show()
import cv2 as cv
from matplotlib import pyplot as plt

original_img = cv.imread("../images/5.webp", 0)
image_nose = cv.GaussianBlur(original_img, (5, 5), 0)

# Laplacian
laplacian = cv.Laplacian(image_nose, cv.CV_64F)

# Sobel
sobel_x = cv.Sobel(image_nose, cv.CV_64F, 1, 0, ksize=5)
sobel_y = cv.Sobel(image_nose, cv.CV_64F, 0, 1, ksize=5)

# Canny Edge Detection
edges = cv.Canny(original_img, 100, 500)


fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1, 5, figsize=(15, 15))
ax1.imshow(original_img, cmap="gray")
ax2.imshow(laplacian, cmap="gray")
ax3.imshow(sobel_x, cmap="gray")
ax4.imshow(sobel_y, cmap="gray")
ax5.imshow(edges, cmap="gray")

plt.show()

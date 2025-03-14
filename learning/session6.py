import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

original_img = cv.imread("../images/1.jpg", 0)

_, thresh = cv.threshold(original_img, 60, 255, cv.THRESH_BINARY_INV)


# Erosion
# kernel = np.ones((5, 5), np.uint8)
# erosion = cv.erode(thresh, kernel, iterations=1)

# Dilation
# kernel = np.ones((3, 3), np.uint8)
# erosion = cv.dilate(thresh, kernel, iterations=1)

# Closing
kernel = np.ones((5, 5), np.uint8)
erosion = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, iterations=1)

# Opening

# Gradient


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 15))
ax1.imshow(original_img, cmap="gray")
ax2.imshow(thresh, cmap="gray")
ax3.imshow(erosion, cmap="gray")

plt.show()

# Morphological Gradient

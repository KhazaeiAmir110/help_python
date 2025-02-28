import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("../images/best-about-us-pages.jpg", cv.IMREAD_GRAYSCALE)

# cv.IMREAD_GRAYSCALE => 0
# cv.IMREAD_COLOR => 1
# cv.IMREAD_UNCHANGED => -1

# System Color => BGR (blue, green, red)

"""
show image

cv.imshow("image", img)
cv.waitKey(0)
cv.destroyWindow()

cv.imwrite("../images/save/1.jpg", img)
"""

plt.imshow(img, cmap="grey", interpolation="bicubic")
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([50, 100], [100, 500], "c", linewidth=4)
plt.show()

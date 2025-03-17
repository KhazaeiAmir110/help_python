import cv2 as cv
import numpy as np

img = cv.imread("../images/best-about-us-pages.jpg", cv.IMREAD_COLOR)

# 10 is thickness
cv.line(img, (5, 5), (200, 150), (55, 0, 0), 10)

# 5 is thickness
cv.rectangle(img, (200, 300), (200, 150), (0, 255, 0), 5)

# -1 for fill
cv.circle(img, (100, 100), 55, (255, 0, 0), 5)

# np.int32 is the type of the array
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)

# -1 means we don't know the number of rows, 1 means we have 1 column, 2 means we have 2 elements in each column
pts = pts.reshape((-1, 1, 2))

# True means the shape is closed
cv.polylines(img, [pts], True, (0, 255, 255), 3)

# anti-aliased line
cv.putText(img, "Hello", (400, 200), cv.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), 2, cv.LINE_AA)

cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()

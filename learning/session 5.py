import cv2 as cv

img4 = cv.imread("../images/4.png")

imgray = cv.cvtColor(img4, cv.COLOR_BGR2GRAY)

_, thresh = cv.threshold(imgray, 60, 255, cv.THRESH_BINARY_INV)

ret, thresh2 = cv.threshold(imgray, 0, 60, cv.THRESH_BINARY + cv.THRESH_OTSU)

thresh3 = cv.adaptiveThreshold(imgray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow("added", thresh2)
cv.imshow("added", thresh3)
cv.waitKey(0)
cv.destroyAllWindows()

import cv2 as cv

img1 = cv.imread("../images/2.jpg")
img2 = cv.imread("../images/3.jpg")

# added
# added = cv.add(img1, img2)
# added = img1 + img2
added = cv.addWeighted(img1, 0.6, img2, 0.4, 0)

cv.imshow("added", added)
cv.waitKey(0)
cv.destroyAllWindows()

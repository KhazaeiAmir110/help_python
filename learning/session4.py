import cv2 as cv

img1 = cv.imread("../images/3.jpg")
img2 = cv.imread("../images/4.png")

# added
# added = cv.add(img1, img2)
# added = img1 + img2
added = cv.addWeighted(img1, 0.2, img2, 0.8, 0)

cv.imshow("added", added)
cv.waitKey(0)
cv.destroyAllWindows()

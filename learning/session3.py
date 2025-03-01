import cv2 as cv

img = cv.imread("../images/best-about-us-pages.jpg", cv.IMREAD_COLOR)

img2 = img[100:300, 250:500]

img[100:300, 250:500] = [0, 0, 0]

cv.imshow("image", img)
cv.imshow("image2", img2)
cv.waitKey(0)
cv.destroyAllWindows()

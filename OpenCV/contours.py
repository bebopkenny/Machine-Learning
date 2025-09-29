import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

canny = cv.Canny(img, 125, 175)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f'{len(contours)} contours found!')

cv.waitKey(0)
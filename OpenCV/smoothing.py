import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')

# Averaging
average = cv.blur(img, (7,7))
cv.imshow('Averge Blur', average)

# Gaussian Blur (uses weight)
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur (same thing as averaging but it finds the mean tends to me more effective reducing noise)
# does not work well with big numbers
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# Bilaterial 
# most effective and used a lot in advanced CV projects
# applies blured but retains image 
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow('Bilateral', bilateral)



cv.waitKey(0)
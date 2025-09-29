import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8') # black image
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
blank[:] = 0,255,0 # one single blank color image
blank[200:300, 300:400] = 0,0,255 # coloring a certain portion of the image
cv.imshow('Green', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2) # thickness=-1 fills in the color
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,0,0), thickness=-1) # gets the actual image as the size

# 3. Draw a circle 
cv.circle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0,0), (300, 400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)























cv.imshow('Rectangle', blank)

cv.waitKey(0)
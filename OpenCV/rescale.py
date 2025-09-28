import cv2 as cv 

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # ONLY WORKS ON: images, videos, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Resizing of the cat image
img = cv.imread('/Resources/Photos/cat.jpg')
resized_image = rescaleFrame(img) 
cv.imshow('Image', resized_image)

# Change resolution
def changeRes(width, height):
    # ONL WORKS ON: live video
    capture.set(3, width)
    capture.set(4, height)

# Recording video
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cv.waitKey(0)
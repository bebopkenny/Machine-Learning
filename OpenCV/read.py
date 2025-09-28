import cv2 as cv

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)

cv.waitKey(0) # waits for a key to be pressed


# Reading videos

capture = cv.VideoCapture('Videos/.mp4')

while True: # we need a while loop to capture the video frame by frame
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'): # if the letter "d" is pressed break out
        break

capture.release()
cv.destroyAllWindows()



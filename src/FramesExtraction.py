import cv2 as cv
import os

videoPath = './assets/videos/'
videoName = 'VideoSource'
videoFormat = '.mp4'
video = cv.VideoCapture(videoPath + videoName + videoFormat)
frameCounter = 0
hasFrame, frame = video.read()

if not os.path.exists('./assets/img/' + videoName):
    os.makedirs('./assets/img/' + videoName)

while hasFrame:
    cv.imshow("Output", frame)
    cv.imwrite('./assets/img/' + videoName + '/Frame' + str(frameCounter) + '.jpg', frame)

    hasFrame, frame = video.read()

    frameCounter += 1
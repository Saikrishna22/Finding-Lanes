import cv2
import numpy as np
import matplotlib.pyplot as plt


def mask_region(canny):
    bottom = image.shape[0]
    ## this array consists of shape of a polygon where the lane lines would be
    ## selecting that as a masking region
    polygons = np.array([[(220,bottom),(1100,bottom),(550,250)]])
    mask = np.zeros_like(canny)
    cv2.fillPoly(mask,polygons,255)
    masked_image = cv2.bitwise_and(canny,mask)
    return masked_image

def display_lines(image,lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 =line.reshape(4)
            cv2.line(line_image,(x1,y1),(x2,y2),(0,255,0),10)
    return line_image





image = cv2.imread('test_image.jpg')
lane = np.copy(image)
gray = cv2.cvtColor(lane,cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
canny = cv2.Canny(blur,50,150)
crop_image = mask_region(canny)
lines = cv2.HoughLinesP(crop_image,2,np.pi/180,100,np.array([]),minLineLength=50,maxLineGap=5)
line_image = display_lines(lane, lines)
add_image = cv2.addWeighted(lane,0.8,line_image,1,1)
cv2.imshow('hello',add_image)
cv2.waitKey(0)
#
#

####->>>>> This Code is for Video test2.mp4
# cap= cv2.VideoCapture("test2.mp4")
# while(cap.isOpened()):
#     _, frame = cap.read()
#     gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
#     blur = cv2.GaussianBlur(gray,(5,5),0)
#     canny = cv2.Canny(blur,50,150)
#     crop_image = mask_region(canny)
#     lines = cv2.HoughLinesP(crop_image,2,np.pi/180,100,np.array([]),minLineLength=50,maxLineGap=5)
#     line_image = display_lines(frame, lines)
#     add_image = cv2.addWeighted(frame,0.8,line_image,1,1)
#     cv2.imshow('hello',add_image)
#     cv2.waitKey(1)

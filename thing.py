
# coding: utf-8

# In[9]:

import cv2
import numpy as np
import math

def angle(p1, p2, p0):
   dx1 = p1[0][0]-p0[0][0]
   dy1 = p1[0][1]-p0[0][1]
   dx2 = p2[0][0]-p0[0][0]
   dy2 = p2[0][1]-p0[0][1]
   return math.atan(dy1/dx1)-math.atan(dy2/dx2)

def right(app, x):
    maxCosine = 0
    for k in range(2, x+1):
        pt1 = app[k%4]
        pt2 = app[k-2]
        pt0 = app[k-1]
        cos = (angle(pt1, pt2, pt0))
        cosine = math.fabs(math.cos(cos))
        maxCosine = max(maxCosine, cosine)
        if(maxCosine<.2):
            return True
        else:
            return False

img = cv2.imread("hwimg.png") #Reads image and places it into img

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Converts to HSV

#cv2.imshow("HSV", img_hsv)

THRESHOLD_MIN = np.array([0, 0, 0],np.uint8) # Sets minimum hue
THRESHOLD_MAX = np.array([20, 255, 255],np.uint8) # Sets maximum hue

thresh = cv2.inRange(img_hsv, THRESHOLD_MIN, THRESHOLD_MAX)

#cv2.imshow("Thresholded", thresh)

cannied = cv2.Canny(thresh, 0, 20, 3)

#cv2.imshow("Canny", edges)

(edges, _) = cv2.findContours(cannied, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

epsilon = 0.1*cv2.arcLength(edges[0],True)

highCont = cv2.approxPolyDP(edges[0], epsilon, True)
highArea = cv2.contourArea(highCont)
for i in edges:
    approx = cv2.approxPolyDP(i, epsilon, True)
    area = cv2.contourArea(approx)
    if (right(approx, 8) and  area > highArea):
        highArea = area
        final = approx
print (final)
final2 = [final]
cv2.drawContours(img, final2, 0, (0,255,255), 10)

print (highArea)
cv2.imshow("Done", img)

cv2.waitKey(0)



# In[ ]:




# In[ ]:




# In[ ]:




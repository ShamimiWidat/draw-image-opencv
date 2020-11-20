import cv2
import numpy as np

image = cv2.imread("nisekoi_chitoge.png")
print(image.shape)

#bgr
blue = (255, 0, 0)
red = (0, 0, 255)
green = (0, 255, 0)
violet = (180, 0, 180)
yellow = (0, 255, 255)
white = (255, 255, 255)

#output will show y,x but in code write x,y (frist point then second point location
cv2.line(image, (100, 200), (1000,200), blue, thickness = 10)
# the centre point, radius, -1=fill the shape with colour
cv2.circle(image, (400,500), 20, red, -1)
#first point=left top, second point=right low
cv2.rectangle(image, (600,200), (700, 500), green, -1)
#centre point, major-minor axis radius, rotational angle of ellipse in clockwise, starting angle in clockwise, finishing angle in clockwise
cv2.ellipse(image, (300,800), (50,25), 45, 150, 400, violet, -1)
#true for closed polygon
points = np.array([[200,600],[300,500],[500,700],[300,1000]], np.int32)
cv2.polylines(image, [points], True, yellow, thickness = 10)
#point at top left, size
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(image, "Baby", (100,300), font, 3, white, thickness = 10)

cv2.imshow("chitoge", cv2.resize(image, None, fx=0.5, fy=0.5))
cv2.waitKey(0)
cv2.destroyAllWindows()

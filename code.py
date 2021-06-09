# TASK-4.1

## Create image by yourself Using Python Code.


import cv2 , numpy

image  = cv2.imread('image.jpeg')

# changing colour to white
image[:] = 255

cv2.imshow('bg',image)
cv2.waitKey()
cv2.destroyAllWindows()

### Creating a 2D image 

# Head
image=cv2.rectangle(image,(200,60),(400,215),(255,0,0),-100)

# Eyes
image=cv2.circle(image,(260,120),15,(0,225,255),-100)
image=cv2.circle(image,(340,120),15,(0,225,255),-100)

# Mouth
image=cv2.rectangle(image,(260,170),(340,190),(0,225,225),-100)

# left-ear
image=cv2.rectangle(image,(180,120),(200,180),(0,0,0),-100)

# right-ear
image=cv2.rectangle(image,(400,120),(420,180),(0,0,0),-100)

# cap
image=cv2.ellipse(image,(300,60),(35,20),0,0,-180,( 102 ,51,0),-100)

# Antenna
image=cv2.rectangle(image,(300,40),(305,10),(0,0,0),-100)

cv2.imshow('bg',image)
cv2.waitKey()
cv2.destroyAllWindows()



# TASK-4.2

## Crop some part of both image and swap it

import cv2 , numpy

path = r"D:\DATA\images1.jfif"

img = cv2.imread(path)

cv2.imshow('myphoto1',img)
cv2.waitKey()
cv2.destroyAllWindows()

path2 = r"D:\DATA\images.jfif"

img2 = cv2.imread(path2)

cv2.imshow('myphoto3',img2)
cv2.waitKey()
cv2.destroyAllWindows()

Swaping

temp=img.tolist()
img[14:195 ,  15:210]=img2[14:195 ,  15:210]
img2[14:195 , 15:210]=numpy.array(temp,dtype='uint8')[14:195 ,  15:210]

cv2.imshow('myphoto5',img)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('myphoto5',img2)
cv2.waitKey()
cv2.destroyAllWindows()





# TASK 4.3

import cv2 , numpy

path1 = r"D:\DATA\image2.jfif"

path2 = r"D:\DATA\image1.jfif"

main1 = cv2.imread(path1)

cv2.imshow('Image1',main1)
cv2.waitKey()
cv2.destroyAllWindows()

main2 = cv2.imread(path2)

cv2.imshow('Image2',main2)
cv2.waitKey()
cv2.destroyAllWindows()

final_horizontal = cv2.hconcat([main1, main2])

cv2.imshow('FINAL in Horizontal',final_horizontal)
cv2.waitKey()
cv2.destroyAllWindows()

final_vertical = cv2.vconcat([main1, main2])

cv2.imshow('FINAL in Vertical',final_vertical)
cv2.waitKey()
cv2.destroyAllWindows()


#Author: Janmejay Mohanty
#Cite: https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpread

def rgb_to_gray(img):
    greyscaleimg = np.zeros(img.shape)                          
    R = np.array(img[:, :, 0])
    G = np.array(img[:, :, 1])
    B = np.array(img[:, :, 2])

    Value = (R *0.2989 + G *0.5870 + B *0.1140)                        #Converting each pixel into grey scale value using this equation.

    greyscaleimg = img.copy()

    for i in range(3):
        greyscaleimg[:,:,i] = Value
           
    return greyscaleimg       

image = mpread.imread("Capture.png")                                     #Giving normal image as an input
print(image)                                                                 
greyscaleimg = rgb_to_gray(image)                                        #Calling Grey Scale converting image
image_gray = plt.imsave("outfile.png", greyscaleimg)
plt.imshow(greyscaleimg)
plt.show()
#Name: Gianni Russell
#gianni.russell07@myhunter.cuny.edu
#Date: October 29, 2023


import matplotlib.pyplot as plt
import numpy as np

inF = input("Enter file name: ")

output_file = input("Enter name of output file: ")

img = plt.imread(inF)


height = img.shape[0] 
width = img.shape[1] 

img2 = img[height//2:, :width//2] 

#plt.imshow(img2) 
#plt.show() 

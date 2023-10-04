import cv2
import os
import pickle
import numpy as np

data_dir = os.path.join(os.getcwd(),'clean_data')
img_dir = os.path.join(os.getcwd(),'images')

#'os.path' is a module in Python's standard library that provides functions for working with file paths and directories.
#'os.getcwd()' is a function that returns the current working directory (CWD) as a string. 
#The CWD is the directory from which the Python script is being executed.
#'images' is a string that represents a directory name.

image_data = []
labels = []

for i in os.listdir(img_dir):      #a loop that iterates over the contents of a directory specified by the variable 'img_dir'
    
    image = cv2.imread(os.path.join(img_dir,i))           #read the image at that location
    image = cv2.resize(image,(100,100))                   #resize all the images to 100x100 pixels
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)        #convert all the images to gray scale/color intensity scale
    image_data.append(image)                              #add the cleaned image to the 'image_data' that will be pickeled as image
    labels.append(str(i).split("_")[0])                   #add the label of the cleaned image to the 'labels' that will be pickeled as labels
    
#converted the cleaned images to an np-array
image_data = np.array(image_data) 
print(image_data)   
labels = np.array(labels) 
print(labels)

#plotting how a image after cleaning looks like
import matplotlib.pyplot as plt
plt.imshow(image_data[25],cmap="gray")
plt.show()

#pickling the images and their labels
with open(os.path.join(data_dir,"images.p"),'wb') as f:
    pickle.dump(image_data,f)
    
with open(os.path.join(data_dir,"labels.p"),'wb') as f:
    pickle.dump(labels,f)
    
#To summarize, the code opens a file named "labels.p" in binary write mode within the specified data_dir directory.
#It then uses the pickle module to serialize and write the labels object to that file. 
#The with statement ensures proper file handling and automatically closes the file after the operation is completed.







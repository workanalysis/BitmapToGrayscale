#This program will convert a bitmap format image into grayscale image format with the help of opencv and numpy python libraries
import cv2              #imports openCV library
import numpy as np      #imports numpy library

img=cv2.imread('workplace/im2.jpg') #this is the function to read image
                                    #the path of image is respect to python installation folder in c drive
                                    #take any test image
                                    #i have saved it in workplace folder in my drive

#img.shape will return three parameters 1st rows,2nd columns(this is generally pixels in form of rows and column)
#img.shape[0] will give us rows of image
#img.shape[1] will give us columns of image
#random module of numpy is used to allocate memory to an array or create array
#refer to numpy library for more information about ramdom module
x=np.random.randint(img.shape[0]*img.shape[1],size=(img.shape[0],img.shape[1])) #this will declare array with similar no. of rows and column of img opened
x=np.uint8(x)   #this is to convert integer array x in uint8(this is called or referred as datatype of the image)
                #uint8 is a datatype provided by numpy library
                #use "img.dtype" to get datatype of the image 
    
x[:,:]=0.11*img[:,:,0]+0.59*img[:,:,1]+0.30*img[:,:,2]  #numpy method of assigning value at each index of multidimensional array
                                                        #eg. x[:,:]=4 will assign 4 to each index of x array
  
cv2.imshow('image',x)   #this function is used to display image, first parameter is window name and 2nd the array of image
cv2.waitKey(5000)          #this function act like getch() in c++ i.e. wait after keyboard input for 0 micro secs
cv2.destroyAllWindows()     #this function is to destroy all result windows 

#Use below given function to execute python script in PYTHON IDLE, path of file provided is respect to python installation folder in c drive
#exec(open('workplace/test.py').read())

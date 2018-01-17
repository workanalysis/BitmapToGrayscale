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
x=np.random.randint(img.shape[0]*img.shape[1],size=(img.shape[0],img.shape[1]))#this will declare array with similar no. of rows and column of img opened
x=np.uint8(x)   #this is to convert integer array x in uint8(this is called or referred as datatype of the image)
                #uint8 is a datatype provided by numpy library
                #use "img.dtype" to get datatype of the image 

for var in range(img.shape[0]):             #this is to iterate rows
    for vara in range(img.shape[1]):        #this is to iterte columns
        im1=int(img[var][vara][0])          #this assign BLUE value of a single pixel and convert it into integer type from float
        im2=int(img[var][vara][1])          #this assign GREEN value of a single pixel and convert it into integer type from float
        im3=int(img[var][vara][2])          #this assign RED value of a single pixel and convert it into integer type from float

        im1=0.11*im1    #11% of blue color is taken
        im2=0.59*im2    #59% of green color is taken
        im3=0.3*im3    #30% of red color is taken

        x[var][vara]=im1+im2+im3    #addtion is performed to get a single 8 bit value(If represented in binary format)

        #below given formulaes are just for testing purpose
        #1st one is average method for mixing three colors
        #2nd is the another form of above given algo of mixing colors

        #x[var][vara]=(img[var][vara][0]+img[var][vara][1]+img[var][vara][2])/3
        #x[var][vara]=((30*100)/int(img[var][vara][0]))+((59*100)/int(img[var][vara][1]))+((11*100)/int(img[var][vara][2]))
        #x[var][vara]=((0*100)/img[var][vara][2])+((59*100)/img[var][vara][1])+((41*100)/img[var][vara][0])
    
    print((var*100)/img.shape[0],"%")   #this is to see the progress of conversion of image

cv2.imshow('image',x)   #this function is used to display image, first parameter is window name and 2nd the array of image
cv2.waitKey(5000)          #this function act like getch() in c++ i.e. wait after keyboard input for 0 micro secs
cv2.destroyAllWindows()     #this function is to destroy all result windows 

#Use below given function to execute python script in PYTHON IDLE, path of file provided is respect to python installation folder in c drive
#exec(open('workplace/test.py').read())
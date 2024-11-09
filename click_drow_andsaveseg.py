import cv2
import numpy as np
import time

def call(event,x,y,flags,param): 
    global nums #access to edit numbers in a function
    if(event == cv2.EVENT_LBUTTONDOWN):
        print("left")
        nums = (nums + 1)%3
        if nums == 0:
            print("errased")
            p.clear()# clear the list
        elif nums == 1:
            print('first point is set')
            p.append((x,y)) # add to the list "p"
        elif nums == 2:
            print("second point is set")
            p.append((x,y)) # add to the lidt "p"
            print("rectangle created")

    elif(event == cv2.EVENT_RBUTTONDOWN):
        print("right")

nums = 0
p = []
im = cv2.imread("red.png")
cv2.imshow("1",im)
cv2.setMouseCallback("1",call)# for this command "call" and  window should exsist. It appends changes for the window.

while True:

    c_im = np.copy(im)
    
    if(len(p) == 2):
        print("Я РИСУЮ ЧЕТЫРЕХУГОЛЬНИК")
        cv2.rectangle(c_im,p[0],p[1],(0,255,0),10)
    print("Я показываю картинку сim")
    cv2.imshow("1",c_im)
    c_b = cv2.waitKey(20)
    if(c_b == 32):
        if(len(p) == 2):
            print("SPACE")
            cv2.imshow("3",c_im)
            res_im =c_im[p[0][1]:p[1][1],p[0][0]:p[1][0]]
            #napisat 4 scenariya if(p[0][1]> p[1][1]): res_im =c_im[p[1][1]:p[0][1],p[0][0]:p[1][0]]
            cv2.imshow("2",res_im)
            #namef = str(int(time.time()))+".png"
            #cv2.imwrite(namef,res_im)
    elif(c_b == 27):
        break
cv2.destroyAllWindows()

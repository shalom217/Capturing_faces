# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:14:53 2020

@author: shalom
"""

import cv2
import os
from numpy import *
from tkinter import * 
import pandas as pd
from tkinter.filedialog import askopenfilename
root = Tk() 
root.title('Capturing faces')
root['bg']='cyan'
root.geometry('750x150')

e1=Entry(root)
e1.grid(row=0,column=1)
Label(root,text='Please Enter Project Name first:').grid(row=0,column=0) 

def open_file1():
    Label(root,text='Enter escape to quit').grid(row=3)
    file = askopenfilename() #to open the file opening window
    vid = cv2.VideoCapture(file)#reading the video file
    face_cascade = cv2.CascadeClassifier('C:/Users/shalo/Desktop/ML stuffs/DL/haarcascade_frontalface_default.xml')# Load HAAR face classifier
    i=0 
    path1='C:/Users/shalo/Desktop/ML stuffs/DL/os check/%s'%(e1.get()) 
    os.mkdir(path1)#will make a directory 
    print(path1)
    while True:
        r,frame = vid.read();
    
        if r == True:
            frame = cv2.resize(frame,(640,480))
            im1 = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
            face=face_cascade.detectMultiScale(im1,1.3,5)#It takes 3 arguments — the input image, scaleFactor and minNeighbours
            for x,y,w,h in (face):
                cv2.rectangle(frame,(x,y),(x+w,y+h),[255,0,0],4)#arguments respectively input image,start_point, end_point, color, thickness
                i=i+1
                im_f = frame[y:y+h,x:x+w]#to capture from each faces 
                path3 = '%s/%d.png'%(path1,i)
                cv2.imwrite(path3,im_f)#saving the image
        
            cv2.imshow('Video',frame)#display the image
        
            k = cv2.waitKey(1) & 0xff## Stop if escape key is pressed
            if k==27:
                print('faces captured:'+str(i))
                break
        
        else:
            print('faces captured:'+str(i))
            break
            
    e2=Entry(root)
    e2.grid(row=2,column=2)
    Label(root,text='No.of faces captured').grid(row=2,column=1)
    e2.delete(first=0,last=22)
    e2.insert(0,i)
    vid.release()
    cv2.destroyAllWindows()
    
      
def open_file2():
    
    cap = cv2.VideoCapture(0) # Initialize Webcam
# Load HAAR face classifier
    face_cascade = cv2.CascadeClassifier('C:/Users/shalo/Desktop/ML stuffs/DL/haarcascade_frontalface_default.xml')
    iter1=0
    path2='C:/Users/shalo/Desktop/ML stuffs/DL/os check/%s'%(e1.get())
    os.mkdir(path2)#will make a directory 
    print(path2)
    while True:
        
        r,frame = cap.read();#reading from webcam
        frame = cv2.resize(frame,(640,480))#resizing
        im1 = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)#converting to grey scale
        face=face_cascade.detectMultiScale(im1,1.3,5)#It takes 3 arguments — the input image, scaleFactor and minNeighbours
        for x,y,w,h in (face):
            cv2.rectangle(frame,(x,y),(x+w,y+h),[255,0,0],4)
            iter1=iter1+1
            im_f = im1[y:y+h,x:x+w]#to draw rectangle 
            im_f = cv2.resize(im_f,(112,92))  
            cv2.putText(frame,'face No. '+str(iter1),(x,y), cv2.FONT_ITALIC, 1,
                        (255,0,255),2,cv2.LINE_AA)#?
#cv2.putText(image, text, org(x,y), font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])        
            path4 = '%s/%d.png'%(path2,iter1)
            cv2.imwrite(path4,im_f)
        
        cv2.imshow('Webcam',frame)
        
        k = cv2.waitKey(1) & 0xff
        if k==27:
            print('faces captured:'+str(iter1))
            break

    e2=Entry(root)
    e2.grid(row=2,column=2)
    Label(root,text='No.of faces captured').grid(row=2,column=1)
    e2.delete(first=0,last=22)
    e2.insert(0,iter1)
    vid.release()
    cv2.destroyAllWindows()    

btn = Button(root, text ="1.) Select Video File,or", command =lambda:open_file1()) 
btn.grid(row = 1, column = 0)

btn = Button(root, text ="2.) Use web Cam", command =lambda:open_file2()) 
btn.grid(row = 1, column = 1) 
Label(root,text='After selecting any option Enter escape to close the cam or video').grid(row=3)  
mainloop()
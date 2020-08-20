import cv2
import numpy as np


class ColorDescriptor:
 def __init__(self,bins):
   self.bins=bins
 def describe(self,image):
   #image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
   features=[]
   h,w=image.shape[:2]
   cX,cY=(int(w*0.5),int(h*0.5))
   
   segments=[(0,cX,0,cY),(cX,w,0,cY),(0,cX,cY,h),(cX,w,cY,h)]
   
   axesX,axesY=(int(w*0.75)//2,int(h*0.75)//2)  
   ellipmask=np.zeros(image.shape[:2],dtype="uint8")
   cv2.ellipse(ellipmask,(cX,cY),(axesX,axesY),0,0,360,255,-1)
   
   for(startX,endX,startY,endY)in segments :
      cornermask=np.zeros(image.shape[:2],dtype="uint8")
      cv2.rectangle(cornermask,(startX,endX),(startY,endY),255,-1)
      cornermask=cv2.subtract(cornermask,ellipmask)
      
      hist=self.histogram(image,cornermask)
      features.extend(hist)

   hist=self.histogram(image,ellipmask)
   features.extend(hist)
   
   return features
  
 def histogram(self,image,mask):
   hist=cv2.calcHist([image],[0,1,2],mask,self.bins,[0,180,0,256,0,256]) 

   hist=cv2.normalize(hist,hist).flatten()  
   return hist


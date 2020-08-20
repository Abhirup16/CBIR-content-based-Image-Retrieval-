from color_descriptor import ColorDescriptor
import cv2
import argparse
import os

ap=argparse.ArgumentParser()
ap.add_argument("-d","--dataset",required=True,help="Path to the image dataset")
ap.add_argument("-i","--index",required=True,help="Path to where features to be stored")
args=vars(ap.parse_args())

cd=ColorDescriptor((8,12,3))
output=open(args["index"],"w")
"""
for imagepath in glob.glob(args["dataset"]+"/*.png"):
 imageID=imagepath[imagepath.rfind("/")+1: ]
 image=cv2.imread(imagepath)
 
 features=cd.describe(image)
 
 features=[str(f) for f in features]
 output.write("%s%s\n" % (imageID,",".join(features)))"""

basepath=args["dataset"]
for imagepath in os.listdir(basepath):
  imageID=imagepath[ :imagepath.rfind(".")]
  image=cv2.imread(os.path.join(args["dataset"],imagepath))
   
  features=cd.describe(image)
  features=[str(f) for f in features]
  output.write("%s,%s\n" % (imageID,",".join(features)))

output.close()




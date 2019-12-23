import sys
import argparse
import subprocess 
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import glob

import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut):
  count = 0
  vidcap = cv2.VideoCapture(pathIn)
  success,image = vidcap.read()
  success = True
  while success:
    vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
    success,image = vidcap.read()
    print ('Read a new frame: ', success)
    cv2.imwrite( pathOut + "/frame%d.jpg" % count, image)     # save frame as JPEG file
    count = count + 1

def cropVideo(confidence_level,pathIn):
  f = open("/Users/ryanyang/Desktop/yolov3-tiny/VG_AlexeyAB_darknet/results/results.txt", "r")
  frame = False
  ct = 0
  consecutive_thumbs = 0 # cut if above 3
  for line in f:

    if(consecutive_thumbs >= 1):
      ffmpeg_extract_subclip(pathIn, 0, ct, targetname="cropped.mp4")
      break
    if("Start" in line):
      frame = True
      continue
    elif("End" in line):
      frame = False
      ct += 1
      continue
    else:
      if("Thumbs" in line):
        confidence = line.rstrip().split(" ")
        if(float(confidence[1].strip("%") ) > confidence_level):
          consecutive_thumbs += 1


def clearFiles():
  #clear contents of img folder to extract images
  files = glob.glob('/Users/ryanyang/Desktop/yolov3-tiny/VG_AlexeyAB_darknet/exp/in_images/*')
  for f in files:
      os.remove(f)
  open("/Users/ryanyang/Desktop/yolov3-tiny/VG_AlexeyAB_darknet/results/results.txt", 'w').close() #clear the contents of txt file

if __name__=="__main__":
    print("aba")
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--confidence", help="confidence level",default=0.45)
    #a.add_argument("--pathOut", help="path to images")
    args = a.parse_args()
    clearFiles()
    extractImages(args.pathIn, "/Users/ryanyang/Desktop/yolov3-tiny/VG_AlexeyAB_darknet/exp/in_images") # extract frames on images
    subprocess.call("./yolov3-tiny-thumbs.sh") # run yolov3 on frames
    cropVideo(args.confidence,args.pathIn) #crop video based on on yolov3 results
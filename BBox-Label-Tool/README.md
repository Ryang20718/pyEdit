# Project 
Our research lab is working on building a drone to identify damage on aircraft via an autonomous visual inspection

## Parrot Instructions

1. run source /opt/ros/indigo/setup.bash
2. Connect SLAMDUNK with your laptop through USB interface.
3. It will show Wired connection 1 probably, which is the name of the connection. (Use the newest connection)
4. Go to edit connections, click on the wired connection, and then click on edit.
5. Go to Ethernet tab and select MAC address of the SLAMDUNK.
6. Go to IPv4 Setting tab, select change method to shared to other computers in the dropdown menu.
9. use ifconfig to find the name of the usb port of the parrot
10. run `sudo arp-scan --localnet --interface=enp0s20u2` (the last part is the name of the usb port for parrot) to find the ip address.
11. run `export ROS_MASTER_URI=http://192.168.45.1:11311` instead of 192.168.45.1 add the ip of the parrot
12. run `export ROS_HOSTNAME= (insert ip of you your computer after the equals)`
13. run `rosnode list`     you should have the out puts 
Output:
```
/rosout
/slamdunk_node
```
14. run $ `rosparam get /properties/ro_parrot_build_version`    it should output 1.0.0 or the version number of the firmware
the page with instructions to set up the stuff and other features as well: http://developer.parrot.com/docs/slamdunk/#overview

## Training instructions

The following are a modified version of the instructions found on the yolo website

1. Strat by collecting images. the goal is to collect close to 500 img/class 
2. create a new folder in BBox-Label-Tool/Images We are currently trying to divide up our data set into 500 ish image chuncks 
3. run main.py and annotate images. 
4. run the convert.py script to format the annotations in yolo form 
5. Set up the darknet config 
6. run `./darknet detector train cfg/lockheed.data cfg/yolov3.cfg <weights(if needed)>`


### Forked from [puzzledqs/BBox-Label-Tool](https://github.com/puzzledqs/BBox-Label-Tool)
## Improvements
1. Add multi-class support 
2. Change some of the color-candidates for better display
3. Fix the 'Example' filepath for convenience
4. Change the image format from '.JPEG' to '.JPG'

## New Usage
### For multi-class task, modify 'class.txt' with your own class-candidates and before labeling bbox, choose the 'Current Class' in the Combobox and make sure you click 'ComfirmClass' button.

### The remaining usage is the same as the origin one.

------------------------------------

**Contact info**: jxgu1016@gmail.com

------------------------------------

BBox-Label-Tool
===============

A simple tool for labeling object bounding boxes in images, implemented with Python Tkinter.

**Updates:**
- 2017.5.21 Check out the ```multi-class``` branch for a multi-class version implemented by @jxgu1016

**Screenshot:**
![Label Tool](./screenshot.png)

Data Organization
-----------------
LabelTool  
|  
|--main.py   *# source code for the tool*  
|  
|--Images/   *# direcotry containing the images to be labeled*  
|  
|--Labels/   *# direcotry for the labeling results*  
|  
|--Examples/  *# direcotry for the example bboxes*  

Environment
----------
- python 2.7
- python PIL (Pillow)

Run
-------
$ python main.py

Usage
-----
0. The current tool requires that **the images to be labeled reside in /Images/001, /Images/002, etc. You will need to modify the code if you want to label images elsewhere**.
1. Input a folder number (e.g, 1, 2, 5...), and click `Load`. The images in the folder, along with a few example results will be loaded.
2. To create a new bounding box, left-click to select the first vertex. Moving the mouse to draw a rectangle, and left-click again to select the second vertex.
  - To cancel the bounding box while drawing, just press `<Esc>`.
  - To delete a existing bounding box, select it from the listbox, and click `Delete`.
  - To delete all existing bounding boxes in the image, simply click `ClearAll`.
3. After finishing one image, click `Next` to advance. Likewise, click `Prev` to reverse. Or, input an image id and click `Go` to navigate to the speficied image.
  - Be sure to click `Next` after finishing a image, or the result won't be saved. 

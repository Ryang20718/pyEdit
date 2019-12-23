#!/bin/sh

cd VG_AlexeyAB_darknet darknet && ./darknet detector batch cfg/voc.data cfg/yolov3-tiny-thumbs.cfg weights/yolov3-tiny-thumbs_4000.weights batch exp/in_images/ exp/out_images/ > results/results.txt



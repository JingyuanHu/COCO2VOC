#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import argparse
parser = argparse.ArgumentParser(description='The year of COCO :2014 or 2017')
parser.add_argument('--year', default=None,type=str, help='2014 or 2017')
args = parser.parse_args()

year = args.year
COCO_Year = ['2014', '2017']
if year not in COCO_Year:
    raise Exception("You need to choose the year of COCO:2014 or 2017")


nameStr = []

with open("annotations/COCO_train"+year+".json","r+") as f:
    data = json.load(f)

if year == '2014':
    for i in data:
        imgName = "COCO_train2014_" + str(i["filename"]).zfill(12) + ".jpg"
        nameStr.append(imgName)
elif year == '2017':
    for i in data:
        imgName = str(i["filename"]).zfill(12) + ".jpg"
        nameStr.append(imgName)

nameStr = set(nameStr)

path = "train"+year+"/"
for file in os.listdir(path):
    if(file not in nameStr):
        os.remove(path+file)

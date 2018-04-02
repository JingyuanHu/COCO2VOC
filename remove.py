#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os

nameStr = []

with open("annotations/COCO_train2017.json","r+") as f:
    data = json.load(f)
    print("read ready")

for i in data:
    imgName = "COCO_train2017_" + str(i["filename"]).zfill(12) + ".jpg"
    nameStr.append(imgName)

nameStr = set(nameStr)
print(nameStr)
print(len(nameStr))

path = "train2017/"
for file in os.listdir(path):
    if(file not in nameStr):
        os.remove(path+file)

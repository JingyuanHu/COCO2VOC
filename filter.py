#! /usr/bin/env python
#-*-coding=utf-8 -*-
import argparse
import json
import sys

parser = argparse.ArgumentParser(description='The year of COCO :2014 or 2017')
parser.add_argument('--year', default=None,type=str, help='2014 or 2017')
args = parser.parse_args()

year = args.year
COCO_Year = ['2014', '2017']
if year not in COCO_Year:
    raise Exception("You need to choose the year of COCO:2014 or 2017")

className = {
            1:'person'
            }

classNum = [1]

def writeNum(Num):
    with open("annotations/COCO_train"+year+".json","a+") as f:
        f.write(str(Num))

inputfile = []
inner = {}

with open("annotations/instances_train"+year+".json","r+") as f:
    allData = json.load(f)
    data = allData["annotations"]

for i in data:
    if(i['category_id'] in classNum):
        inner = {
            "filename": str(i["image_id"]).zfill(6),
            "name": className[i["category_id"]],
            "bndbox":i["bbox"]
        }
        inputfile.append(inner)
inputfile = json.dumps(inputfile)
writeNum(inputfile)

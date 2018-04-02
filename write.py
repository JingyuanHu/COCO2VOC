#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.dom
import xml.dom.minidom
import os
import cv2
import json

_AUTHOR= 'Hujingyuan'
_SEGMENTED= '0'
_DIFFICULT= '0'
_TRUNCATED= '0'
_POSE= 'Unspecified'

def createElementNode(doc,tag, attr):
    element_node = doc.createElement(tag)
    text_node = doc.createTextNode(attr)
    element_node.appendChild(text_node)
    return element_node

def createChildNode(doc,tag, attr,parent_node):
    child_node = createElementNode(doc, tag, attr)
    parent_node.appendChild(child_node)

def createObjectNode(doc,attrs):
    object_node = doc.createElement('object')
    createChildNode(doc, 'name', attrs['name'],
                    object_node)
    createChildNode(doc, 'pose',
                    _POSE, object_node)
    createChildNode(doc, 'truncated',
                    _TRUNCATED, object_node)
    createChildNode(doc, 'difficult',
                    _DIFFICULT, object_node)
    bndbox_node = doc.createElement('bndbox')
    createChildNode(doc, 'xmin', str(int(attrs['bndbox'][0])),
                    bndbox_node)
    createChildNode(doc, 'ymin', str(int(attrs['bndbox'][1])),
                    bndbox_node)
    createChildNode(doc, 'xmax', str(int(attrs['bndbox'][0]+attrs['bndbox'][2])),
                    bndbox_node)
    createChildNode(doc, 'ymax', str(int(attrs['bndbox'][1]+attrs['bndbox'][3])),
                    bndbox_node)
    object_node.appendChild(bndbox_node)
    return object_node

def writeXMLFile(doc,filename):
    tmpfile =open('tmp.xml','w')
    doc.writexml(tmpfile, addindent=''*4,newl = '\n',encoding = 'utf-8')
    tmpfile.close()
    fin =open('tmp.xml')
    fout =open(filename, 'w')
    lines = fin.readlines()
    for line in lines[1:]:
        if line.split():
            fout.writelines(line)
    fin.close()
    fout.close()

if __name__ == "__main__":
    img_path = "train2017/"
    fileList = os.listdir(img_path)
    if fileList == 0:
        print("Do not find images in your img_path")
        os._exit(-1)

    with open("COCO_train2017.json", "r") as f:
        ann_data = json.load(f)

    current_dirpath = os.path.dirname(os.path.abspath('__file__'))

    if not os.path.exists('Annotations'):
        os.mkdir('Annotations')

    for imageName in fileList:
        saveName= imageName.strip(".jpg")
        print(saveName)

        xml_file_name = os.path.join('Annotations', (saveName + '.xml'))

        img=cv2.imread(os.path.join(img_path,imageName))
        print(os.path.join(img_path,imageName))
        height,width,channel=img.shape
        print(height,width,channel)

        my_dom = xml.dom.getDOMImplementation()

        doc = my_dom.createDocument(None, 'annotation', None)

        root_node = doc.documentElement
        #print(root_node)
        #input()
        createChildNode(doc, 'folder', 'COCO2017', root_node)

        createChildNode(doc, 'filename', saveName+'.jpg',root_node)

        source_node = doc.createElement('source')

        createChildNode(doc, 'database', 'LOGODection', source_node)

        createChildNode(doc, 'annotation', 'COCO2017', source_node)

        createChildNode(doc, 'image','flickr', source_node)

        createChildNode(doc, 'flickrid','NULL', source_node)

        root_node.appendChild(source_node)

        owner_node = doc.createElement('owner')

        createChildNode(doc, 'flickrid','NULL', owner_node)

        createChildNode(doc, 'name',_AUTHOR, owner_node)

        root_node.appendChild(owner_node)

        size_node = doc.createElement('size')

        createChildNode(doc, 'width',str(width), size_node)

        createChildNode(doc, 'height',str(height), size_node)

        createChildNode(doc, 'depth',str(channel), size_node)

        root_node.appendChild(size_node)

        createChildNode(doc, 'segmented',_SEGMENTED, root_node)

        count = 0
        for ann in ann_data:
            if(saveName==("COCO_train2017_" + ann["filename"].zfill(12))):
                count = 1
                object_node = createObjectNode(doc, ann)
                root_node.appendChild(object_node)
            else:
                continue

        if count ==1:
            writeXMLFile(doc, xml_file_name)

import json

className = {
            1:'person'
            }

classNum = [1]

def writeNum(Num):
    with open("COCO_train2017.json","a+") as f:
        f.write(str(Num))

inputfile = []
inner = {}

with open("instances_train2017.json","r+") as f:
    allData = json.load(f)
    data = allData["annotations"]
    print(data[1])
    print("read ready")

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

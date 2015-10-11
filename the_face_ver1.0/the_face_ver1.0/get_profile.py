import json
import os

def getProfile(myPath):
    image_paths = [os.path.join(myPath, f) for f in os.listdir(myPath) if f[0]!='.']
    myList = []
    for image_path in image_paths:
        f = open(image_path)
        tmp = json.loads(f.read())
        dic = {}
        #dic['bio'] = tmp['bio']
        dic['name'] = tmp['first_name'] + ' ' + tmp['last_name']
        dic['age'] = tmp['age_range']['min']
        dic['email'] = tmp['email']
        myList.append(dic)
    return myList

if __name__ == "__main__":
    myPath = "./FacebookData"
    print getProfile(myPath)
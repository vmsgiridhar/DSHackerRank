# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 15:13:15 2018

@author: C5232886
"""
from base64 import b64encode, b64decode 
from json import dumps, loads, JSONEncoder
import pickle, sys, os,json

argAlert = 'Argument missing: Mount point is not supplied.'

class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (list, dict, str, int, float, bool, type(None))):
            return super().default(obj)
        return {'_python_object': b64encode(pickle.dumps(obj)).decode('utf-8')}

def as_python_object(dct):
    if '_python_object' in dct:
        return pickle.loads(b64decode(dct['_python_object'].encode('utf-8')))
    return dct
    
def gre_2_processor(*args, startPath = '.'):
    #format
    d = {"files":[]}
    #reading any directory as an argument from user input
    mountPoint = sys.argv[1:][0]
    #indexing search to mount point
    os.chdir(mountPoint)
    #list all the files
    for dirPath, dirName, fileName in os.walk(mountPoint, topdown = "True"): #os.walk returns a generator
        for file in fileName:
            filePath = os.path.join(dirPath, file)
            fileSize = os.path.getsize(filePath)
            d["files"].append({filePath, fileSize})
    print(type(d))
    return(d)
#executing the function
data = gre_2_processor()
j = json.dumps(data, cls=PythonObjectEncoder)
j0 = loads(j ,object_hook=as_python_object)
print(j0)
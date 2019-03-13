# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 15:31:53 2018

@author: GIRIDHAR
"""

#importing required libraries
import sys, os, json
from json import dumps, loads, JSONEncoder, JSONDecoder 
import pickle

#constants
argMissing = 'Please enter the mount point as argument.'
data = {"files":[]}
'''
Using a custom JSONEncoder, JSONDecoder to cleanly 
encode Python datastructres
like sets because by default sets are not JSON 
serializable.
'''
#Subclassing JSONEncoder and overriding the default method to handle set
class SetEncoder(json.JSONEncoder):
    def default(self, set_fp_fs):
        if isinstance(set_fp_fs, set):
            return (list(set_fp_fs))
        else:
            super.default(self, set_fp_fs)
#decoding the list to a set again
def listFpFsAsSet(dct):
    temp = {"files":[]}
    for i in range(len(dct["files"])):
        temp["files"].append(set(dct["files"][i]))
    return temp
#logic function
def processorFiles():
    #read the arguments being passed at CLI
    inputMPList = sys.argv[:]
    #console(inputMP) #Check
    if validateMountPoint(inputMPList) is True:
        enteredMountPoint = inputMPList[1]
        #indexing search to mount point
        os.chdir(enteredMountPoint)
        #list all the files
        for dirPath, dirName, fileName in os.walk(enteredMountPoint, topdown = "True"): #os.walk returns a generator
            for file in fileName:
                filePath = os.path.join(dirPath, file)
                fileSize = os.path.getsize(filePath)
                #console(filePath, fileSize) #Check
                data["files"].append(set([filePath, fileSize]))
        #data = {"files":[{filePath,fileSize}]}
        ENC = json.dumps(data, indent=4, separators=(",",":"), cls=SetEncoder)
        #console(ENC, type(ENC)) #Check
        console(json.loads(ENC, object_hook=listFpFsAsSet)) #Final Print
    else:
        console(argMissing)

#json Dumper
def jsonDumps():
    pass

#input validation function
def validateMountPoint(impl):
    if len(impl) > 1 and impl[1]:
        #console('Mount Point present') #Check
        return True
    else:
        return False

#console function - for testing
def console(*args):
    for _ in args:
        print(_) #Check
    #pass

#to check the execution of module
if __name__ == '__main__':
    processorFiles()

#notes
'''
json.dumps(x,indent=4,seperators=(item_separator, 
key_separator))
a python tuple returns as a list after decoding
{'files': [
        {'C:\\Users\\C5232886\\Desktop\
\Python_Prac\\GRE\\Test\\News.txt', 5915}, 
        {17664, 'C:\\Users\\C5232886\\Desktop\
\Python_Prac\\GRE\\Test\\ProfilePic.jpeg'}, 
        {124298, 'C:\\Users\\C5232886\\Desktop\
\Python_Prac\\GRE\\Test\\WebProject.zip'}
        ]
}
'''
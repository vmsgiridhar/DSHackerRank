# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 15:10:20 2018

@author: C5232886
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 15:31:53 2018
@author: GIRIDHAR
"""

#importing required libraries
import sys, os, json
from json import dumps, loads, JSONEncoder, JSONDecoder

#constants
ErrorMap = {"noMountPoint": 'Please enter the mount point as argument.',
            "badMountPoint": 'Please recheck the mount point given. System is not able to find it.'}
#noMountPoint = 'Please enter the mount point as argument.'
#fileNotFound = 'Please recheck the mount point given. System is not able to find it.'
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
def listFpFsAsSet(lis):
    temp = {"files":[]}
    for i in range(len(lis["files"])):
        temp["files"].append(set(lis["files"][i]))
    return temp

#logic function
def processorFiles():
    #read the arguments being passed at CLI
    inputMPList = sys.argv[:]
    #console(inputMP) #Check
    try:
        #if validateMountPoint(inputMPList) is True:
            validateMountPoint(inputMPList)
            #enteredMountPoint = inputMPList[1]
            #indexing search to mount point
            #os.chdir(enteredMountPoint)
            #list all the files
            for dirPath, dirName, fileName in os.walk(inputMPList[1], topdown = "True"): #os.walk returns a generator
                for file in fileName:
                    filePath = os.path.join(dirPath, file)
                    fileSize = os.path.getsize(filePath)
                    #console(filePath, fileSize) #Check
                    data[(lambda x:[*x])(data)[0]].append(set([filePath, fileSize])) #list(data.keys())[0] - get first key
            #data = {"files":[{filePath,fileSize}]}
            #console(data)
            ENC = json.dumps(data, indent=4, separators=(",",":"), cls=SetEncoder)
            #console(ENC, type(ENC)) #Check
            console(json.loads(ENC, object_hook=listFpFsAsSet)) #Final Print
        #else:
            #raise Exception({"Error":argMissing})
    except Exception as e:
        console(e)

#input validation function
def validateMountPoint(impl):
    if len(impl) > 1 and impl[1]:
        #console('Mount Point present') #Check
        try:
            os.chdir(impl[1])
        except:
            raise Exception(ErrorMap["badMountPoint"])
        return True
    else:
        raise Exception(ErrorMap["noMountPoint"])

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
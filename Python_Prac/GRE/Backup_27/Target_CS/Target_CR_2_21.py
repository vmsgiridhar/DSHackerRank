# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 15:31:53 2018
@author: GIRIDHAR
"""

# importing required libraries.
import sys
import os
import json

# constants.
ErrorMap = {"noMountPoint": 'Please enter the mount point as argument.',
            "badMountPoint": 'Please recheck the mount point given. System is not able to find it.'}
data = {
        "files": []
}

class SetEncoder(json.JSONEncoder):
    """Subclassing JSONEncoder and overriding the defualt method to handle sets.
    """
    def default(self, set_fp_fs):
        if isinstance(set_fp_fs, set):
            return (list(set_fp_fs))
        else:
            super.default(self, set_fp_fs)
            
def listFpFsAsSet(lis):
    """Converting the list(which is returned by SetEncoder) to a set again.
    """
    temp = {
            "files": []
    }
    for i in range(len(lis["files"])):
        temp["files"].append(set(lis["files"][i]))
    return temp

def processorFiles():
    """This is the function that handles the complete logic and flow
    """
    inputMPList = sys.argv[:]       # read the arguments being passed at CLI
    try:
            validateMountPoint(inputMPList)
            for dirPath, dirName, fileName in os.walk(inputMPList[1], topdown = "True"): 
                for file in fileName:
                    filePath = os.path.join(dirPath, file)
                    fileSize = os.path.getsize(filePath)
                    data[(lambda x:[*x])(data)[0]].append(set([filePath, fileSize])) # list(data.keys())[0] - get first key
            ENC = json.dumps(data, indent=4, separators=(",",":"), cls=SetEncoder)
            console(json.loads(ENC, object_hook=listFpFsAsSet)) # Final Print
    except Exception as e:
        console(e)

def validateMountPoint(impl):
    """This validates the Mount Point being supplied at CLI.
    """
    if len(impl) > 1 and impl[1]:
        try:
            os.chdir(impl[1])
        except:
            raise Exception(ErrorMap["badMountPoint"])
        return True
    else:
        raise Exception(ErrorMap["noMountPoint"])

def console(*args):
    """This function prints the arguments passed on to console.
    
    Used for testing and printing purposes.
    """
    for _ in args:
        print(_)

# call to the processing function. 
if __name__ == '__main__':
    processorFiles()
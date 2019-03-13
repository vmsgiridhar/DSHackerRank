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
ERROR_MAP = {"noMountPoint": 'Please enter the mount point as argument.',
            "badMountPoint": 'Please recheck the mount point given. System is not able to find it.'}
RESULT = {
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
            
def conv_lis_to_set(self):
    """Converting the list(which is returned by SetEncoder) to a set again.
    
    The List gets converted to a set and appends to final result template
    """
    res_temp = {
            "files": []
    }
    for i in range(len(self["files"])):
        res_temp["files"].append(set(self["files"][i]))
    return res_temp

def processor_files():
    """This is the function that handles the complete logic and flow
    """
    input_mount_point_list = sys.argv[:]       # read the arguments being passed at CLI
    try:
            validate_mount_point(input_mount_point_list)
            for dirPath, dirName, fileName in os.walk(input_mount_point_list[1], topdown = "True"): 
                for file in fileName:
                    file_path = os.path.join(dirPath, file)
                    file_size = os.path.getsize(file_path)
                    RESULT[(lambda x:[*x])(RESULT)[0]].append(set([file_path, file_size])) # list(RESULT.keys())[0] - get first key
            enc_data = json.dumps(RESULT, indent=4, separators=(",",":"), cls=SetEncoder)
            console(json.loads(enc_data, object_hook=conv_lis_to_set)) # Final Print
    except Exception as err:
        console(err)

def validate_mount_point(self):
    """This validates the Mount Point being supplied at CLI.
    
    Mount Point as argument gets validated.
    """
    if len(self) > 1 and self[1]:
        try:
            os.chdir(self[1])
        except:
            raise Exception(ERROR_MAP["badMountPoint"])
        return True
    else:
        raise Exception(ERROR_MAP["noMountPoint"])

def console(*args):
    """This function prints the arguments passed on to console.
    
    Used for testing and printing purposes.
    """
    for entry in args:
        print(entry)

# call to the processing function. 
if __name__ == '__main__':
    processor_files()
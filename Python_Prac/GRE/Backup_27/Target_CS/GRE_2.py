# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 12:56:49 2018

@author: C5232886

Input: This program should take a mount point on the file system as an argument
Processing: List all the files and their disk usage
Output: Output the File names and the disk usage in JSON format

Result: Not exactly as how expected. We get the strings. Should try framing the output in reverse - Updated at 2:47 AM
"""
#importing required libraries
import sys, os, json

#To customize
argAlert = 'Argument missing: Mount point is not supplied.'
output = {"files":[]}

#function to form output.
def fileSizeJSONfier(filePath, fileSize):
    bindFileData = '{' + filePath + ',' + str(fileSize) + '}'
    #bindFileData = set([filePath, fileSize])
    output["files"].append(bindFileData)

#function to process the files and memory occupied
def gre_2_processor(*args, startPath = '.'):
    
    #reading any directory as an argument from user input
    mountPoint = sys.argv[1:][0]
    if mountPoint == '':
        print(argAlert)
    else:
        #indexing search to mount point
        os.chdir(mountPoint)
        #checking the existing mp
        #print(os.getcwd()) 
        #list all the files
        for dirPath, dirName, fileName in os.walk(mountPoint, topdown = "True"): #os.walk returns a generator
            for file in fileName:
                filePath = os.path.join(dirPath, file)
                fileSize = os.path.getsize(filePath)
                #calling the function
                fileSizeJSONfier(filePath, fileSize)
    return(json.dumps(output, indent=4, separators=(", ", ": ")))
    #return(json.dumps(output))
#executing the function
print(gre_2_processor())


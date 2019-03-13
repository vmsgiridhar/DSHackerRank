# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 12:38:59 2018

@author: C5232886
"""

fileDirectory = open('FileReader.txt','r')
fileNames =  [i for i in fileDirectory.readlines()] 
#list comprehension to collect the fileNames
readContents = [i.split('\n')[0] for i in open(fileNames[0].split('\n')[0],'r').readlines()] 
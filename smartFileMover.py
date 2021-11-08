from pathlib import Path
import sys
import pandas as pd
from random import shuffle
import random
import numpy as np
import os
import re
from mutv1 import fileListCopy


inHastePath = r'D:\Developed\Automation\inHaste'


def dividesmartly_helper(filename,tp,targetPath):
    filepath = Path(inHastePath) / filename
    if not Path(filepath).is_file():
        return
    with open(filepath,'r') as fp:
        filesToMove = [x.rstrip() for x in fp.readlines() if targetPath in x]
    if len(filesToMove) > 0:
        fileListCopy(filesToMove,tp)
        

def dividesmartly(targetPath,filemovingdict):
    for key,tp in filemovingdict.items():
        dividesmartly_helper(key,tp,targetPath)

def main():
    targetPath = r'D:\Developed\VFS\RandyVideo\xdivision'
    filemovingdict = {'1.txt':r'D:\paradise\stuff\Essence\FS\yummyClips\deletable','2.txt':r'D:\paradise\stuff\Essence\FS\yummyClips\TheekThak','3.txt':r'D:\paradise\stuff\Essence\FS\yummyClips\SachMe'}
    dividesmartly(targetPath,filemovingdict)
    
main()
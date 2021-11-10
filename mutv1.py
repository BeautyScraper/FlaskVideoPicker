from pathlib import Path
import sys
import pandas as pd
from random import shuffle
import random
import numpy as np
import os
import re
import subprocess

def listToFile(l,filename='D:\\ListFile.txt'):
    k = [x.strip('\n')+'\n' for x in l]
    k = list(set(k))
    with open(filename,'w') as fp:
        fp.writelines(k)

def FastCopy(txtFileName,dstination):
    if not Path(txtFileName).is_file():
        return
    fastCopyLocation = r"C:\app\FSC\FastCopy.exe"
    cmdTemplate = '''%0 /log /cmd="force_copy" /auto_close /force_close /srcfile=%1 /to="%2" '''
    cmd = cmdTemplate.replace('%0',fastCopyLocation)
    cmd = cmd.replace('%1',txtFileName)
    cmd = cmd.replace('%2',dstination)
    print(cmd)
    # import pdb;pdb.set_trace()
    # subprocess.check_output(cmd.split(' '))
    os.system(cmd)        
        
def inputWithinTime(inputString='',timelimit=10):
    import time
    print(inputString)
    for i in range(timelimit):
        time.sleep(1)
        print(i+1)
        
def moveByFastCopy(txtFileName,dstination):
    if not Path(txtFileName).is_file():
        return
    fastCopyLocation = r"C:\app\FSC\FastCopy.exe"
    cmdTemplate = '''%0 /log /cmd="move" /auto_close /force_close /srcfile="%1" /to="%2" '''
    cmd = cmdTemplate.replace('%0',fastCopyLocation)
    cmd = cmd.replace('%1',txtFileName)
    cmd = cmd.replace('%2',dstination)
    print(cmd)
    # import pdb;pdb.set_trace()
    os.system(cmd)

def is_removable(dp,ignoreExtensions):
    for ie in ignoreExtensions:
        [fp for fp in dp.glob(ignoreExtensions)]
    
def redwine(dirPath,ignoreExtensions=['*.jp*g']):
    '''remove empty dir with ignoring named extensions'''
    if type(dirPath) != type(Path.cwd()):
       dirPath = Path(dirPath) 
    for dp in dirPath.rglob('*'):
        if not dp.is_dir():
            continue
        if is_removable(dp,ignoreExtensions):
            dp.rmtree()
            
def fileListCopy(fileList,dstination):
    if len(fileList) == 0:
        return
    tempFileName = str(hash(tuple(fileList)))+'.txt'
    listToFile(fileList,tempFileName)
    moveByFastCopy(tempFileName,dstination)
    Path(tempFileName).unlink()

def frad(ext='*.mkv'):#fileRenameAccordingToDir 
    validFiles = Path.cwd().rglob(ext)
    for vf in validFiles:
        # import pdb;pdb.set_trace()
        fn = re.search('^(\d+)$',vf.stem)
        
        if fn:
            nfn = vf.parent.stem + '-' + fn[0] + vf.suffix
            vf.rename(nfn)
        elif len(vf.stem) < 8:
            nfn = vf.parent.stem + vf.stem + vf.suffix
            print(nfn)
            vf.rename(nfn)
            
            # fn[0]
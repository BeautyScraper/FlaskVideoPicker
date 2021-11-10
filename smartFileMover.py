from pathlib import Path
import sys
import pandas as pd
from random import shuffle
import random
import numpy as np
import os
import re
from mutv1 import FastCopy
from mutv1 import moveByFastCopy


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
def moveSmartly(masterTable):
    for index,row in masterTable.iterrows():
        if '@move' not in row['filename']:
            FastCopy(row['filename'],row['Path'])
        if '@move' in row['filename']:
            moveByFastCopy(row['filename'],row['Path'])
        if Path(row['filename']).is_file():
            os.remove(row['filename'])
        # import pdb;pdb.set_trace()
def main():
    csvFilePath = 'config.csv'
    df = pd.read_csv(csvFilePath)
    moveSmartly(df)
    
if __name__ == '__main__':    
    main()
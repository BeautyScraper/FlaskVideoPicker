from flask import Flask, render_template, url_for, request, redirect
import shutil
from pathlib import Path
import random
import re
import argparse
import os
import atexit
import pandas as pd

from bluevs import vsblueprint

app = Flask(__name__)

cnfLinks = []

@app.route('/')
def main():
    print(cnfLinks)
    return render_template('index.html',links=cnfLinks)
    

if __name__ == '__main__':
    cnffiledir = Path.cwd() / 'configs'
    for cnffile in cnffiledir.glob('*.cfg'):
        print('hi')
        x = vsblueprint()
        bp = x.createbp(str(cnffile))
        app.register_blueprint(bp,url_prefix='/%s' % cnffile.stem)
        cnfLinks.append(cnffile.stem)
    app.run(host='0.0.0.0',port=5002)
    print(app.url_map)
# inputDir = r'D:\paradise\stuff\Images\walls'


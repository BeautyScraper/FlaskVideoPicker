from flask import Flask, render_template, url_for, request, redirect, Blueprint
import shutil
from pathlib import Path
import random
import re
import argparse
import os
import atexit
import pandas as pd
from smartFileMover import moveSmartly

# inputDir = r'D:\paradise\stuff\Images\walls'




# def dir_path(string):
    # if os.path.isdir(string):
        # return string
    # else:
        # try:
            # _ = Path(string)
        # except:
            # raise NotADirectoryError(string)
    # return string

# parser = argparse.ArgumentParser()

# parser.add_argument('--inputConfig',type=dir_path,default='config')
# parser.add_argument('--port', type=int,default= 5000)

# args = parser.parse_args()

# listOfFilesDelete = []
# cnffile = args.inputConfig
# inputDir = r'C:\Heaven\YummyBaked\SuperWemon4\SuperWemon1\club9'
# currentImagePath = None
# cdir = []


# allImages =  random.shuffle(allImages)

class vsblueprint:

    def createbp(self,cnffile):
        delPath = Path(r'D:\paradise\stuff\Essence\FS\yummyClips\deletable')
        delPathfn = delPath.name + '_into@move.txt'
        # cnffile = cnffile
        cdir = []
        with open(cnffile,'r+') as fp: 
           inputDir = fp.readline().strip()
           for x in fp.readlines():
                line = x.strip()
                cdir.append(line)
        mastermovertablefn = Path(cnffile).stem + '.csv'
        csvdata = [[Path(x).name+'_into.txt', x] for x in cdir] + [[delPathfn,str(delPath)]]
        df = pd.DataFrame(csvdata,columns=['filename', 'Path'])
        if Path(mastermovertablefn).is_file():
            Path(mastermovertablefn).unlink()
        df.to_csv(mastermovertablefn)
        # with open(cnffile,'r+') as fp:
            # inputDir = random.choice(fp.readlines()).strip()
        inputDirP = Path(inputDir)
        allImages = [x for x in inputDirP.glob('*.mkv')] + [x for x in inputDirP.glob('*.mp4')]
        # random.shuffle(allImages)
        # atexit.register(closingAction)     
        app = simple_page = Blueprint('config', __name__,static_folder=inputDirP)

        @app.route('/')
        def main():
           if len(allImages) <= 0:
                return 'No images left in the directory'
           imgfp = imageRender()
           cpdir = [Path(x).name for x in cdir]
           return render_template("template.html", name=imgfp.name, outDirs=cpdir)
           # return 'hello world'

        @app.route('/noteFilePaths',methods=['POST', 'GET'])
        def noteDownFilename():
            print(request.args)
            try:
                deletepartialRederedFiles()
            except:
                pass
            filename = request.args['imgfilename']
            dstfp = inputDirP / filename
            for k in request.args:
                v = request.args[k]
                print(k,v)
                
                if 'category' not in k:
                    continue
                # import pdb;pdb.set_trace()
                index = int(re.search('\d+',k)[0])
                fcafptm = csvdata[index][0] #file contain all files paths to move
                with open(fcafptm,'a+') as fp:
                    fp.write(str(dstfp) + '\n')
                # outfilepath = Path(cdir[index]) / filename
                
                # shutil.copy(dstfp, outfilepath        
            # print(request.args['category1']).
            with open(delPathfn,'a+') as fp:
                fp.write(str(dstfp) + '\n')
            return redirect(url_for('config.main'))

        @app.route('/move')
        def MoveFiles():
            moveSmartly(df)
            return redirect(url_for('config.main'))
            
        def getSourceFilePath(filename):
            tk = filename
            dirName = re.search('(.*) @hudengi (.*) W1t81N (.*)',str(tk))[2]
            filename = re.search('(.*) @hudengi (.*) W1t81N (.*)',str(tk))[3]
            srcPath = getThisFile(filename,dirName)
            return srcPath
            
        def getThisFile(sourceFile,parentDir,srclistFilePath=r'D:\Developed\Automation\fnr\TargetDirs.opml'):
            with open(srclistFilePath,'r') as fp:
                srcFileList = fp.readlines()
            # srcFileList.append(r'C:\bekar')
            for srself.cdir in srcFileList:
                dirP = Path(srself.cdir.rstrip())
                srcPath = dirP / parentDir / sourceFile
                # import pdb;pdb.set_trace()
                if srcPath.is_file():
                    return srcPath
                return None    
        # def deletepartialRederedFiles():
            # global listOfFilesDelete
            # if len(listOfFilesDelete) > 0:
                # [x.unlink() for x in listOfFilesDelete]
                # listOfFilesDelete = []
          
        def imageRender():
            # global currentImagePath
            imgfp = allImages.pop()
            # dstfp = Path(__file__).parent / 'static' / 'images' / imgfp.name
            # dstfp.parent.mkdir(parents=True,exist_ok=True)
            # shutil.move(imgfp,dstfp)
            return imgfp
        return app

if __name__ == '__main__':
   app.run(host="0.0.0.0",port=args.port)

   
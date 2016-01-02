#!/usr/bin/env python
# Author: Shunfa Zhang
# Date: 2016/1/2
# Do the same thing as repalceOrderPic.lua

import os
import os.path
import math
import shutil

def copyFile(orgDir, targetDir, sourceName):
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)

    sourceFile = os.path.join(orgDir, sourceName)
    targetFile = os.path.join(targetDir, sourceName)
    shutil.copy(sourceFile, targetFile)


def removeFile(targetFile):
    if os.path.isdir(targetFile):
        for item in os.listdir(targetFile):
            itemPath = os.path.join(targetFile, item)
            os.remove(itemPath)

        print "removeDir: -> %s" % targetFile
        os.rmdir(targetFile)

    if os.path.isfile(targetFile):
        print "removeFile : -> %s" % targetFile
        os.remove(targetFile)

def copyFileForUser(orgDir, targetDir, picMode):
    for i in range(81, 99):
        picOrgName = picMode % i
        for parent, dirnames, filenames in os.walk(orgDir):
            for filename in filenames:
                if picOrgName == filename:
                    print "copyFile : -> %s" % filename
                    copyFile(orgDir, targetDir, filename)

def renameFileForUser(dirc):
    for i in range(81, 99):
        picOrgName = picOrgMode % i
        picName = picMode % i
        for parent, dirnames, filenames in os.walk(dirc):
            for filename in filenames:
                if picOrgName == filename:
                    orgPath = os.path.join(dirc, picOrgName)
                    targetPath = os.path.join(dirc, picName)
                    print "renameFile : -> %s" % filename
                    os.rename(orgPath, targetPath)

# just modify this for the different dirertionary
#orgDir = actorDir
#targetDir = actorTargetDirc
# just modify this for the different dirertionary

#copyFileForUser(orgDir, targetDir, picOrgMode)
#renameFileForUser(targetDir)
#copyFileForUser(targetDir, orgDir, picMode)
#removeFile(targetDir)


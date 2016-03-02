#!/usr/bin/env python
# -*- coding: cp936 -*-
# Author: Shunfa Zhang
# Date: 2016/3/2

import os
import os.path
import math
import shutil

soundPath = "../soundListDircitionary"
soundOutPath = "../soundOut.txt"
xySoundPath = "res/sound/ui/"

def getSoundKey(soundStrList):
    soundStrListLen = len(soundStrList)
    ret = ""
    if soundStrListLen > 0:
        ret = ret + str(soundStrList[1])
        for i in range(2, soundStrListLen):
            ret = ret + str(soundStrList[i]).title()

        return str(ret)

def writeSoundOutFile(string):
    try:
        f = open(soundOutPath, "a+")
        f.write(string)
    finally:
        if f:
            f.close()

def cleanSoundOutFile():
    try:
        f = open(soundOutPath, "w")
        f.write("")
    finally:
        if f:
            f.close()

def addSpaceStr(strLen):
    alignLen = 20
    spaceStr = " "
    ans = ""
    if strLen <= alignLen:
        return spaceStr * (alignLen-strLen)
    else:
        return ""

for parent, dirnames, filenames in os.walk(soundPath):
    cleanSoundOutFile()
    for filename in filenames:
        soundPath = "{ " + "soundPath = \"" + xySoundPath + "\", "
        soundName = "soundName = \"" + filename + "\""
        loopSuffix = ", loop = false" + " },"

        soundNameStr = os.path.splitext(filename)[0]
        soundStrList = soundNameStr.split("_")

        soundKey = getSoundKey(soundStrList)
        spaceNum = addSpaceStr(len(soundKey))

        ans = "[\"" + soundKey + "\"]" + spaceNum + " = " + soundPath + soundName + loopSuffix + "\n"

        writeSoundOutFile(ans)

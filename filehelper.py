import os
from os import listdir
from os.path import isfile, join
import glob
import subprocess

def GetFilesInDirectory(dirpath):
    return [f for f in listdir(dirpath) if isfile(join(dirpath, f))]
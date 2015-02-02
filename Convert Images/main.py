#!/Users/wgillis/anaconda/bin/python
__author__ = 'wgillis'

from PIL import Image
import os
import argparse
import math


commandLineParser = argparse.ArgumentParser(description='Resizes and changes format of images in pwd')

h = """New size of picture based on original size, in float form
    i.e. -s 0.25 makes the image 4 times smaller.
    Works with .tif and .bmp files"""

commandLineParser.add_argument('-s', dest='size', type=float, help=h)
args = commandLineParser.parse_args()
scale = args.size

cd = os.getcwd()

# rootPath = os.path.realpath(os.path.join((os.path.realpath(os.path.join(cd, '../../'))), 'Lab Data/Pictures'))

rootPath = cd


def bmpOrTif(filename, files):
    """
    Finds original files if they end with one of these file extensions
    :param filename: filename of png (str)
    :param files: list of files in this folder (list)
    :return: original file name (str)
    """
    for f in files:
        if f[:-4] == filename and f.endswith(('.tif', '.bmp', '.tiff')):
            return f
    return None


# walks through all folders within the current directory and checks for these large files
for root, dirnames, filenames in os.walk(rootPath):

    for filename in filenames:
        if filename.endswith('.png') :
            im = Image.open(os.path.join(root, filename))
            wid, hei = im.size
            originalFile = bmpOrTif(filename[:-4], filenames)
            if originalFile:
                im2 = Image.open(os.path.join(root, originalFile))
                wid2, hei2 = im2.size
                if wid/wid2 == scale or hei/hei2 == scale:
                    print('Image {0} at {1} has previously been scaled and converted to this size'.format(filename, root))
                    continue
        elif filename.endswith(('.tif', '.bmp', '.tiff')):
            im = Image.open(os.path.join(root, filename))
            wid, hei = im.size
            newSize = (math.floor(wid*scale), math.floor(hei * scale))
            newIm = im.resize(newSize)
            try:
                newIm.save(os.path.join(root, filename[:-4] + '_{0}px_by_{1}px_'.format(*newSize) + '.png'))
                print('Image {0} has been saved successfully at {1}'.format(filename, root))
            except Exception as e:
                print('Error', e)
                print(os.path.join(root, filename))
                print('Process aborted before fully finishing')
                raise e


print('Process finished successfully')

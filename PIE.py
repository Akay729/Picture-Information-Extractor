from PIL import Image
from PIL.ImageStat import Stat
import numpy as np
from tabulate import tabulate
import os
import argparse

def pathFolder():
    '''go from the current folder through "files" to "images" and print a list of element'''

    if 'files' in os.listdir():
        images_folder = os.getcwd() + "\\files\\images"
        return os.listdir(images_folder) 

    else:
        print("Folder not found")
        return None

def getColorLayer(img):
    '''Get a img and return a np.array of it '''
    imgsArray = np.asarray(img)

    # Greyscale
    if type(img.getpixel((0, 0))) == int:
        grayscale = np.mean(imgsArray)
        return grayscale, 0, 0, 0, 0

    # RGB AND RGBA
    elif type(img.getpixel((0, 0))) == tuple:
        colors_parameters = [0]
        matrix_averege = np.mean(imgsArray, axis=0)
        rgb_averege = np.mean(matrix_averege, axis=0)
        rgb_averege = np.round(rgb_averege, 2)

        for i in rgb_averege:
            colors_parameters.append(i)
        return colors_parameters

    else:
        print("something went worng")
        return None

def tabulation():
    table = []
    headers = ["Name", "Height", "Width", "Grayscale", "R", "G", "B", "ALPHA"]

    if pathFolder() != None:

        for path_image in pathFolder():
            img = Image.open(img)
            width, height = img.size()
            img_layer = getColorLayer(img)
    else:
        print("tabulation Failed")


def main():
    img = Image.open("trump.jpeg")
    print(getColorLayer(img))
    '''
    img_layer = np.insert(img_layer,0,0)
    table_row = np.insert(img_layer,4,0)'''


if __name__ == '__main__':
    main()





#print(getColorLayer(img))'''

#Getting RGB value 
#print(img.getpixel((0, 0)))
#print(np.mean(a))
#Stat._getmean(img)




        
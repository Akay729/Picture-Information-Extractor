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
        files = os.listdir(images_folder)
        return[files, images_folder]

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
        colors_parameters = [0.00]
        matrix_averege = np.mean(imgsArray, axis=0)
        rgb_averege = np.mean(matrix_averege, axis=0)
        rgb_averege = np.round(rgb_averege, 2)

        for i in rgb_averege:
            colors_parameters.append(i)
        return colors_parameters

    else:
        print("something went worng")
        return None


def table_row(path, image_name, img):

    width, height = list(img.size)    
    img_layer = list(getColorLayer(img))
    if len(img_layer) == 5:
        return[image_name, height, width]+img_layer
    return [image_name, height, width]+img_layer+[0]


def main():
    image_extesion = ['.ai', '.bmp', '.gif', '.ico', '.jpeg', '.jpg', '.png', '.ps', '.psd', '.svg',
         '.tif', '.tiff']
    location = pathFolder()
    table = []
    heads = ["Name", "Height", "Width", "Grayscale", "R", "G", "B", "ALPHA"]
    
    for image_name in location[0]:
        path = location[1] +f"\\{image_name}"
        img = Image.open(path)
        getColorLayer(img)
        table.append(table_row(path, image_name, img))
    print(tabulate(table,headers=heads))


if __name__ == '__main__':
    main()


#print(getColorLayer(img))'''
#Getting RGB value 
#print(img.getpixel((0, 0)))
#print(np.mean(a))
#Stat._getmean(img)
        
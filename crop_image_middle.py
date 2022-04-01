import cv2 as cv
import os.path
import glob

input_path  = "D:/test/original/"
output_path = "D:/test/after/"

def splitmid(pngfile,outdir):
    img = cv.imread(pngfile)

    imgSize = img.shape[0:2]
    h = imgSize[0] 
    w = imgSize[1]

    #Set the cropping range
    crop_h  = int((1/4)*h)
    crop_h1 = int((3/4)*h)
    crop_w  = int((1/4)*w)
    crop_w1 = int((3/4)*w)

    crop_img = img[crop_h : crop_h1 , crop_w :crop_w1 ] # [y:y1, x:x1]

    name = os.path.splitext(os.path.basename(pngfile))
    newname = name[0]+".png"
    cv.imwrite(os.path.join(outdir,newname),crop_img)

for pngfile in glob.glob(input_path + "*.png"): 
    splitmid(pngfile,output_path)


import os
from datetime import datetime
import numpy as np
import cv2
import natsort
from background_light import getLargestDiff, backgroundLight
from transmission_map import estimate_t, refine_t
from adaptive_exposure_map import adaptiveExposureMap, applyAdaptiveMap
from BG_dehazing import BGDehaze


startTime = datetime.now()

folder = folder = "C:\\Academics\\5th Sem\\CS517 DIPA\\Project\\Underwater Image Color Restoration\\GBdehazingRCorrection"
imagesPath = folder + '\\images'
resultPath = folder + '\\result'

images = os.listdir(imagesPath)

for imgName in images:
    imgPath = imagesPath + '\\' + imgName
    prefix = imgName[:imgName.index('.')]

    if os.path.isfile(imgPath):
        print("Reading Image : ", imgName)
        
        # Reading image
        img = cv2.imread(imgPath)
        
        # Normalizing intensities from [0,255]
        i_min = img.min()
        i_max = img.max()
        img = (img - i_min) / (i_max - i_min) * 255

        # finding largest difference between 3 color channels
        largestDiff = getLargestDiff(img, 9)
        print("Largest Difference : ", largestDiff)

        bgLight, bgLightGB, bgLightRGB = backgroundLight(largestDiff, img)

        print("Background Light RGB: ", bgLightRGB)
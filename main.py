import os
from datetime import datetime
import numpy as np
import cv2
import natsort
from background_light import getLargestDiff, backgroundLight
from transmission_map import estimate_t, refine_t
from adaptive_exposure_map import adaptiveExposureMap, applyAdaptiveMap
from GB_dehazing import GBDehaze
from R_correction import correctRChannel

startTime = datetime.now()

folder = "C:\\Academics\\5th Sem\\CS517 DIPA\\Project\\underwater-image-restoration"
imagesPath = folder + '\\sample_images'
resultPath = folder + '\\result'

images = os.listdir(imagesPath)
windowSize = 9
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

        print("Starting GB Dehazing...")
        restored_gb = GBDehaze(img, windowSize)

        cv2.imwrite(resultPath + '\\' + prefix + '_GBDehazed.jpg', restored_gb)
        
        print("Starting R channel correction...")
        restored = correctRChannel(img, restored_gb)

        cv2.imwrite(resultPath + '\\' + prefix + '_RCorrection.jpg', restored)

        print("Generating Adaptive Exposure Map...")
        S_x = adaptiveExposureMap(img, restored)

        print("Applying Adaptive Exposure Map...")
        restored = applyAdaptiveMap(restored, S_x)

        print("=======>" , resultPath + '\\' + prefix + '_final.jpg')
        
        cv2.imwrite(resultPath + '\\' + prefix + '_final.jpg', restored)
        
endTime = datetime.now()
print("Time taken : ", endTime - startTime)
print("Time executed = ", datetime.now())
import numpy as np
import cv2
from background_light import getLargestDiff, backgroundLight
from transmission_map import estimate_t

def BGDehaze(img, window):
    print("Started BG Dehazing Process...")
    largestDiff = getLargestDiff(img, window)
    print("Getting Background Light...")
    B, B_GB, B_RGB = backgroundLight(img, largestDiff)
    print("Estimating medium transmission map...")
    t_map = estimate_t(img, B_RGB, window)
    ##to-do --- cv2.imwrite output image before and after refined transmission
    #todo --- write restored image fn and refined transmission map fn
    print("Blue green dehazing done!")
    return


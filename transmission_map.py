import math
import numpy as np

#coarse estimation of the transmission map, based on Dark Channel Prior Theory assumptions
def estimate_t(I, B, window):
    temp = I/B
    padSize = math.floor(window/2)
    paddedTemp = np.pad(temp, ((padSize, padSize), (padSize, padSize), (0,0)) , 'constant')

    #initialize t
    t = np.zeros((I.shape[0], I.shape[1], 2))

    #t(x)=1−minc∈{g,b}(minx∈Ω(Ic(x)Bc))
    #todo--- doubt!
    return t
    


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
    for i, j in np.ndindex(I.shape[0], I.shape[1]):
        t[i, j, 0] = 1 - np.min(paddedTemp[i:i+window, j:j+window, 0])      #t_blue
        t[i, j, 1] = 1 - np.min(paddedTemp[i:i+window, j:j+window, 1])      #t_green
        
        #according to me, as medium transmission maps of b and g channels are assumed to be identical
        #tmp = min(np.min(paddedTemp[i:i+window, j:j+window, 0]), np.min(paddedTemp[i:i+window, j:j+window, 1]))
        #t[i, j, 0] = 1 - tmp
        #t[i, j, 1] = 1 - tmp

    return t
    


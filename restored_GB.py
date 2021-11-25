import numpy as np

#Jc(x)=Ic(x)−Bc/tc(x)+Bc,c∈{g, b}
def getRestoredChannel(I, t, B):
    I = np.float32(I)
    J = np.zeros(I.shape, dtype = np.float32)
    for c in range(2):  #for b and g
        J[:, :, c] = (I[:, :, c]-B[c])/t[:, :, c]
        J[:, :, c] = J[:, :, c] + B[c]
    
    #scale J to (0, 255) and astype = uint8(check!)
    J = (J-J.min())/(J.max()-J.min())*255
    J = np.uint8(np.clip(J, 0, 255))
    return J
    

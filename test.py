import numpy as np
from StoreWater import WaterStoredInPlatform
print ("Final Storage case 1: ",WaterStoredInPlatform(np.array([[2,2,2],[2,2,2],[2,2,2]])))
print ("Final Storage case 2: ",WaterStoredInPlatform(np.array([[2,2,2,2],[2,1,2,1],[2,2,2,1]])))
print ("Final Storage case 3: ",WaterStoredInPlatform(np.array([[3,3,3,3,3,3],[3,1,2,3,1,3],[3,1,2,3,1,3],[3,3,3,1,3,3]])))
print ("Final Storage case 4: ",WaterStoredInPlatform(np.array([[3,3,3,3,5,3],[3,0,2,3,1,3],[3,1,2,3,1,3],[3,3,3,1,3,3]])))
print ("Final Storage case 5: ",WaterStoredInPlatform(np.array([[5,5,5,5,5],[9,1,1,1,5],[5,1,5,1,5],[5,1,1,1,5],[5,5,5,5,5]])))
print ("Final Storage case 6: ",WaterStoredInPlatform(np.array([[3,3,5,3,3,3],[3,1,1,6,1,3],[3,1,2,1,3,3],[3,1,3,3,3,3]])))
print ("Final Storage case 6: ",WaterStoredInPlatform(np.array([[6,6,6,6,6,6],[6,1,1,1,1,6],[6,6,6,6,1,6],[6,6,1,6,1,6]])))

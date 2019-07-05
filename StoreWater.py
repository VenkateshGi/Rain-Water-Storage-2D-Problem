import numpy as np
global visit_nodes
global deciders
def checkSides(platform):
    #canStoreWater = np.zeros(platform.shape)
    #print ("platform inside :\n",platform)
    #print("PLATFORM",platform)

    deciders = np.ones(platform.shape)
    for i in range(1,platform.shape[0]-1):
        for j in range(1,platform.shape[1]-1):
            visit_nodes = np.zeros(platform.shape)
            base(i,j,platform,platform[i][j],visit_nodes,i,j,deciders)

    return deciders

def base(i,j,platform,value,visit_nodes,fixed_x,fixed_y,deciders):
    visit_nodes[i][j] = 1
    #print("--i--",i,"--j--",j,'===>',value,"\n")
    if i == 0 or i == (platform.shape[0] - 1) or j == 0 or (j==platform.shape[1] - 1) or platform[i][j] == 0:
        #print("returning 0")
        deciders[fixed_x][fixed_y] = 0
        return 0

    else:
        #UP
        print("GO UP--","**",i,"**",j,"**","**",value)
        if (platform[i-1][j] <= value) and (not visit_nodes[i-1][j]):
            base(i-1,j,platform,value,visit_nodes,fixed_x,fixed_y,deciders)
            #print("recursion")
        #DOWN
        print("GO DOWN--","**",i,"**",j,"**","**",value)
        if (platform[i+1][j] <= value) and (not visit_nodes[i+1][j]):
            base(i+1,j,platform,value,visit_nodes,fixed_x,fixed_y,deciders)
            #print("recursion")
        #RIGHT
        print("GO RIGHT--","**",i,"**",j,"**","**",value)
        if (platform[i][j+1] <= value) and (not visit_nodes[i][j+1]):
            base(i,j+1,platform,value,visit_nodes,fixed_x,fixed_y,deciders)
            #print("recursion")
        #LEFT
        print("GO LEFT--","**",i,"**",j,"**","**",value)
        if (platform[i][j-1] <= value) and (not visit_nodes[i][j-1]):
            base(i,j-1,platform,value,visit_nodes,fixed_x,fixed_y,deciders)
            #print("recursion")

def WaterStoredInPlatform(platform):

    deciders = np.ones(platform.shape)
    for i in range(1,platform.shape[0]-1):
        for j in range(1,platform.shape[1]-1):
            visit_nodes = np.zeros(platform.shape)
            #print("checking for after 0 :",i,"--",j,"--",platform[i][j])
            base(i,j,platform,platform[i][j],visit_nodes,i,j,deciders)

    waterStorage = 0

    canStoreWater = deciders

    print ("final platform :\n",platform)
    print("Store water : \n",canStoreWater)
    while 1 in canStoreWater[1:-1,1:-1]:
        for i in range(1,platform.shape[0]-1):
            for j in range(1,platform.shape[1]-1):
                if canStoreWater[i][j] == 1:
                    platform[i][j]+=1
                    waterStorage+=1
        #
        canStoreWater = checkSides(platform)
    return waterStorage

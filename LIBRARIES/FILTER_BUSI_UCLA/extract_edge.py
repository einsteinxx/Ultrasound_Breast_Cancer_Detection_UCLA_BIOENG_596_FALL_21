def extract_edge(binary_image,npoint, center,roworcol):
    #
    # Get valid columns/rows from image
    # roworcol = 0 is row, 1 = column

    
    point = [0,npoint]
    edges =[]
    
    for ii in point:
        max_line = 0
        max_default = 1e6
        #print(' ii, center = ', ii, center)
        if (center > ii):
            step = -1
            heading = 0
        else:
            step = 1
            heading = npoint


        for line in range(center,heading,step):
            #nr,nc = np.shape(binary_image)
            #print('bin image = ', binary_image)
            if (roworcol == 0):
                max_vals = np.sum(binary_image[line,:])
            else:
                max_vals = np.sum(binary_image[:,line])
            #print(line, max_vals, roworcol)
            if (max_vals < max_default):
                max_default= max_vals
                max_line = line
            if (max_vals < 250):
                #this is likely outside the core subimage
                break
        #print('max default = ',max_default)
        #print('max line = ',max_line)
        edges.append(max_line)

    status = 1
    if (len(edges) <2):
        edges = [0,0]
        status = 0

    return edges, status
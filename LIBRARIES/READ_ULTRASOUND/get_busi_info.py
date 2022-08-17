def get_busi_info(busi_main_dir):
    print('--- Loading BUSI Data Files and Categorizing')
    busi_dirs = os.listdir(busi_main_dir)
    print('busi directories: ', busi_dirs)

    #busi_m_files = os.listdir(os.path.join(busi_main_dir, 'malignant')) #bus_dirs['malignant']))

    m_mask_list = []
    image_m_dict={}
    image_n_dict ={}
    image_b_dict={}

    mask_m_dict = {}
    mask_n_dict ={}
    mask_b_dict = {}

    busi_filename =[]
    busi_category = []
    busi_bbox=[]

    for category in busi_dirs:
        busi_files = os.listdir(os.path.join(busi_main_dir, category))
        
        for filename in busi_files:
            busi_filename.append(filename)
            if ('mask' in filename):
                m_mask_list.append(filename)
                temp= filename.split(' ')
                number = re.findall('\d+',temp[1])
                number = int(number[0])

                full_file = os.path.join(busi_main_dir,category, filename)
                img_data = image.imread(full_file)

                if ('normal' not in category):
                    result =np.where(img_data > 0)
                    rows = min(result[0]),max(result[0])
                    cols = min(result[1]), max(result[1])
                else:
                    #normal cases have a solid 0 mask
                    rows = 0,0
                    cols = 0,0



                #
                # Create Mask coordinates
                #
                #    pos = np.int32(pos)
                #    xmin = pos[0][0]
                #    xmax = pos[1][0]
                #    ymin = pos[0][1]
                #    ymax = pos[2][1]        
                #busi_bbox.append([(rows[0],cols[0]), (rows[0], cols[1]), (rows[1], cols[0]), (rows[1], cols[1])])
                if ('malignant' in temp[0]):
                    mask_m_dict[number]  = [(cols[0],rows[0]), (cols[1],rows[0]), 
                                            (cols[0], rows[1]), (cols[1], rows[1])]
                    #[(rows[0],cols[0]), (rows[0], cols[1]), (rows[1], cols[0]), (rows[1], cols[1])]
                elif ('normal' in temp[0]):
                    mask_n_dict[number] = [] 
                    #[(cols[0],rows[0]), (cols[1],rows[0]), 
                    #                        (cols[0], rows[1]), (cols[1], rows[1])]
                    
                # [(rows[0],cols[0]), (rows[0], cols[1]), (rows[1], cols[0]), (rows[1], cols[1])]
                elif ('benign' in temp[0]):
                    mask_b_dict[number] = [(cols[0],rows[0]), (cols[1],rows[0]), 
                                            (cols[0], rows[1]), (cols[1], rows[1])]
                # [(rows[0],cols[0]), (rows[0], cols[1]), (rows[1], cols[0]), (rows[1], cols[1])]
                else:
                    print('Found an incorrect data category')
                    exit()

                
                '''
                plt.figure()
                plt.imshow(img_data,cmap = 'jet')
                plt.colorbar()
                plt.show()
                '''
            else:
                temp= filename.split(' ')
                number = re.findall('\d+',temp[1])
                number = int(number[0])
                full_file = os.path.join(busi_main_dir,category, filename)

                if ('malignant' in temp[0]):
                    image_m_dict[number] = full_file
                elif ('normal' in temp[0]):
                    image_n_dict[number] = full_file
                elif ('benign' in temp[0]):
                    image_b_dict[number] = full_file
                else:
                    print('Found an incorrect data image category')
                    exit()
        print('Done with category: ', category)
                
    print('Done parsing BUSI data')
        
    return mask_m_dict, mask_n_dict, mask_b_dict, image_m_dict,image_n

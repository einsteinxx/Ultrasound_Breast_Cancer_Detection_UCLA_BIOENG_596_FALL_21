def video_stats(training_set, video_id, bounding_box):
    if (training_set in [0,1]):
        #generate stats on bounding boxes
        uvids = set(video_id)

        box_collect=[]
        frames_collect=[]
        empty_annotations=[]
        for count, v in enumerate(uvids):
            number_frames = 0
            number_boxes = 0
            
            #print('---- loading: ', v)
            for icount,ii in enumerate(video_id):
                if (ii == v):
                    box_info = bounding_box[icount]
                    number_frames+=1
                    if (not (box_info =='[]')):
                        number_boxes+=1
                    else:
                        pass
                        #print('no annotation', frame_id[icount])
            frames_collect.append(number_frames)
            box_collect.append(number_boxes)
            #print(v,number_frames,number_boxes)
            if (number_boxes == 0):
                empty_annotations.append(v)




        print('Number of videos: ',np.size(frames_collect[:]))
        print('Number of annotated cases ',np.size(box_collect))
        print('Videos with no Annotations:', empty_annotations)
            #get_bb_stats(v, video_id,bounding_box, image_path)
    else:
        print('Skipping Bounding box statistics for UCLA data')
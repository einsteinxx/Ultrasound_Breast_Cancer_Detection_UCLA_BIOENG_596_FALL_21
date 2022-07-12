def sort_UCLA_csv(annotation_rows, annotation_fields):
    print(np.shape(annotation_rows))

    print(annotation_fields)

    array_rows = np.array(annotation_rows)
    mrn = array_rows[:,1]
    accession = array_rows[:,2]
    video_id = array_rows[:,3]
    frame_id = array_rows[:,4]
    image_path = array_rows[:,5]
    bounding_box = array_rows[:,6]
    diagnosis = array_rows[:,7]
    biopsy_site = array_rows[:,8]
    diagnosis2 = array_rows[:,9]
    first50 = array_rows[:,10]

    return array_rows, mrn, accession, video_id, frame_id, image_path, bounding_box, \
        diagnosis, biopsy_site, diagnosis2, first50
def get_ucla_csv(csv_dir):
    #READ CSV FILES
    #pull out the box information and label info
    csv_list = os.listdir(csv_dir)

    for csv_file in csv_list:
        filename = os.path.join(csv_dir,csv_file)
        if (os.path.isdir(filename) == 1):
            #skip any directories found in list
            continue
        #if ('_final' in csv_file):
        if ('Batch1_Batch2' in csv_file):
            annotation_fields, annotation_rows = get_csv_data(filename)

        else:
            print('Non-archive file found ',filename)
    return annotation_fields, annotation_rows
def get_dicom_info(local_dir):
	#
	# Get DICOM info
	#
	import os
	from pydicom import dcmread
	local_files = os.listdir(local_dir)

	for dicom_file in local_files:
		filename = os.path.join(local_dir,dicom_file)
		if (os.path.isdir(filename) == 1):
			#skip any directories found in list
			continue
		if ('dcm' in filename):
			print(filename)
			ds = dcmread(filename, force=True)
			for element in ds:
				print(element)

		else:
			print('Non-dicom file found ',filename)
	return
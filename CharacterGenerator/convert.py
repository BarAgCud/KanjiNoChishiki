from PIL import Image
import numpy as np

import os
import glob

# Dataset generated to train the network
filestraining = glob.glob(r'filea/*')
# Dataset generated to evaluate the network performance
fileseval = glob.glob(r'fileb/*')
# Dataset generated to test the network with a single character
filesingle = glob.glob(r'fileb/0987_988_Hannari.otf_fs_27_bc_245a.png')


def generate_array(inputdir,outputfile):
	out= np.array([], dtype=np.uint8)
	for name in inputdir:
			#If files were generated by main.py,
			#name[6:10] should be the label
			label = name[6:10]
			print(label)
			
			im = Image.open(name)
			rgb_im = im.convert('RGB')
			im = (np.array(rgb_im))

			r = im[:,:,0].flatten()
			g = im[:,:,1].flatten()
			b = im[:,:,2].flatten()

			labelfin= []
			labellist=np.array( list(label),np.uint8)
			
			for charac in np.nditer(labellist):
						charac2=charac+48
						labelfin.append(charac2)
			
			out=np.r_[out,np.array( list(labelfin) + list(r) + list(g) + list(b),np.uint8)]


			
	out.tofile(outputfile)
	return
	
#There lines should be commented if you don't want to generate every file
#generate_array(filestraining,"training.bin")
generate_array(fileseval,"verify.bin")
#generate_array(filesingle,"single.bin")

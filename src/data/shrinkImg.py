from PIL import Image
import numpy as np
import glob
import os
import pandas as pd


basewidth = 512

pd_paper = pd.read_csv('../../bib/paper_vis4ml_v2_copy.csv')

paper_list = []
for index, row in pd_paper.iterrows():
	if row['Citation'] != 'nan':
		paper_list.append(row['Citation'])


print(len(paper_list))

for image_path in glob.glob("./papers_img_raw/*.png"):
	img = Image.open(image_path)
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), Image.Resampling.LANCZOS)

	img_name = os.path.basename(image_path)
	print(img_name)

	if(img_name.split('.')[0] in paper_list):
		img.save('./papers_img/'+img_name, optimize=True, quality=95) 

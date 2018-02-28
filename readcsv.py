import os
import pandas as pd
import csv
from pandas import parser

li_splitfiles = os.listdir('pol-splitted/')

# for splitfile in li_splitfiles:

dfreader = ''
dfreader = pd.read_csv('pol-splitbasefile.csv', escapechar='\\', encoding='utf-8', engine='python', chunksize=50000)
counter = 0
for chunk in dfreader:
	try:
		counter = counter + 1
		columnheaders = ['num','subnum','thread_num','op','timestamp','timestamp_expired','preview_orig','preview_w','preview_h','media_filename','media_w','media_h','media_size','media_hash','media_orig','spoiler','deleted','capcode','email','name','trip','title','comment','sticky','locked','poster_hash','poster_country','exif']
		chunk.to_csv('fixed/pol-' + str(counter) + '.csv', index=False, header=columnheaders)
		print('file ' + str(counter) + ' fixed and written.')
	except (parser.ParserError) as detail:
		print(detail)
		quit()
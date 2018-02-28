import os
import pandas as pd
import csv
import datetime
from pandas import parser

inputfolder = 'fixed/'
li_files = os.listdir('fixed/')
columnheaders = ['num','subnum','thread_num','op','timestamp','timestamp_expired','preview_orig','preview_w','preview_h','media_filename','media_w','media_h','media_size','media_hash','media_orig','spoiler','deleted','capcode','email','name','trip','title','comment','sticky','locked','poster_hash','poster_country','exif']
# for csvfile in li_files:

def getWordCounts(inputcsv, word, timebucket='month'):
	timebucket = timebucket
	li_files = []
	if os.path.isdir(inputcsv):
		li_files = os.listdir(inputcsv)
	elif os.path.isfile(inputcsv)
		li_files.append(inputcsv)
	print(inputcsv)
	df = pd.read_csv(inputcsv, escapechar='\\', encoding='latin-1')
	df_filtered = df[df['comment'].str.lower().str.contains(word, na=False)]
	df_filtered.to_csv('csvs-wordfiltered/' + word + '-' + inputcsv[10:], index=False)
	print(str(len(df_filtered)) + ' mentions of ' + word)

	di_mentions = {}
	stored_date = ''
	count_wordmentions = 1


	if timebucket == 'hour':			#determine what time filter should be used
		timefilter = '%Y-%m-%d %H'
	elif timebucket == 'day':
		timefilter = '%Y-%m-%d'
	elif timebucket == 'month':
		timefiter = '%Y-%m'
	elif timebucket == 'year':
		timefiter = '%Y-%m'
	else:
		timefilter = 'month'

	for index, row in df_filtered.iterrows():
		previousdate = stored_date
		currentdate = datetime.datetime.fromtimestamp(row['timestamp']).strftime(timefilter)

		if currentdate == stored_date:			#if date already exists
			count_wordmentions = count_wordmentions + 1
			di_mentions[currentdate] = count_wordmentions
		else:									#if it's a new date
			count_wordmentions = 1
			di_mentions[currentdate] = count_wordmentions
		stored_date = currentdate
	print(di_mentions)

getWordCounts(inputfolder + li_files[168], 'nigger', timebucket='day')
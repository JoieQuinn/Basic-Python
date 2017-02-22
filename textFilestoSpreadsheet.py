#!/usr/bin/env python 3

'''
A program for creating a spreadsheet from text files in the
same directory.  You must have openpyxl installed.

On the command line, type: 
>> pip install openpyxl
or
>> pip3 install openpyxl

The first file will populate column 1, the second will
populate column 2, and so on...
'''

from __future__ import print_function
import sys, openpyxl

def main():
	if (len(sys.argv)) > 1:
		args = sys.argv[1:]
	else:
		print('Usage: python textFilestoSpreadsheet.py [file 1] [file 2]...')
	
	#Create workbook
	wb = openpyxl.Workbook()
	sheet = wb.active
	
	#Loop through input files with readlines() and print lines to 
	#appropriate column
	row = 1
	column = 1

	for item in args:
		f = open(item, 'r')
		for line in f.readlines():
			sheet.cell(row=int(row), column=int(column)).value = line
			row += 1
		f.close()
		column += 1
		row = 1

	#Save workbook
	wb.save('combinedFiles.xlsx')

if __name__ == '__main__':
	main()
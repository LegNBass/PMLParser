import os
import sys
from PML_Parser import parsePML

if __name__ == "__main__":

	#Check for valid argument
	if len(sys.argv)>1 and sys.argv[1][-5:] == '.html':

		#Run PML Parser
		f = open(sys.argv[1])
		text = f.read()
		result = parsePML(text)

		for i in xrange(len(result.split('\n'))-1):
			text = text[:text.find('<pml>')] + result.split('\n')[i] + text[text.find('</pml>')+6:]
		print text

	elif len(sys.argv)>1 and sys.argv[1] == '--help':
		print 'Syntax is "python Main.py [HTML Document FilePath]"'

	else: 
		print 'No Valid Arguments\n--help for more info'
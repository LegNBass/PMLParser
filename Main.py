import sys
from PML_Parser import parsePML

if __name__ == "__main__":

	#Check for valid doc argument
	if len(sys.argv)>1 and sys.argv[1][-5:] == '.html':

		#Retrieve text from file and run the parsing script
		f = open(sys.argv[1])
		text = f.read()
		result = parsePML(text)

		# Each line of the result represents a PML block, so we iterate 
		# through each line and inject it into each PML block in order
		for i in xrange(len(result.split('\n'))-1): # -1 here because exec adds a blank line
			text = text[:text.find('<pml>')] + result.split('\n')[i] + text[text.find('</pml>')+6:] # +6 here to avoid displaying pml tag
		print text

	# Display syntax when asked for help
	elif len(sys.argv)>1 and sys.argv[1] == '--help':
		print 'Syntax is: "python Main.py [HTML Document FilePath]"'

	# illegal arg result.
	else: 
		print 'No Valid Arguments\n--help for more info'
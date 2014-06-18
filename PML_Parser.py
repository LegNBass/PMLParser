import sys
import re
from StringIO import StringIO


# This Method finds the indentation used and returns the 
# indent of the first letter in the first non-whitespace line
def findIndent(text): 
	pBlankLine = re.compile('\s*$') #Blank Line Regex
	pText = re.compile('\w') #Any non-whitespace character Regex
	
	# Split the input into rows and iterate
	rows = text.split('\n')	
	for i in rows:
		if not pBlankLine.match(i): break # Break when first non-whitespace line is found
	if pText.search(i): #Error trapping
		start = pText.search(i).start()
		return i[:start]
	else:
		return ''


# This Method takes a file input and parses it for 
# <pml> python code </pml>
def parsePML(htmlFile):
	# pml will hold the entire statement to execute
	pml=''

	# ltest contains the file text in lowercase.
	# This is to help parse for the pml tags, regarless of case.
	ltext = htmlFile.lower()

	# Start and end will temporarily hold the indicies of each PML block
	start, end = ltext.find('<pml>'), ltext.find('</pml>')

	# Loop while there are still valid PML blocks
	while start != -1 and end != -1:

		#Save the interior of the PML block as statement
		statement = htmlFile[start+6:end] 

		#find next indicies
		start = ltext.find('<pml>',end)
		end = ltext.find('</pml>', end+6) # start the search after the existing tags close

		# Finds the indent of the PML block
		indent = findIndent(statement)

		# Removes indentation and adds a print pml statement if the pml variable is reassigned
		pAssignPML = re.compile('pml\s*[+\-*%/]?=') #finds pml assignment
		while statement[:len(indent)] == indent and indent != '':
			statement = '\n'.join([i[len(indent):] for i in statement.split('\n')])+'\nprint pml.replace("\\n","")\n' if pAssignPML.search(statement) \
				else '\n'.join([i[len(indent):] for i in statement.split('\n')])

		# Adds statement to pml expression
		pml+=statement
	
	# Compiles the pml expression into a code object
	result = compile(pml,'-','exec')

	# Creates a buffer and replaces the stdout with it during 
	# the execution of the pml expression
	buffer = StringIO()
	sys.stdout = buffer
	exec result
	sys.stdout = sys.__stdout__ #replaces the stdout

	# Returns the output of the interpreted pml expression
	return (buffer.getvalue())
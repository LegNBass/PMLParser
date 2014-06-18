import sys
from StringIO import StringIO
#
# This Method takes a file input and parses it for 
# <pml> python code </pml>
#
def parsePML(htmlFile):
	# pml will hold the entire statement to execute
	pml=''

	# ltest contains the file text in lowercase.
	# This is to help parse for the pml tags, regarless of case.
	ltext = htmlFile.lower()

	# indicies will contain a set of tuples of the start and end of each pml block
	# start and end will temporarily hold the values of each tuple
	indicies=[]
	start, end = ltext.find('<pml>'), ltext.find('</pml>')

	# 
	while start != -1 and end != -1:
		indicies.append((start,end))
		statement = htmlFile[start+6:end] 
		start = ltext.find('<pml>',end)
		end = ltext.find('</pml>', end+6)
		while statement[:4]=='    ':
			statement = '\n'.join([i[4:] for i in statement.split('\n')])+'\nprint pml.replace("\\n","")\n' if 'pml' in statement \
				else '\n'.join([i[1:] for i in statement.split('\n')])
		while statement[:1]=='\t':
			statement = '\n'.join([i[1:] for i in statement.split('\n')])+'\nprint pml.replace("\\n","")\n' if 'pml' in statement \
				else '\n'.join([i[1:] for i in statement.split('\n')])
		pml+=statement
	result = compile(pml,'-','exec')

	buffer = StringIO()
	sys.stdout = buffer
	exec result
	sys.stdout = sys.__stdout__

	return (buffer.getvalue())
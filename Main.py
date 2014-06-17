import os
import sys
from PML_Parser import parsePML

if __name__ == "__main__":

	#Check for valid argument
	if len(sys.argv)>1 and sys.argv[1][-5:] == '.html':

		#Run PML Parser
		parsePML(open(sys.argv[1]))
		
	else: 
		print 'No Args'
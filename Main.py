import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from PML_Parser import parsePML

if __name__ == "__main__":

	#Check for valid doc argument
	if sys.argv[1:] and sys.argv[1][-5:] == '.html':

		#Retrieve text from file and run the parsing script
		f = open(sys.argv[1])
		text = f.read()
		result = parsePML(text)

		# Each line of the result represents a PML block, so we iterate 
		# through each line and inject it into each PML block in order
		for i in xrange(len(result.split('\n'))-1): # -1 here because exec adds a blank line
			text = text[:text.find('<pml>')] + result.split('\n')[i] + text[text.find('</pml>')+6:] # +6 here to avoid displaying pml tag
		
		# If --runserver is selected, the html output is hosted on localhost:8000
		if sys.argv[2:] and sys.argv[2] == '--runserver':
			
			# Writes the output to index.html
			page = open('index.html','w')
			page.write(text)
			page.close()

			# Sets up the simple http server
			HandlerClass = SimpleHTTPRequestHandler
			ServerClass  = BaseHTTPServer.HTTPServer
			Protocol     = "HTTP/1.0"

			# Provides default port
			port = 8000
			server_address = ('127.0.0.1', port)

			HandlerClass.protocol_version = Protocol
			httpd = ServerClass(server_address, HandlerClass)

			# Prints a message showing server creation and starts serving
			sa = httpd.socket.getsockname()
			print( "Serving HTTP on", sa[0], "port", sa[1], "...")
			httpd.serve_forever()
		# If --runserver is not selected, prints the result to stdout
		else:
			print text

	# Display syntax when asked for help
	elif sys.argv[1:] and sys.argv[1] == '--help':
		print 'Syntax is: python Main.py "HTML Document FilePath" [--runserver]'

	# illegal arg result.
	else: 
		print 'No Valid Arguments\n--help for more info'
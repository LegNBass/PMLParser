PMLParser
Author: Charlie Armentrout
=========

Parses .html files for <PML></PML> tags and replaces the tagged blocks with the result of the executed python code within.

ASSUMPTIONS:
1. Each and every <PML></PML> tagged block must have one and ONLY one return.
	-A return is defined as either a statement that writes to the stdout or an assignment to a variable named 'pml'. If the pml variable is modified, that will also trigger a return.
	-This is required in order to make these PML tags usable in a real-life scenario. If there were multiple returns in one block, there would be no way to determine which one to replace that block with. If there were no returns at all, then why include a <PML></PML> block at all? In that scenario, put your python code in the block that will return a value.
2. Input files will be .html documents
	-The goal of this application is to produce valid HTML. Because of this, the application only accepts files that end in .html.
3. If a return includes multiple lines, assign it to the pml variable instead of printing to the stdout directly.
	-This is required because the python interpreter adds a new line after a printed statement, which cannot be accounted for by the exec command. It can however be accounted for by removing line breaks from the pml variable.
	-Valid HTML does not require line breaks.

USAGE:
1. Install python 2.7
2. Execute the python 2.7 application from the command line, supplying the ParsePML.py file as the first argument.
3. Supply "--help" as the second argument for a syntax reference.
4. To parse a file, supply the filepath of the .html document as the second argument. If the file is located in the same folder as the shell instance, the name will suffice.
5. If you would like to host the output of the parsed file locally, supply "--runserver" as an optional third argument. Then open a browser and navigate to http://localhost:8000
6. To stop the web server, perform a keyboard interrupt (usually ctrl+c)

TESTING:
There is a test .html file located in the PMLParser directory named "TestDoc.html". This file contains examples of multiple <PML></PML> blocks with a variable assignment in one that is called in another. Feel free to experiment with the capabilities of python nested within HTML, while keeping in line with the assumptions listed above!
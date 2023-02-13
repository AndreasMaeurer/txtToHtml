#!/usr/bin/env python3

""" ********************************************************************   
 * 
 * @Author
                     _                      __  __                                
     /\             | |                    |  \/  |                               
    /  \   _ __   __| |_ __ ___  __ _ ___  | \  / | __ _  ___ _   _ _ __ ___ _ __ 
   / /\ \ | '_ \ / _` | '__/ _ \/ _` / __| | |\/| |/ _` |/ _ \ | | | '__/ _ \ '__|
  / ____ \| | | | (_| | | |  __/ (_| \__ \ | |  | | (_| |  __/ |_| | | |  __/ |   
 /_/    \_\_| |_|\__,_|_|  \___|\__,_|___/ |_|  |_|\__,_|\___|\__,_|_|  \___|_|


Version: 	0.1
Created: 	03/22/2020
Modified: 	03/23/2020  improvements
			04/08/2020	Added Installation Notes

Scope:
    For years I've been saving .txt files with lots of URLs
    The purpose of this script is to convert the .txt files
    into .html files so that the URLs are clickable.  This provides much better usability.
    
Usage:
     python3 txtToHtml.py myfile.txt 
     This creates an output file named myfile.html.  Which is what we need.

References:
    https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
    https://www.w3schools.com/python/python_file_write.asp
    https://docs.python.org/3/library/stdtypes.html?highlight=startswith#str.startswith
    https://www.tutorialspoint.com/python3/python_command_line_arguments.htm
    https://pythonprinciples.com/blog/converting-integer-to-string-in-python/
    https://stackoverflow.com/questions/1038824/how-do-i-remove-a-substring-from-the-end-of-a-string-in-python
    https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_body_bgcolor
    
Installation:
	On Ubuntu 16.04
	sudo cp /home/andreas/csIch/txtToHtml/txtToHtml.py /usr/bin/txtToHtml
	sudo chmod 777 /usr/bin/txtToHtml 
	
FixMe:
	if the URL is indented, this program should still turn the URL into a link.  Right now it only works when the URL is at the beginning of the line.
		Use case scenario:  I'm reading old code, I want to quickly click through the References.  So, BOOM, this program should convert the code into .html
		I did implement this.  But for the future, it would be better if I could use Regular Expressions and identify a URL from anywhere in the text.
	Need to add a "usage" case.   If the user runs the program without the adequate input params the "usage" notes print out.
	

******************************************************************** """ 

import sys

fileToBeOpened = sys.argv[1]

nameOfOutputFile = (str(fileToBeOpened) + ".html")

if nameOfOutputFile.endswith('.txt.html'):
    nameOfOutputFile = nameOfOutputFile[:-9]
    nameOfOutputFile = (str(nameOfOutputFile) + ".html")

f = open(nameOfOutputFile, "w")  #"w" overwrites the old file  "x" only if no old exists

file1 = open(fileToBeOpened, 'r') 
Lines = file1.readlines()

f.write('<!DOCTYPE html><html><body bgcolor="#DED2BC"><br><br><br>')

for line in Lines:
    if("\n" in line):
        f.write("<br>")
    if ((line.startswith("http"))or(line.startswith("	http"))):
        f.write('<p><a href="')
        f.write(line)
        f.write('" target="_blank">')
        f.write(line)
        f.write('</a></p>')
    else:
        f.write(line)
        
f.write("<br><br>End!</body></html>")
f.close()

#!/usr/bin/python

import requests
import random
import string
import os
import sys

class colors:
    END  = '\033[0m'
    RED  = '\033[31m'
    CYAN = '\033[36m'
    

def main (url_file):
   try:
    letters = string.ascii_letters
    randomName = ''.join(random.choice(letters) for i in range(5))
    response = requests.get(url_file)
    file = open(randomName, "wb")
    file.write(response.content)
    file.close()
    print "\033[0;30;47m==================== File Name: "+randomName+" ====================\033[0m\n"
    print "\033[0;33m****************************** File Command Results ******************************\033[0m"
    print"\033[31m";os.system("file "+randomName);print"\033[0m"
    print "\033[0;33m******************************* Exiftool Command Results ********************************\033[0m"
    print "\033[31m";os.system("exiftool "+randomName);print"\033[0m"
    print "\033[0;33m******************************* Binwalk Command Results *******************************\033[0m"
    print "\033[31m";os.system("binwalk "+randomName);print"\033[0m"
    print "\033[36mPlease Answer yes/no OR y/n "
    os.system("rm -i"+" "+randomName)
    print "\033[0m\n\n"
    print "\033[90;7m-------------------------------------------------------------------------------"
    print "Written by: Mustafa Twitter - @c0brabaghdad1 , File + ExifTool + Binwalk (FETB)"
    print "-------------------------------------------------------------------------------\033[0m"
   except :
    	print(colors.RED+"Failed To Connect !"+colors.END)
if len(sys.argv) > 1:
	if sys.argv[1] == "--url" or  sys.argv[1] == "-u":
		if len(sys.argv) > 2:
			main(sys.argv[2])
		else:
			print(colors.CYAN+"Missing URL Try ->  -h"+colors.END)
	if sys.argv[1] == "--help" or sys.argv[1] == "-h":
         print (colors.CYAN+"Usage : fetb.py --url or -u https://www.target.tld/metadata.png"+colors.END)
	else:
		pass
else:
	url_file = raw_input("Enter URL File : ")
	main(url_file)    
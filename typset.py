#!/usr/bin/env python
##############################################
# File: amsTypset.py                         #
# Auth: Jeremy A. Gibbs                      #
# Date: 30 Mar 2009                          #
# Desc: This is a simple utility to typeset  #
#       .tex files into several formats.     #
##############################################

import os,sys

###################
# Grab LaTeX file #
###################

try: 
    latexFile = sys.argv[1]
except:
    print "Hey! I need a LaTeX file to typeset."
    latexFile = raw_input("Enter your LaTeX file name ==> ")
    if latexFile == "":
        print "I quit!!"
        exit()
        
fileName = latexFile[:-4]
dviFile = fileName + ".dvi"
psFile = fileName + ".ps"
pdfFile = fileName + ".pdf"
outputDir = "./"

###########################
# Let us welcome everyone #
###########################

print "Welcome to your friendly neighborhood LaTeX typesetting script."
print "We will create .dvi, .ps, and .pdf versions of %s."%latexFile

print "\nFirst run-thru with LaTeX ..."
os.system("/usr/texbin/latex %s >& /dev/null"%latexFile)

print "\nMaking bibliography with BibTex ..." 
os.system("/usr/texbin/bibtex %s >& /dev/null"%fileName) 

print "\nLast run-thru with LaTeX ..."
os.system("/usr/texbin/latex %s >& /dev/null"%latexFile)
os.system("/usr/texbin/latex %s >& /dev/null"%latexFile)

#################################
# Tell them what we've done Bob #
#################################
#convert dvi to ps
os.system("/usr/texbin/dvips -o %s %s >& /dev/null"%(psFile,dviFile))

#create a pdf
os.system("ps2pdf %s >& /dev/null"%(psFile))

print "\nSuccessfully created %s"%pdfFile
print "To view this file, type 'open %s'"%(outputDir+pdfFile)

#open the pdf, since most people prefer this option
print "\nOpening .pdf ..."
os.system("open %s"%(outputDir+pdfFile))

#Here we clean up some junk files made during conversion.
print "\nRemoving temporary files ..."
os.system(" \\rm *.aux *.bbl *.blg *.lof *.lot *.toc *.log *.fff *.ttt %s %s"%(dviFile, psFile))
print "\nI successfully cleaned up after myself. I am a thoughtful little script!"
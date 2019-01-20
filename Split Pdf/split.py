#! python3
# split.py - big pdf to some pages of that pdf
# Press the windows button + r
# type: split [student name] [pdf name] [page start] [number of pages]
# Example: split Alex Spectrum Reading G1-1 4 2
# The program will find the pdf and save the number of pages you want to
# C:\Users\User\Desktop\English Steward\Students\Student\Month\Day
# --------------------------- Imports -----------------------------------------
import PyPDF2, os, sys, pprint, getpass, datetime
# --------------------------- Variables ---------------------------------------
# Todays date
date      = datetime.datetime.today()
# Month as locale’s full name.
month     = date.strftime("%B")
# Day of the month as a zero-padded decimal number.
day       = date.strftime("%d")
# Base path
path      = 'C:\\Users\\%s\\Desktop\\English Steward' % getpass.getuser()
# Folder to walk
materials = path + '\\Materials'
# sys.argv[0] is the script path
# sys.arg[1] is the student name
# sys.arg[2] is the start of the pdf name
start     = 2
# x is the total length of sys arguments
# sys.arg[2:x-2] is the pdf name
# sys.arg[x-2] is the page to start the split
# sys.arg[x-1] is the amount of pages to include
# there are 4 sys arguments reserved
# path, name, start page, and number of number of pages
# everything in between is the pdf name
length    = len(sys.argv) - 4
end       = start + length
name      = sys.argv[1]
pdf       = ' '.join(sys.argv[start:end]) + '.pdf'
dest      = path + '\\Students\\' + name + '\\' + month + '\\' + day
# Where to start split
pageNum = int((sys.argv[len(sys.argv)-2]))
# Where to end split
numOfPages = int(sys.argv[len(sys.argv)-1])
# ----------------------------- Functions -------------------------------------
def search(pdf):
    for folderName, subfolders, filenames in os.walk(materials):
        for filename in filenames:
            if filename == pdf:
                return os.path.join(folderName, filename)
def split(pdf):
    # if the dest folder doesn't exist
    if os.path.exists(dest) == False:
        # Make the directory
        os.makedirs(dest, exist_ok=True)
    # Change the current working directory to the destination folder
    os.chdir(dest)
    # open the pdf file in read binary mode
    file = open(pdf, 'rb')
    # create reader object
    reader = PyPDF2.PdfFileReader(file)
    # create writer object
    writer = PyPDF2.PdfFileWriter()
    # Make new pdf out of old pdf
    for i in range(numOfPages):
        # read page
        page = reader.getPage(pageNum + i)
        # write page
        writer.addPage(page)
    # open new pdf with new name in write binary mode
    outputFile = open('%s %s Class Material.pdf' % (month, day), 'wb')
    writer.write(outputFile)
    # always close files
    outputFile.close()
    file.close()
# ------------------------------- Main ----------------------------------------
# function returns abs path of the file
location = search(pdf)
# if the file is found
if location:
    split(location)

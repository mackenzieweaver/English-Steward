#! python3
# splitPdf.py - big pdf -> some pages of that pdf
# inputs: pdf file location, new name, new destination
# outputs: new pdf with new name in new destination

import PyPDF2, os, sys, pprint, getpass, datetime

date = datetime.datetime.today()
month = date.strftime("%B")
day = date.strftime("%d")
path = 'C:\\Users\\%s\\Desktop\\English Steward' % getpass.getuser()
materials = path + '\\Materials'

def search(pdf):
    for folderName, subfolders, filenames in os.walk(materials):
        for filename in filenames:
            if filename == pdf:
                return os.path.join(folderName, filename)

# Main

# Student name
print('Student: ', end = '')
name = input()

# Pdf file
print('Pdf file name: ', end='')
pdf = input() + '.pdf'
print('Searching for: ' + pdf + '...')
location = search(pdf) # returns abs path of the file
if location:
    print('Found!')
else:
    print('File ' + pdf + ' not found in')
    print(materials)
# Make directory to save the split pdf
dest = path + '\\Students\\' + name + '\\' + month + '\\' + day
if os.path.exists(dest) == False:
    os.makedirs(dest, exist_ok=True)
os.chdir(dest)
print(os.getcwd())
    
# How many?
print('Starting from: ', end='')
pageNum = int(input()) - 1
print('Number of pages: ', end='')
numOfPages = int(input())

# open file in read binary mode
pdf = open(location, 'rb')

# reader object
reader = PyPDF2.PdfFileReader(pdf)

# writer object
writer = PyPDF2.PdfFileWriter()

for i in range(numOfPages):
    # read page
    page = reader.getPage(pageNum + i)
    # write page
    writer.addPage(page)

# output
outputFile = open('%s %s Class Material.pdf' % (month, day), 'wb')
writer.write(outputFile)

# close files
outputFile.close()
pdf.close()

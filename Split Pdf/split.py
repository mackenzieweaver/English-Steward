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
date      = datetime.datetime.today()
month     = date.strftime("%B")
day       = date.strftime("%d")
path      = 'C:\\Users\\%s\\Desktop\\English Steward' % getpass.getuser()
materials = path + '\\Materials'
start     = 2
length    = len(sys.argv) - 4
end       = start + length
name      = sys.argv[1]
pdf       = ' '.join(sys.argv[start:end]) + '.pdf'
dest      = path + '\\Students\\' + name + '\\' + month + '\\' + day

# ----------------------------- Functions -------------------------------------
def search(pdf):
    for folderName, subfolders, filenames in os.walk(materials):
        for filename in filenames:
            if filename == pdf:
                return os.path.join(folderName, filename)


# ------------------------------- Main ----------------------------------------
print('Searching for: ' + pdf + '...')
# function returns abs path of the file
location = search(pdf)
# if the file is found
if location:
    print('Found!')
    # if the dest folder doesn't exist
    if os.path.exists(dest) == False:
        # Make the directory
        os.makedirs(dest, exist_ok=True)
    # Change the current working directory to the destination folder
    os.chdir(dest)
    # Where to start split
    pageNum = int((sys.argv[len(sys.argv)-2]))
    # Where to end split
    numOfPages = int(sys.argv[len(sys.argv)-1])
    # open the pdf file in read binary mode
    pdf = open(location, 'rb')
    # create reader object
    reader = PyPDF2.PdfFileReader(pdf)
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
    pdf.close()
# otherwise end the program
else:
    print('File ' + pdf + ' not found in')
    print(materials)

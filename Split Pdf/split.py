#! python3
# splitPdf.py - big pdf -> some pages of that pdf
# inputs: pdf file location, new name, new destination
# outputs: new pdf with new name in new destination

#  --------------------------- Imports --------------------------- 
import PyPDF2, os, sys, pprint, getpass, datetime


# --------------------------- Variables ------------------------------- 
date = datetime.datetime.today()
month = date.strftime("%B")
day = date.strftime("%d")
path = 'C:\\Users\\%s\\Desktop\\English Steward' % getpass.getuser()
materials = path + '\\Materials'
'''
for i in range(len(sys.argv)):
    print('sys.argv[%d]' % i + ' = ' + sys.argv[i])
'''
start = 2
length = len(sys.argv) - 4
end = start + length

#----------------------------- Functions ------------------------------
def search(pdf):
    for folderName, subfolders, filenames in os.walk(materials):
        for filename in filenames:
            if filename == pdf:
                return os.path.join(folderName, filename)
            

# ------------------------------- Main --------------------------------

# Student name
name = sys.argv[1]

# Pdf file
pdf = ' '.join(sys.argv[start:end]) + '.pdf'
print('Searching for: ' + pdf + '...')
location = search(pdf) # returns abs path of the file
if location:
    print('Found!')
    # Make directory to save the split pdf
    dest = path + '\\Students\\' + name + '\\' + month + '\\' + day
    if os.path.exists(dest) == False:
        os.makedirs(dest, exist_ok=True)
    os.chdir(dest)
    print(os.getcwd())
    
    # How many?
    pageNum = int((sys.argv[len(sys.argv)-2]))
    numOfPages = int(sys.argv[len(sys.argv)-1])
    
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
else:
    print('File ' + pdf + ' not found in')
    print(materials)

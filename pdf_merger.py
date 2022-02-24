from PyPDF2 import PdfFileMerger
import os
path = os.listdir("D:/temp/test")
merge = PdfFileMerger()
for file in path:
    if file.endswith('.pdf'):
        merge.append(file)
merge.write('merged.pdf')
merge.close()

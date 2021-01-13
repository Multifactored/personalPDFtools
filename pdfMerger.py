#!/usr/bin/env python3
from PyPDF2 import PdfFileMerger
import sys
import os

pdfs = [sys.argv[1], sys.argv[2]]
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

os.mkdir("outcome")
try:
    merger.write("outcome/result.pdf")
except IOError:
    os.mkdir("outcome")
    merger.write("outcome/result.pdf")
merger.close()
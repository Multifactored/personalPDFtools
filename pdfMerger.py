#!/usr/bin/env python
from PyPDF2 import PdfFileMerger
import sys

pdfs = [sys.argv[1], sys.argv[2]]
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
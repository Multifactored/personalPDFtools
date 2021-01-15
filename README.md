# Personal PDF Editing Tools
Written by [@Multifactored](https://github.com/Multifactored)

Originally this was a set of really scuffed tools, but now it's just a utility for my personal use. Probably don't use this yourself, lol. Public for a friend.


Requires Python3 all modules!

* pip3 install pdf2image (use pip3 if need be)
* pip3 install pillow
* pip3 install PyPDF2

## Good uses:
* Editing PDFs in a rather convoluted way, using image editors.
* Compressing PDFs locally without using some freeware online service for privacy reasons by abusing png compression.
* Making PDFs uncopiable without any software, I guess.

## How to use:
python3 pdfToPng.py resume.pdf 
- Outputs the \*.png

python3 pdfToPng.py 0.png 
- Makes 0.pdf.

python3 pdfMerger.py 0.pdf 1.pdf
- Outputs result.pdf

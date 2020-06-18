#!/usr/bin/env python
from pdf2image import convert_from_path, convert_from_bytes


pages = convert_from_bytes(open('resume.pdf', 'rb').read())

count = 0
for page in pages:
    page.save(str(count) + '.png', 'PNG')
    count = count + 1
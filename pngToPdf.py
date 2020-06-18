#!/usr/bin/env python
from PIL import Image
import sys

image1 = Image.open(sys.argv[1])
pdf1 = image1.convert('RGB')
pdf1.save(sys.argv[1][:-4] + ".pdf")
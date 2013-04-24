#!/usr/bin/python

import sys
import os
import requests

pdf_url = sys.argv[1]
output = sys.argv[2]

tmpfilename = 'tmpfile'


gfile = requests.get(pdf_url)
tfile = open(tmpfilename, 'w+b')
tfile.write(gfile.content)
tfile.close()


# http://www.parlamento.gub.uy/VerDocEspecial.asp?DocumentoId=114
# curl http://www.parlamento.gub.uy/VerDocEspecial.asp?DocumentoId=114 > viaticos.pdf


from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfdevice import TagExtractor
from pdfminer.pdfinterp import process_pdf

codec = 'utf-8'
debug = 0
# input option
password = ''
pagenos = set()
maxpages = 0
# output option
outfile = None
outtype = None
imagewriter = None
layoutmode = 'normal'
codec = 'utf-8'
pageno = 1
scale = 1
caching = True
showpageno = True


fp = open(tmpfilename, 'rb')
outfp = file(output, 'w')
rsrcmgr = PDFResourceManager()


device = TagExtractor(rsrcmgr, outfp, codec=codec)

fp = file(tmpfilename, 'rb')
process_pdf(rsrcmgr, device, fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True)
fp.close()
os.remove(tmpfilename)

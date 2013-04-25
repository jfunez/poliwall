#!/usr/bin/python
import sys
import os
import requests

from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfdevice import TagExtractor
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import process_pdf


pdf_url = sys.argv[1]
output = sys.argv[2]
tmpfilename = 'tmpfile'

gfile = requests.get(pdf_url)
tfile = open(tmpfilename, 'w+b')
tfile.write(gfile.content)
tfile.close()

codec = 'utf-8'
laparams = LAParams()
imagewriter = None
password = ''
pagenos = set()
codec = 'utf-8'
scale = 1
caching = True
outtype = 'html'
layoutmode = 'normal'

fp = open(tmpfilename, 'rb')
outfp = file(output, 'w')
rsrcmgr = PDFResourceManager()

if outtype == 'text':
    device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams,
                           imagewriter=imagewriter)
elif outtype == 'xml':
    device = XMLConverter(rsrcmgr, outfp, codec=codec, laparams=laparams,
                          imagewriter=imagewriter)
elif outtype == 'html':
    device = HTMLConverter(rsrcmgr, outfp, codec=codec, scale=scale,
                           layoutmode=layoutmode, laparams=laparams,
                           imagewriter=imagewriter)
elif outtype == 'tag':
    device = TagExtractor(rsrcmgr, outfp, codec=codec)

device = TagExtractor(rsrcmgr, outfp, codec=codec)
fp = file(tmpfilename, 'rb')
process_pdf(rsrcmgr, device, fp, pagenos, maxpages=0,
            password=password, caching=caching, check_extractable=True)
fp.close()
os.remove(tmpfilename)

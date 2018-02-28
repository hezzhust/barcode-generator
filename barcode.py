#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib,urllib2;
import time



code = 'EAN13'
multiplebarcodes = 'false'

def get_image(first , second):
    mid = ''
    if second <10:
        mid = '00'
    elif second>=10 and second <100:
        mid = '0'
    else:
        mid = ''

    num = '%d%s%d' % (first ,mid, second)
    src = 'https://barcode.tec-it.com/barcode.ashx?data='+num+ \
          '&code='+ code +\
          '&multiplebarcodes='+ multiplebarcodes +\
          '&translate-esc=false&unit=Fit&dpi=96&imagetype=Gif&rotation=0&color=%23000000&bgcolor=%23ffffff&qunit=Mm&quiet=0'
    res = urllib.urlopen(src).read()
    path = "d:\dlimg\%s.gif" % (second)
    f = open(path, "wb")
    f.write(res)
    f.close()
    time.sleep(1)

first_num = 697139564
# page_size = 100
for i in range(1, 1000):
    get_image(first_num, i)


# get_image(first_num, 61)
# list = [543,556,569,574,585,587,593,598]
# for i in list:
#     get_image(first_num, i)


#!/usr/bin/env python
# coding=utf-8
import Image 
import os

pathS = raw_input("please input source dir path:")
pathD = raw_input('please input dest dir path: ')
if not os.path.exists(pathD):
    os.mkdir(pathD)
f = open('/home/sdgl/sdgl/python/dir.txt','r')
for line in f.readlines():
    print line
    im = Image.open(pathS+'/'+line.strip())
    pix = im.load()
    x,y=im.size
#    print im.size
    for i in range(0,x):
        for j in range(0,y):
            if(pix[i,j][0] in range(120,240)): 
                pix[i,j]=(255,255,255)
    im.save(pathD+"/"+line.strip())
f.close()

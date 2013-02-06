#!/usr/bin/python
# -*- coding: UTF-8 -*-


import  os
import sys

LIB_DIR = (os.path.join(os.curdir, 'LIB'))
sys.path.append(os.curdir)
sys.path.append(os.pardir)
sys.path.append(LIB_DIR)

dirs = [n for n in os.listdir(LIB_DIR) if
        os.path.isdir(os.path.join(LIB_DIR, n))]
for d in dirs:
	sys.path.append(os.path.join(LIB_DIR, d))
print map(__import__,dirs)

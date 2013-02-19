#!/usr/bin/env python
# coding: utf8

"""
导入各目录至系统路径
"""

import  os
import sys

LIB_DIR = os.path.dirname(__file__)
sys.path.append(LIB_DIR)

dirs = [n for n in os.listdir(LIB_DIR) if
        os.path.isdir(os.path.join(LIB_DIR, n))]
for d in dirs:
    sys.path.append(os.path.join(LIB_DIR, d))

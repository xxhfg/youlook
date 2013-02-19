#!/usr/bin/env python
# -*- coding: UTF8 -*-

""" docstring """

__author__ = "Hao FengGe (xxhfg@163.com)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2007/11/30 10:26:45 $"
__copyright__ = "Copyright (c) 2010 Hao FengGe"
__license__ = "Python"


import unittest
import sys
import os
import libs
import tests


from ColorUnittest.myunittest import MyTestRunner

tests = os.listdir(os.curdir)
tests = [n[:-3] for n in tests if n.startswith('test') and n.endswith('.py')]

teststests = os.path.join(os.curdir, 'tests')
if os.path.isdir(teststests):
    teststests = os.listdir(teststests)
    teststests = [n[:-3] for n in teststests
                  if n.startswith('test') and n.endswith('.py')]
    modules_to_test = tests + teststests
else:
    modules_to_test = tests


def suite():
    alltests = unittest.TestSuite()
    for module in map(__import__, modules_to_test):
        alltests.addTest(unittest.findTestCases(module))
    return alltests

if __name__ == '__main__':
    unittest.main(defaultTest='suite', testRunner=MyTestRunner())

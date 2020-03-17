#!/usr/bin/python3
# coding: utf-8
from __future__ import unicode_literals

import sys

if __package__ is None and not hasattr(sys, 'frozen'):
    import os.path
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

import src

if __name__ == '__main__':
    src.main()

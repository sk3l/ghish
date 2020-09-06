from os.path import abspath, dirname
from sys import path

PARENT_DIR = abspath(dirname(__file__))
if PARENT_DIR not in path:
    path.append(PARENT_DIR)

from distutils.core import setup
import py2exe
import glob
import os
import random
import re
import sqlite3
from pathlib import Path
from time import sleep

setup(zipfile=None,
      options={'py2exe':{"bundle_files":1}},
      windows=["hackerscript.py"])
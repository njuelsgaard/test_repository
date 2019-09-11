#!/usr/bin/env python

import sys
import sqlalchemy
from SQLiteConnection import engine, Session
from ModelClasses import *

# filename = 'student_data.txt'
# or use argparse

# data = open(filename)

session = Session()


# your code here

session.commit()

engine.dispose() # cleanly disconnect from the database
sys.exit(0)

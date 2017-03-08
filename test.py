# (c) Theresa Thoraldson 2017 | http://github.com/tthoraldson
# theresa.thoraldson@gmail.com

import sys
from flask import Flask
import xlsxwriter

# Define Flask Server
app = Flask('_test_')


# setting up workbook and worksheet
workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

@app.route('/')
def index():
    return 'App Running!'

@app.route('hello')
def hello():
    worksheet.write('A1', 'Hello world')
    workbook.close()
    return 'Complete'

# -*- coding:utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, send_file
import tushare as ts
import datetime
from urllib import quote
import os

app = Flask(__name__)
UPLOAD_FOLDER='upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))

def getYearQuarter(datePicker=None):
    if datePicker:
        [year, quarterStr] = datePicker.split(" ")
        quarter = int(quarterStr[1])
    else:
        now = datetime.datetime.now()
        quarter = (now.month / 3) if now.month % 3 == 0 else now.month / 3 + 1
        year = now.year
    return [year, quarter]

def export(exportType, datePicker):
    sb = None
    [year, quarter] = getYearQuarter(datePicker)
    if exportType == "report":
        name = "业绩报表"
        sb = ts.get_report_data(year, quarter)
    elif exportType == "profit":
        name = "盈利能力报表"
        sb = ts.get_profit_data(year, quarter)
    elif exportType == "operation":
        name = "营运能力报表"
        sb = ts.get_operation_data(year, quarter)
    elif exportType == "growth":
        name = "成长能力报表"
        sb = ts.get_growth_data(year, quarter)
    elif exportType == "debtpaying":
        name = "偿债能力报表"
        sb = ts.get_debtpaying_data(year, quarter)
    elif exportType == "cashflow":
        name = "现金流量报表"
        sb = ts.get_cashflow_data(year, quarter)

    filename = quote(name  + str(year) + "Q" +str(quarter) + ".xlsx")
    filepath = os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename)


    sb.to_excel(filepath)

    rtn = send_file(filepath, as_attachment=True)
    rtn.headers['Content-Disposition'] += "; filename*=utf-8''%s" % (filename)
    return rtn

@app.route('/')
def hello_world():
    return render_template('stock_basics.html')
    #return 'Hello World!'

@app.route('/stock/basics')
def stock_basics():
    return render_template('stock_basics.html')

@app.route('/stock/basics/export', methods=['POST'])
def stock_basics_export():
    date = ""
    year = ""
    quarter = ""
    quarters = {'Q1': '0331', 'Q2': '0630', 'Q3': '0930', 'Q4': '1231'}

    datePicker = request.form['datePicker']
    if datePicker:
        [year, quarter] = datePicker.split(" ")
        date = year + quarters.get(quarter)

    filename = quote("股票列表"+str(year)+str(quarter)+".xlsx")
    filepath = os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename)

    sb = ts.get_stock_basics(date)
    sb.to_excel(filepath)

    rtn = send_file(filepath, as_attachment=True)
    rtn.headers['Content-Disposition']+="; filename*=utf-8''%s"%(filename)
    return rtn

@app.route('/stock/report')
def stock_report():
    return render_template('stock_report.html')

@app.route('/stock/profit')
def stock_profit():
    return render_template('stock_profit.html')

@app.route('/stock/operation')
def stock_operation():
    return render_template('stock_operation.html')

@app.route('/stock/growth')
def stock_growth():
    return render_template('stock_growth.html')

@app.route('/stock/debtpaying')
def stock_debtpaying():
    return render_template('stock_debtpaying.html')

@app.route('/stock/cashflow')
def stock_cashflow():
    return render_template('stock_cashflow.html')

@app.route('/stock/export/<exportType>', methods=['GET', 'POST'])
def stock_export(exportType):
    datePicker = request.form['datePicker']
    rtn = export(exportType, datePicker)
    return rtn

if __name__ == '__main__':
    app.run(debug=True)

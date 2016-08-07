#!/usr/bin/env python
#-*- coding:utf-8 -*-

import datetime
from flask import Flask, render_template, session, request, redirect
from util import fresh_session 
from util import need_check

app = Flask(__name__)
app.debug = True

@app.route('/')
@need_check
def main():
    return render_template('index.html')

@app.route('/check', methods=['GET', 'POST', ])
def check():
    if request.method == 'GET':
        return render_template('check.html')
    else:
        passwd = request.form.get('password', '')
        if passwd == 'wyqphz517824':
            fresh_session()
            return redirect(url_for('main'))
        else:
            return redirect(url_for('check'))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')

#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import datetime
from flask import Flask, render_template, session, request, redirect, url_for
from util import fresh_session 
from util import need_check

app = Flask(__name__)
app.debug = True 
app.config['SECRET_KEY'] = os.urandom(24)

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
            return redirect('/')
        else:
            return redirect(url_for('check'))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')

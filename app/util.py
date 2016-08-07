#-*- coding: utf-8 -*-

import time
import datetime
from flask import session, redirect, url_for

def datetime_2_unixstamp(dt):
    return time.mktime(dt.timetuple())

def get_now_timestamp():
    return datetime_2_unixstamp(datetime.datetime.now())

def fresh_session():
    session['_key'] = {
        'validate': True,
        'expire': get_now_timestamp() + 60*20,
    }

def validate_session():
    _key = session.get('_key', None)
    if not _key or not _key['validate'] or _key['expire'] < get_now_timestamp():
        return False
    return True

def need_check(func):
    def _wrapped(*args, **kwargs):
        if validate_session():
            fresh_session()
            return func(*args, **kwargs)
        else:
            return redirect(url_for('check'))
    return _wrapped

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.app import app 
realapp = app

if __name__ == '__main__':
    app.run('0.0.0.0')


#!/usr/bin/env python
# coding=utf-8

from flask import Flask

supermarket = Flask(__name__)

from supermarket import views
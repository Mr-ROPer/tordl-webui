#!/usr/bin/env python3

import asyncio
import json

from flask import Flask, render_template, request
from tordl.func import run_api

app = Flask(__name__)
lp = asyncio.get_event_loop()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def search():
    query = request.form['search']
    response = run_api(query, loop=lp)
    j = json.loads(response)

    res = sorted(j['result'], key=lambda x: x['seeds'], reverse=True)
    return render_template('index.html', search_query=query, rows=res)

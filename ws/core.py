#!/usr/bin/env python3

import asyncio
import json

from flask import Flask, render_template, request
from tordl.func import run_api

app = Flask(__name__)
lp = asyncio.get_event_loop()

columns = {
    'name': 'Name',
    'links': 'Link',
    'magnet': 'Magnet',
    'origins': 'Origin',
    'seeds': 'Seeders',
    'leeches': 'Leechers',
    'size': 'Size'
}

@app.route('/')
def index():
    return render_template('index.html', cols=columns)

@app.route('/', methods=['POST'])
def search():
    query = request.form['search']
    response = run_api(query, loop=lp)
    j = json.loads(response)

    sort = request.form['sort-by']
    sort_rev = request.form['sort-order'] == 'descending'

    res = sorted(j['result'], key=lambda x: x[sort], reverse=sort_rev)
    return render_template(
        'index.html',
        cols=columns,
        query=query,
        res=res,
        sort=sort
    )

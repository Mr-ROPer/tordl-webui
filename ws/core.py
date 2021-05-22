#!/usr/bin/env python3

import asyncio
import json

from flask import Flask, render_template
from tordl.func import run_api

app = Flask(__name__)
lp = asyncio.get_event_loop()

@app.route('/')
def index():
    # Haven't implemented the search box yet, but it won't take long.
    s = run_api('flac', loop=lp)
    j = json.loads(s)
    return render_template('index.html', rows=j['result'])

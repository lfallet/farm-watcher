from flask import Flask, render_template, url_for, g
# session, redirect, escape, request
from datetime import datetime
# import os
import sqlite3

DATABASE = './database.db'

app = Flask(__name__)

# ping route to monitor the uptime
@app.route('/ping')
def ping():
  return 'up'

# main route, dashboard
@app.route('/')
def index():
  now = datetime.now()
  return render_template('index.html',
                         now=now)

# prevent execution by requiring from another script
if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=80)


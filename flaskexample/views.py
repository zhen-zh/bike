from flask import render_template
from flaskexample import app

@app.route('/')
@app.route('/index')
def index():
   user = { 'nickname': 'Miguel' } # fake user
   return render_template("index.html",
       title = 'Home',
       user = user)
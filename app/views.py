from flask import render_template, flash, redirect
from app import app
from visual import *

@app.route('/')
def index():
	tag_class_dict = get_tags('http://vignette1.wikia.nocookie.net/joke-battles/images/4/40/18360-doge-doge-simple.jpg/revision/latest?cb=20151209161638')
	return render_template('index.html', tags=tag_class_dict)
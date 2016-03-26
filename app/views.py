from flask import render_template, flash, redirect
from app import app
from visual import *

@app.route('/')
def index():
	img_url = 'http://vignette1.wikia.nocookie.net/joke-battles/images/4/40/18360-doge-doge-simple.jpg/revision/latest?cb=20151209161638'
	tags_dict = get_tags(img_url)
	return render_template('index.html', tags=tags_dict, img=img_url)
from flask import render_template, flash, redirect
from app import app
from visual import *
from .forms import UrlForm

@app.route('/', methods=['GET', 'POST'])
def index():
	form = UrlForm()
	img_url = ''
	tag_tuples = []

	if form.validate_on_submit():
		img_url = str(form.imageurl.data)
		tag_tuples = get_tags(img_url)

	# img_url = 'http://vignette1.wikia.nocookie.net/joke-battles/images/4/40/18360-doge-doge-simple.jpg/revision/latest?cb=20151209161638'
	return render_template('index.html', tags=tag_tuples, img=img_url, form=form)
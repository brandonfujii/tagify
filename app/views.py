from flask import render_template, flash, redirect, url_for, request, abort
from  werkzeug.debug import get_current_traceback
from app import app
from visual import *
from .forms import *

@app.route('/', methods=['GET', 'POST'])
def index():
	form = UrlForm()
	img_url = ''
	tag_tuples = []

	if form.validate_on_submit():
		img_url = str(form.imageurl.data)
		tag_tuples = get_tags_from_url(img_url)

	# img_url = 'http://vignette1.wikia.nocookie.net/joke-battles/images/4/40/18360-doge-doge-simple.jpg/revision/latest?cb=20151209161638'
	return render_template('index.html', tags=tag_tuples, img=img_url, form=form)

# @app.route('/file', methods=['GET', 'POST'])
# def file():
#     form = PhotoForm()
#     filename = ''
#     if form.validate_on_submit():
#         filename = secure_filename(form.fileName.file.filename)
#         form.fileName.file.save('file/' + filename)

#     return render_template('file.html', form=form, filename=filename)

	
@app.errorhandler(500)
def internal_error(error):
  return "500 Internal Error"

@app.errorhandler(404)
def not_found(error):
	return "404 Error: Page not found", 404
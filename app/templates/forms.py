from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from werkzeug import secure_filename
from flask_wtf.file import FileField


class UrlForm(Form): 
	imageurl = StringField('imageurl', validators=[DataRequired()])

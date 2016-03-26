from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class UrlForm(Form): 
	imageurl = StringField('imageurl', validators=[DataRequired()])
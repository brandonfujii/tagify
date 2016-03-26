#!/usr/bin/python

from clarifai.client import ClarifaiApi
import re
from convertjson import *

clarifai_api = ClarifaiApi() # assumes environment variables are set.

# filename = 'tags.txt'
# f = open(filename, 'w')
# f.write(str(result))
tmp_dict = {}

def get_tags(img_url):
	result = clarifai_api.tag_image_urls(img_url)
	return generate_dict(convert_from_unicode(result))
	# generate_dict(convert_keys_to_string(result))

def generate_dict(data):
	tmp_dict.clear()
	probs = re.search(r'\'probs\': \[([^]]*)\]', str(data)).group(1).split(',')
	tag_classes = re.search(r'\'classes\': \[([^]]*)\]', str(data)).group(1)
	tags = re.findall(r"\'([0-9a-zA-Z_\s]+)\'", tag_classes)

	if probs and tags and len(probs) == len(tags):
		for tag in tags:
			for prob in probs:
				tmp_dict[tag] = prob
		return tmp_dict

	else: 
		print "Error: Not Found"

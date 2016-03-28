#!/usr/bin/python

from clarifai.client import ClarifaiApi
import re
from convertjson import *
import operator

clarifai_api = ClarifaiApi() # assumes environment variables are set.

def get_tags_from_url(img_url):
	result = clarifai_api.tag_image_urls(img_url)
	tag_dict = generate_dict(convert_from_unicode(result))
	return get_tuples_from_dict(tag_dict)

def generate_dict(data):
	probs = map(float, re.search(r'\'probs\': \[([^]]*)\]', str(data)).group(1).split(','))
	tag_classes = re.search(r'\'classes\': \[([^]]*)\]', str(data)).group(1)
	tags = re.findall(r"\'([0-9a-zA-Z_\s]+)\'", tag_classes)

	if probs and tags and len(probs) == len(tags):
		tmp_dict = dict(zip(tags, probs))
		return tmp_dict

	else: 
		print "Error: Not Found"

def get_tuples_from_dict(dictionary):
	# generate tuples and order by probability (greatest -> least)
	sorted_tuples = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
	return sorted_tuples
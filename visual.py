#!/usr/bin/python

from clarifai.client import ClarifaiApi
import re

clarifai_api = ClarifaiApi() # assumes environment variables are set.

# filename = 'tags.txt'
# f = open(filename, 'w')
# f.write(str(result))

tag_dict = {}

def get_tags(img_url):
	result = clarifai_api.tag_image_urls(img_url)
	generate_tuples(result)

def generate_dict(tags):
	probs = re.search(r'\'probs\': \[([^]]*)\]', str(tags)).group(1).split(',')
	tag_classes = re.search(r'\'classes\': \[([^]]*)\]', str(tags)).group(1).split(',')
	if probs and tag_classes and len(probs) == len(tag_classes):
		for tag_class in tag_classes:
			for prob in probs:
				tag_dict[tag_class] = prob
		print tag_dict
	else: 
		print "Error: Not Found"

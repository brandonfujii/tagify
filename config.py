#!/usr/bin/python

from clarifai.client import ClarifaiApi

clarifai_api = ClarifaiApi() # assumes environment variables are set.

# filename = 'tags.txt'
# f = open(filename, 'w')
# f.write(str(result))


def find_tags(img_url):
	result = clarifai_api.tag_image_urls(img_url)
	print result




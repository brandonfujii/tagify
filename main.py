#!/usr/bin/python

# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def index():
# 	return "Index page"


# if __name__ == '__main__':
# 	app.run(debug=True)

import sys
import visual

def main():
	if len(sys.argv) != 3:
		print "usage: ./main.py --findtags {{img_url}}"
		sys.exit(1)

	option = sys.argv[1]
	img_url = sys.argv[2]

	visual.get_tags(img_url)


if __name__ == '__main__':
  main()
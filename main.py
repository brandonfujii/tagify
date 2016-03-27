#!/usr/bin/python


import sys
from app.visual import *
from app.validate import url_exists

def main():
	if len(sys.argv) != 3:
		print "usage: ./main.py --findtags {{img_url}}"
		sys.exit(1)

	option = sys.argv[1]
	img_url = sys.argv[2]

	tmp = get_tags(img_url)
	print tmp

if __name__ == '__main__':
  main()
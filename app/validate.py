import httplib

def url_exists(site, path):
	connection = httplib.HTTPConnection(site)
	connection.request('HEAD', path)
	response = connection.getresponse()
	connection.close()
	# If response status is not 200, then the url doesn't exist
	return response.status == 200


import httplib2
import six
import simplejson
from instagram.client import InstagramAPI
import os

IG_CLIENT_ID = os.environ.get('IG_CLIENT_ID', 0)
IG_CLIENT_SECRET = os.environ.get('IG_CLIENT_SECRET', 0)

api = InstagramAPI(client_id=IG_CLIENT_ID, client_secret=IG_CLIENT_SECRET)
popular_media = api.media_popular(count=20)
for media in popular_media:
    print media.images['standard_resolution'].url
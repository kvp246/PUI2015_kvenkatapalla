import sys
import json
import datetime
import urllib2

if __name__=='__main__':
    url = 'https://nycopendata.socrata.com/views/%s' % (sys.argv[1])
    request = urllib2.urlopen(url)
    metadata = json.loads(request.read())
    print datetime.datetime.fromtimestamp(metadata['createdAt'])

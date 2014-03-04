__author__ = 'Administrator'
#submit_get.py
import urllib2,urllib,sys
def add_Data(url,data):
    return url+"?"+urllib.urlencode(data)
zipcode = 'chengdu'
#url = add_Data("http://www.wunderground.com/cgi-bin/findweather/getForecast",[('query',zipcode)])
url = add_Data("http://www.wunderground.com/cgi-bin/findweather/getForecast",{'query':zipcode})
print url
try:
    req = urllib2.Request(url)
    fd = urllib2.urlopen(req)
except urllib2.URLError,e:
    print "Error retrieving data:",e
    sys.exit(1)

while 1:
    data = fd.readline(1024)
    if not  len(data):
        break
    sys.stdout.write(data)

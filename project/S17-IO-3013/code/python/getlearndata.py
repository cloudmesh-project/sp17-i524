import urllib2 

url = "http://static.echonest.com/millionsongsubset_full.tar.gz"

print "downloading file " 

f = urllib2.urlopen(url)
print "opening url"
data = f.read()
print "start download" 
with open("code2.zip", "wb") as code:
	code.write(data)

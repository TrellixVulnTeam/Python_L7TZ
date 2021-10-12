import urllib2
auth = urllib2.HTTPBasicAuthHandler()
auth.add_password(user="admin", passwd="tom7", realm="Apache tomcat", uri="http://localhost:8080/probe")
opener = urllib2.install_opener(auth)
urllib2.install_opener(opener)
response = urllib2.urlopen("http://localhost:8080/probe")
response.getcode()
for header, value in response.headers.items():
    print (header + " : " + value)
import httplib2
conn = httplib.HTTPSConnection("www.google.com.br")
#conn = httplib.HTTPConnection("www.google.com.br")
headers = {}
params = {}
conn.request("GET"," ",params, headers)
response = conn.getresponse()
###dir(conn)
print (response)
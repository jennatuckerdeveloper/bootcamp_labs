#API - application program interface
#it's a way for our operating system to interact with outside programs
#on the web, there are API's for all kinds of stuff
#Square, Paypal, Ebay
#Amazon web services has a lot of them
#Google has them for maps
#some service has a large set of data, you want access, they want to give you access
#so an API is a way to allow that to happen without giving you too much access

#what's a VPN?

#there is a package called requests
#it's not part of the Python standard library
#so you can't just say:  import requests

#command line entry:  pip3 list
#command line entry:  pip3 install requests
#we can also do a pip3 uninstall -whatever-
import requests

r = requests.get('http://api.icndb.com/jokes/random', auth=('user', 'pass'))
#this API is not locked down, we don't need any passwords or anything to get in there
r.status_code
#requests wants to know if it's a get or a post, which way is info going
#so in this case, we're asking the server for information
#with a post request, we would be trying to give the server information
json_data = r.json()
print(json_data['value']['id'])
print(jason_data['value']['joke'])

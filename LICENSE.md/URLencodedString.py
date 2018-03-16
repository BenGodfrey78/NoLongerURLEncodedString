import urllib 
print ('Put in qoute ""')
url = input('Input Here:')
urllib.unquote(url).decode('utf8')
print ""
print urllib.unquote(url).decode('utf8')

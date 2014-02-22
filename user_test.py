import os
from url_regex import create_regex
urlList = []
print "Enter URLs or -- to quit: "
while True:
    url = raw_input()
    if url == "--":
        break
    urlList.append(url)
    

print create_regex(urlList).pattern
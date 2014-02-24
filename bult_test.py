from url_regex import create_regex
from test_data import * 

REGEX = create_regex(test_urls_4)
print REGEX.pattern
for u in test_urls_4:
	print REGEX.findall(u)
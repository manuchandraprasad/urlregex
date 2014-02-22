from test_data import *


def long_substr(data):
    """
    Prints the longest string that is common in the list of strings provided
    Source: http://stackoverflow.com/questions/2892931/longest-common-substring-from-more-than-two-strings-python
    """
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0]) - i + 1):
                if j > len(substr) and all(data[0][i:i + j] in x for x in data):
                    substr = data[0][i:i + j]
    return substr

"""
Idea is to find the only changing part from the URL and make a regular expression out of it. 

1.First find the longest common substring prefix
2.The remove it from the urls and obtain a list of the remaining URL
3.Repeat one till there is no more LCS 
4.Make pattern from the list LCSs
"""

def find_common_substr(data):
    longest_common_substrings = []
    while(long_substr(data)):
        lcs = long_substr(data)
        print data
        new_data = []
        for url in data:
            new_data.append(url.replace(lcs,''))
        data = new_data
        print new_data


find_common_substr(test_urls)        
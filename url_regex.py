from test_data import *
import re

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


def substring_pos(string,substring):
    """
    Find the position of the substring in the given string and substitute ^ at boundaries
    """
    pos = string.index(substring)
    if pos == 0:
        #Substring is in the begining of string
        return substring+"^"
    elif pos == len(string)-len(substring):
        #Substring is in the end of the string
        return "^"+substring 
    else:
        return "^"+substring+"^"


def find_common_substrs(data):
    """
    Find the list of longest common substrings in a given list of URLs (strings) 
    Returns a list of strings with ^ substituted at the boundaries
    """
    longest_common_substrings = []
    while(long_substr(data)):
        lcs = long_substr(data)
        subs = substring_pos(data[0], lcs)
        longest_common_substrings.append(subs)
        new_data = []
        for url in data:
            new_data.append(url.replace(lcs,''))
        data = new_data
    return longest_common_substrings

def create_regex(data):
    """
    Replaces the ^ character to add '.+' regex 
    """
    #FIXME: Improve code to find the data type of the variable part and use a regex rule to replace it 
    s = ("".join(find_common_substrs(data)))
    s = re.escape(s) 
    s = s.replace('\^','^')
    s = s.replace('^^','.+')
    s = s.replace('^','.+')
    return re.compile(s)


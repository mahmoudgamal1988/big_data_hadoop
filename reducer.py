#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

translation = []
word = None

words = {}
# input comes from STDIN
s = " Ahmed Mohamed /n asd sdf"
#for line in sys.stdin:
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    word, translation = line.split('\t',1)
   
    if word not in words.keys():
        words[word]=[ translation]
    else:
        words[word].append(translation)
for key in words.keys():
    a =words.get(key)
    s= str('|'.join(x for x in a))
    print(key,s)

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer


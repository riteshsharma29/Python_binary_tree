#!/usr/bin/python

import bintrees
import pandas as pd
import sys


'''
Documentation :

https://pypi.python.org/pypi/bintrees
http://www.bintreepython.net/

'''

df = pd.read_csv('titanic_data.csv')

#print df['PassengerId'].values

pass_name = df['Name'].values
pass_age = df['Age'].values

#create iterator of tuples.
mylist = zip(pass_name,pass_age)

#create a dictionary 
mydict = dict(mylist)

#create a binary tree
t = bintrees.FastBinaryTree(mydict)

k = [x for x in t.keys()]
v = [y for y in t.values()]

#!/usr/bin/python

import bintrees

mydict = {

    "python" : ".py",
    "java" : ".java",
    "php" : ".php",
    "ruby" : ".ruby"

}

t = bintrees.FastBinaryTree(mydict)

#from list k,v pair
t.update([("vba",".vb"), ("pwscript",".ps")])

#from dict sequence
t.update({"R":".R","DotNet":".net"})

#inert item
t.insert("Objective-C","OC")

#create a tree from a tree
t_2 = bintrees.FastBinaryTree(t)

#remove item by passing a key
t.remove("R") 

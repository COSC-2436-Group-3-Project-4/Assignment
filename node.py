"""
File: node.py

Node classes for one-way linked structures and two-way
linked structures.
"""

class Node(object):

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next

class DNode():
    def __init__(self,data,next=None,previous=None):
        self.data = data
        self.next = next
        self.previous = previous
        

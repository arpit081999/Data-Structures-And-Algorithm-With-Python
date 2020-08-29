# -*- coding: utf-8 -*-
"""
@author: Arpit Somani
"""

class newNode: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def _deleteTree(node): 
	if (node == None): 
		return

	_deleteTree(node.left) 
	_deleteTree(node.right) 

	print("Deleting node: ", 
				node.data) 
	node = None

def deleteTree(node_ref): 
	_deleteTree(node_ref[0]) 
	node_ref[0] = None

root = [0] 
root[0] = newNode(1) 
root[0].left = newNode(2) 
root[0].right = newNode(3) 
root[0].left.left = newNode(4) 
root[0].left.right = newNode(5) 

deleteTree(root) 
print("Tree deleted ") 

# -*- coding: utf-8 -*-
"""
@author: Arpit Somani
"""



class Node: 
	def __init__(self, key): 
		self.key = key 
		self.left = None
		self.right = None

def createNode(parent, i, created, root): 

	if created[i] is not None: 
		return

	created[i] = Node(i) 

	if parent[i] == -1: 
		root[0] = created[i] 
		return

	if created[parent[i]] is None: 
		createNode(parent, parent[i], created, root ) 

	p = created[parent[i]] 

	if p.left is None: 
		p.left = created[i] 
	else: 
		p.right = created[i] 


def createTree(parent): 
	n = len(parent) 

	created = [None for i in range(n+1)] 
	
	root = [None] 
	for i in range(n): 
		createNode(parent, i, created, root) 

	return root[0] 
 
def inorder(root): 
	if root is not None: 
		inorder(root.left) 
		print( root.key)
		inorder(root.right) 

parent = [-1, 0, 0, 1, 1, 3, 5] 
root = createTree(parent) 
print ("Inorder Traversal of constructed tree")
inorder(root) 


# -*- coding: utf-8 -*-
"""
@author: Arpit Somani
"""


class newNode(): 

	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
		
		
def getfullCount(root): 

	if (root == None): 
		return 0
	
	res = 0
	if (root.left and root.right): 
		res += 1
	
	res += (getfullCount(root.left) +
			getfullCount(root.right)) 
	return res 


if __name__ == '__main__': 
	root = newNode(2) 
	root.left = newNode(7) 
	root.right = newNode(5) 
	root.left.right = newNode(6) 
	root.left.right.left = newNode(1) 
	root.left.right.right = newNode(11) 
	root.right.right = newNode(9) 
	root.right.right.left = newNode(4) 
	
	print(getfullCount(root)) 
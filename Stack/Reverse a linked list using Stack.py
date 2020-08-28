# -*- coding: utf-8 -*-
"""
@author: Arpit Somani
"""



class Node: 
	def __init__(self, next = None, data = None): 
		self.next = next
		self.data = data 


def push( head_ref, new_data): 

	new_node = Node() 
	new_node.data = new_data 
	new_node.next = (head_ref) 
	(head_ref) = new_node 
	return head_ref 

def getCount( head): 

	count = 0 
	current = head  
	while (current != None): 
	
		count = count + 1
		current = current.next
	
	return count 

def getNth( head, n): 

	curr = head 
	i = 0
	while( i < n - 1 and curr != None ): 
		curr = curr.next
		i = i + 1
	return curr.data 

def printReverse(head): 

	stk = [] 
	ptr = head 
	while (ptr != None): 
	
		stk.append(ptr) 
		ptr = ptr.next
	

	while (len(stk) > 0): 
	
		print( stk[-1].data, end = " ") 
		stk.pop() 
	
	print( " ") 


head = None
q=int(input("How many total elements to push:"))

for i in range (0,q):
    a=int(input("Enter "+str(i+1)+" element to push:"))
    head = push(head, a) 
print(" ")


printReverse(head) 


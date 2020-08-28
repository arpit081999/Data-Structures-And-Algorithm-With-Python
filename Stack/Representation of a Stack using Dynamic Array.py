# -*- coding: utf-8 -*-
"""
@author: Arpit Somani
"""


class Node: 
	
	#create nodes of linked list 
	
	def __init__(self,data): 
		self.data = data 
		self.next = None
	
class Stack: 
	
	# default is NULL 
	def __init__(self): 
		self.head = None
	
	# Checks if stack is empty 
	def isempty(self): 
		if self.head == None: 
			return True
		else: 
			return False
	

	# add item to stack 
	def push(self,data): 
		
		if self.head == None: 
			self.head=Node(data) 
			
		else: 
			newnode = Node(data) 
			newnode.next = self.head 
			self.head = newnode 
	
	# Remove element from stack
	def pop(self): 
		
		if self.isempty(): 
			return None
		#make a new top element after popping	
		else:  
			poppednode = self.head 
			self.head = self.head.next
			poppednode.next = None
			return poppednode.data 
	
	#top element in stack
	def peek(self): 
		
		if self.isempty(): 
			return None
			
		else: 
			return self.head.data 
	
		 
	def display(self): 
		
		fnode = self.head 
		if self.isempty(): 
			print("Stack Underflow") 
		
		else: 
			
			while(fnode != None): 
                
				print(fnode.data,end = " ") 
				fnode = fnode.next
			return
		
mystack = Stack() 

q=int(input("How many total elements to push:"))

for i in range (0,q):
    a=int(input("Enter "+str(i+1)+" element to push:"))
    mystack.push(a) 
print(" ")

mystack.display() 

print("\nBefore pop, Top (peek) element is ",mystack.peek()) 
 
mystack.pop() 

mystack.display() 

print("\nAfter pop, Top (peek) element is ", mystack.peek()) 

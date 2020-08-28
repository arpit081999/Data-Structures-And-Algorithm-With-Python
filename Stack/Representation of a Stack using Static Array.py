# -*- coding: utf-8 -*-
"""
@author: Arpit Somani
"""



from sys import maxsize 

# Create a stack.
def createStack(): 
	mystack = [] 
	return mystack 

# Check Stack is empty  
def isEmpty(mystack): 
	return len(mystack) == 0

# Add an item to stack.
def push(mystack, item): 
	mystack.append(item) 
	print(item + " pushed to stack ") 
	
# Remove an item from stack. 
def pop(mystack): 
	if (isEmpty(mystack)): 
		return str(-maxsize -1) # return minus infinite 
	
	return mystack.pop() 

# Return the top from stack
def peek(mystack): 
	if (isEmpty(mystack)): 
		return str(-maxsize -1) 
	return mystack[len(mystack) - 1] 

 
mystack = createStack() 

q=int(input("How many total elements to push:"))

for i in range (0,q):
    a=int(input("Enter "+str(i+1)+" element to push:"))
    push(mystack, str(a))
print(" ")

print("Pop in process...")
print("Popped item from stack: " + pop(mystack))
print(" ")

print("Stack after popping an element: " + str(mystack))

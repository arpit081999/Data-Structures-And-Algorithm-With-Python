# -*- coding: utf-8 -*-
"""
@author: Arpit Somani
"""


# Create a stack
def create_stack():
    mystack = []
    return mystack


# Create empty stack
def check_empty(mystack):
    return len(mystack) == 0


# Add items into the stack
def push(stack, item):
    stack.append(item)
    


# Remove an element from the stack
def pop(mystack):
    if (check_empty(mystack)):
        return "stack is empty"

    return mystack.pop()

mystack = create_stack()
q=int(input("Enter element to do factorial :"))
if q<0:
	print("Enter a number greater than 0, to do a factorail !")
else:

	for i in range (0,q):
	    
	    push(mystack, str(i+1))
	print(" ")
ans=1
for i in range(0,q):
	s=int(pop(mystack))
	ans=ans *  s
	
print("Factorial of ",q,"is",ans)

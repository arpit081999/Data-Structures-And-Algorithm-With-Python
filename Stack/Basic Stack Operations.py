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
    print("pushed item: " + item)


# Remove an element from the stack
def pop(mystack):
    if (check_empty(mystack)):
        return "stack is empty"

    return mystack.pop()


mystack = create_stack()
q=int(input("How many total elements to push:"))

for i in range (0,q):
    a=int(input("Enter "+str(i+1)+" element to push:"))
    push(mystack, str(a))
print(" ")

print("Pop in process...")
print("Popped item: " + pop(mystack))
print(" ")

print("Stack after popping an element: " + str(mystack))
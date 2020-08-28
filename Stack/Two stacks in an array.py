# -*- coding: utf-8 -*-
"""
@author: Arpit Somani
"""


class twoStacks: 
	
	def __init__(self, n):	
		self.size = n 
		self.arr = [None] * n 
		self.top1 = -1
		self.top2 = self.size 
		
	#push element x to stack1 
	def push1(self, x): 
		
		#empty space for new element is must
		if self.top1 < self.top2 - 1 : 
			self.top1 = self.top1 + 1
			self.arr[self.top1] = x 

		else: 
			print("Stack Overflow ") 
			exit(1) 

	#push element x to stack2 
	def push2(self, x): 

		# There is at least one empty space for new element 
		if self.top1 < self.top2 - 1: 
			self.top2 = self.top2 - 1
			self.arr[self.top2] = x 

		else : 
                        print("Stack Overflow ") 
                        exit(1) 

	#pop from first stack 
	def pop1(self): 
		if self.top1 >= 0: 
			x = self.arr[self.top1] 
			self.top1 = self.top1 -1
			return x 
		else: 
			print("Stack Underflow ") 
			exit(1) 

	#pop from second stack 
	def pop2(self): 
		if self.top2 < self.size: 
			x = self.arr[self.top2] 
			self.top2 = self.top2 + 1
			return x 
		else: 
			print("Stack Underflow ") 
			exit() 


arr = twoStacks(5) 
#remember the size limit of array is fixed, so from both stack push elements, keeping the size of array in mind. 
arr.push1(4) 
arr.push2(7) 
arr.push2(6) 
arr.push1(9) 
arr.push2(12) 
#now size of array is full
#pop from either one of the stack
print("Popped item of stack1 : " + str(arr.pop1())) 
arr.push2(30) 
print("Popped item of stack2 : " + str(arr.pop2())) 


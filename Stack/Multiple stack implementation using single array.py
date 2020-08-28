# -*- coding: utf-8 -*-
"""
@author: Arpit Somani
"""



class KStacks: 
	
	def __init__(self, k, n): 
		self.k = k
		self.n = n 

		 
		self.arr = [0] * self.n 

		# stacks must empty
		self.top = [-1] * self.k 
 
		self.free = 0
 
		self.next = [i + 1 for i in range(self.n)] 
		self.next[self.n - 1] = -1

	# Check stack is empty. 
	def isEmpty(self, sn): 
		return self.top[sn] == -1


	def isFull(self): 
		return self.free == -1

	# push item into po stack
	def push(self, item, po): 
		if self.isFull(): 
			print("Stack Overflow") 
			return

        
		insert_at = self.free 
 
		self.free = self.next[self.free] 
 
		self.arr[insert_at] = item 

		self.next[insert_at] = self.top[po] 

		self.top[po] = insert_at 

	def pop(self, po): 
		if self.isEmpty(po): 
			return None

		top_of_stack = self.top[po] 

		self.top[po] = self.next[self.top[po]] 

		self.next[top_of_stack] = self.free 
		self.free = top_of_stack 

		return self.arr[top_of_stack] 

	def printstack(self, po): 
		top_index = self.top[po] 
		while (top_index != -1): 
			print(self.arr[top_index]) 
			top_index = self.next[top_index] 

if __name__ == "__main__": 
	

        #using 3 atack
        #array size is 3
	kstacks = KStacks(3, 10) 

	# Push item in stack-2. 
	kstacks.push(10, 2) 
	kstacks.push(20, 2) 

	# Push item in stack-1.
	kstacks.push(15, 1) 
	kstacks.push(16, 1) 
	kstacks.push(17, 1) 

	# Push item in stack-0.
	kstacks.push(70, 0) 
	kstacks.push(80, 0) 
	kstacks.push(90, 0) 

	print("Popped element from stack 2 is " +
						str(kstacks.pop(2))) 
	print("Popped element from stack 1 is " +
						str(kstacks.pop(1))) 
	print("Popped element from stack 0 is " +
						str(kstacks.pop(0))) 
    
	print('element of stack no.2 :' )
	kstacks.printstack(2)
	print('element of stack no.1 :' )
	kstacks.printstack(1)
	print('element of stack no.0 :' )
	kstacks.printstack(0)


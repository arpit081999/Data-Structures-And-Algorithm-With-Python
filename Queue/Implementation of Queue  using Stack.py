# -*- coding: utf-8 -*-
"""
@author: Arpit Somani
"""

class Queue: 
	def __init__(self): 
		self.s = [] 
		
	def enQueue(self, data): 
		self.s.append(data) 

	def deQueue(self): 
		# Return if queue is empty 
		if len(self.s) <= 0: 
			print('Queue is empty') 
			return

		x = self.s[len(self.s) - 1] 
		self.s.pop() 

		if len(self.s) <= 0: 
			return x 

		item = self.deQueue() 

		self.s.append(x) 

		return item 
	
if __name__ == '__main__': 
	q = Queue() 
	q.enQueue(1) 
	q.enQueue(2) 
	q.enQueue(3) 
	
	print(q.deQueue()) 
	print(q.deQueue()) 
	print(q.deQueue()) 


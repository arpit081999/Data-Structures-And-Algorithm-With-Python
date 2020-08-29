# -*- coding: utf-8 -*-
"""
@author: arpit
"""

class Queue: 
 
	def __init__(self, c): 
		
		self.queue = [] 
		self.front = self.rear = 0
		self.capacity = c 

	def queueEnqueue(self, data): 

		if(self.capacity == self.rear): 
			print("\nOOPS! Queue is full") 

		else: 
			self.queue.append(data) 
			self.rear += 1
 
	def queueDequeue(self): 

		if(self.front == self.rear): 
			print("Queue is empty") 

		else: 
			x = self.queue.pop(0) 
			self.rear -= 1

	def queueDisplay(self): 
		
		if(self.front == self.rear): 
			print("\nRight now Queue is Empty, lets enqueue items!") 

		for i in self.queue: 
			print(i, " ", end = '') 



if __name__=='__main__': 

	t=int(input("Enter size of  array to represent as queue:"))
	q = Queue(t) 

	q.queueDisplay() 

	for i in range (0,t):
	    a=int(input("Enter "+str(i+1)+" item to enqueue:"))
	    q.queueEnqueue(a)
		
	q.queueDisplay() 

	u=int(input("Lets Check can we put more items than its actual size! give one more item to enqueue:"))
	q.queueEnqueue(u) 
	
	r=print("Dequeue in process: ")
	q.queueDequeue() 

	print("\n\nAter performing dqueue successfully!, the remaining items are :\n") 

	q.queueDisplay() 


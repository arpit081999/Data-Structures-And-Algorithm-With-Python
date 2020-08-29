# -*- coding: utf-8 -*-
"""
@author: Arpit Somani
"""


class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next


def printList(head):

	ptr = head
	while ptr:
		print(ptr.data, end=" -> ")
		ptr = ptr.next
	print("None")


if __name__ == '__main__':

	e = Node(5, None)	 
	d = Node(4, e)
	c = Node(3, d)
	b = Node(2, c)
	a = Node(1, b)		

	head = a
	printList(head)

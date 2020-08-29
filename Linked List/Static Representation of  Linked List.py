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
		print(ptr.data, end = " -> ")
		ptr = ptr.next
	print("None")

def createStaticList(A):

	for i in range(len(A)):
		node[i] = Node(A[i], None)
		if i > 0:
			node[i - 1].next = node[i]
	return node[0]

if __name__ == '__main__':

	A = [1, 2, 3, 4, 5]
	N = len(A)

	node = [Node()] * N
	head = createStaticList(A)
	printList(head)

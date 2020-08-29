# -*- coding: utf-8 -*-
"""
@author: arpit
"""


class Queue:

    def __init__(self):
        self.queue = []

    # Add item
    def enqueue(self, item):
        self.queue.append(item)

    # Remove item
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()
t=int(input("How many total elements to enqueue:"))

for i in range (0,t):
    a=int(input("Enter "+str(i+1)+" element to enqueue:"))
    q.enqueue(a)
print(" ")

print(" Queue after complete Enqueue :")
q.display()

q.dequeue()

print("Dequeue successfully performed! Now the Queue is :")
q.display()
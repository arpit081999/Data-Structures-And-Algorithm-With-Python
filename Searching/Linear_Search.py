# -*- coding: utf-8 -*-
"""
@author: Arpit Somani
"""

def linear_search(n,x):
	element=[]
	for i in range(1,n):
		element.append(i)
		
	count=0
	flag=0
	for i in element:
		count+=1
		
		if(i==x):
			print("Yes! I found my number at position"+str(i))
			flag=1
			break;
			
		if(flag==0):
			print("Number is not found")
			
	print("Number of iterations:"+str(count))

linear_search(50,5)
#This is also a disadvantage of lenear search, if in 1 lakh numbers, i want to find a number which is at last position among 1 lakh, so this will undergo 1 lakh iterations, which is not efficient.
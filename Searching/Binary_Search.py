# -*- coding: utf-8 -*-
"""
@author: Arpit Somani
"""

def binary_search(a,x):
	first_pos=0
	last_pos=len(a)-1
	flag=0   #means element is not been found yet.
	count=0
	
	while(first_pos<=last_pos and flag==0):
		count+=1
		mid=(first_pos+last_pos)//2
		
		if(x==a[mid]):
			flag=1
			print("Element is present at position: "+str(mid))
			print("No. of iterations are: "+str(count))
			return
		else:
			if(x<a[mid]):
				last_pos=mid-1
			else:
				first_pos=mid+1
				
	print("The no. is not present")
	
	
a=[]
for i in range(1,101):
	a.append(i)
	
binary_search(a,4)

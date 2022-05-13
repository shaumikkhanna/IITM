import numpy as np


file = open("test.py",'w')

def vec_addition(u,v):  
	if u.shape == v.shape: 
		return u + v
import random

def generate():
	x = hex(random.randint(2**256,2**257-1))
	return x
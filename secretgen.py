from Crypto.Random import get_random_bytes

def generate():
	x = str(get_random_bytes(32).hex())
	x = '0x' + x
	# print(len(str(x)))
	return x
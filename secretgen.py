from Crypto.Random import get_random_bytes


def generate():
	"""
	generates random 128-bits secret
	"""
	x = str(get_random_bytes(16).hex())
	x = '0x' + x
	return x
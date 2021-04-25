import sys
from Crypto.Protocol.SecretSharing import Shamir
import secretgen
from Crypto.Random import get_random_bytes
# int('0x11',16)
# print(sys.argv[1])


if __name__ == '__main__':

	print("=== WELCOME TO SHAMIR SPLITTER ===")

	arg = sys.argv[1]

	if(arg == 'generate'):
		print('\nGenerated key:')
		print(secretgen.generate())
	elif(arg == 'split'):
		print('\nInput secret:')

		# secret_str = input()
		secret_str = "0x1b93527e"
		# secret_int = int(secret_str, 16)
		secret_bytes = bytes.fromhex(secret_str[2:])
		print('\nInput N T:')

		# nt_strs = input().split()
		nt_strs = "10 3"

		n = nt_strs[0]
		t = nt_strs[1]

		exam = get_random_bytes(16)
		shares = Shamir.split(2, 5, exam)

		for idx, share in shares:
			print("Index {}: {}".format(idx, share.hex()))
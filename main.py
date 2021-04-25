import sys
from Crypto.Protocol.SecretSharing import Shamir
import secretgen
from Crypto.Random import get_random_bytes
import binascii

if __name__ == '__main__':
    print("=== WELCOME TO SHAMIR SPLITTER ===")
    arg = sys.argv[1]

    if(arg == 'generate'):
        print('\nGenerated key:')
        print(secretgen.generate())

    elif(arg == 'split'):

        print('\nInput secret:')
        secret_str = input()
        secret_bytes = bytes.fromhex(secret_str[2:])

        print('\nInput N T (N >= T):')
        nt_strs = input().split()
        n = int(nt_strs[0])
        t = int(nt_strs[1])

        shares = Shamir.split(t, n, secret_bytes)

        print('\nSplitted secret:')
        for idx, share in shares:
            print("Part {}: 0x{}".format(idx, share.hex()))

    elif(arg == 'recover'):
        shares = []
        fl = True
        print('\nInput idx and part of secret separated by ":" (or press enter to exit):')
        while fl:
            part_str = input()
            if len(part_str) != 0:
                idx, share = [ s.strip() for s in part_str.split(":") ]
                #part_int = int(share, 16)
                inner_share = share[2:]

                part_bytes = inner_share
                #part_bytes = binascii.unhexlify(inner_share)

                shares.append([int(idx), binascii.unhexlify(part_bytes)])
            else:
                fl = False

        print('\nRecovered secret:')
        key = Shamir.combine(shares)
        print('0x{}'.format(key.hex()))
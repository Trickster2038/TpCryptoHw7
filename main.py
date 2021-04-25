import sys
from Crypto.Protocol.SecretSharing import Shamir
import secretgen
from Crypto.Random import get_random_bytes
import binascii
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
        secret_str = input()
        # secret_str = "0x3454078a54a22d0c97db7f294b376278"

        #secret_int = int(secret_str, 16)
        secret_bytes = bytes.fromhex(secret_str[2:])

        print('\nInput N T (N >= T):')
        nt_strs = input().split()
        #nt_strs = "10 3"
        n = int(nt_strs[0])
        t = int(nt_strs[1])

        # exam = get_random_bytes(16)
        shares = Shamir.split(t, n, secret_bytes)

        print('\nSplitted secret:')
        for idx, share in shares:
            print("Part {}: 0x{}".format(idx, share.hex()))

    elif(arg == 'recover'):
        # shares = [[1, "2bae6ed5ba407223348226a4e1e58a42"],[2, "fa7b3591a728f18d870c2939bc3a2f91"]]
        shares = []
        fl = True
        print('\nInput idx and share separated by ":" (or press enter to exit):')
        while fl:
            part_str = input()
            if len(part_str) != 0:
                idx, share = [ s.strip() for s in part_str.split(":") ]
                #part_int = int(share, 16)
                inner_share = share[2:]

                part_bytes = inner_share
                #part_bytes = binascii.unhexlify(inner_share)

                shares.append([int(idx), part_bytes])
            else:
                fl = False

        #shares = [[1, "2bae6ed5ba407223348226a4e1e58a42"],[2, "fa7b3591a728f18d870c2939bc3a2f91"]]
        print(shares)
        bin_shares = [] 

        for share in shares:
            bin_shares.append((share[0], binascii.unhexlify(share[1])))

        for idx, share in shares:
            print("Part {}: 0x{}".format(idx, share))

        for idx, share in bin_shares:
            print("Part {}: 0x{}".format(idx, share))

        for idx, share in bin_shares:
            print("Part {}: 0x{}".format(idx, share.hex()))

        key = Shamir.combine(bin_shares)
        print('0x{}'.format(key.hex()))
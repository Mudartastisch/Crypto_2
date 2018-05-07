"""
sha1 brute force password recovery
"""
import hashlib
import os

from sys import argv
from itertools import product
from string import ascii_lowercase

def bruteforce(hash_, charset, min_length, max_length, algo, debug):
    for length in range(int(min_length), int(max_length) + 1):
        for attempt in product(charset, repeat=length):
            to_hash = "".join(attempt).encode("utf-8")
            to_hash = algo(to_hash).hexdigest()

            if to_hash != hash_:
                if debug:
                    print("Hash: "+hash_+" Attempt: "+''.join(attempt)+" "+to_hash)
            else:
                if debug:
                    print("Success! password: "+''.join(attempt))
                return "".join(attempt)

def main():
    hash_file = argv[1]
    script_dir = os.path.dirname(__file__)
    rel_path = hash_file
    abs_file_path = os.path.join(script_dir, rel_path)
    hash_list = []
    pwfile = open(abs_file_path)
    while True:
        line = pwfile.readline()
        hash_list.append(line.rstrip('\n'))
        if not line:
            break
    pwfile.close()
    result_list = []
    charset = ascii_lowercase
    min_length_ = 6
    max_length_ = 6
    algo = hashlib.sha1
    debug_ = True
    for i in range(len(hash_list)):
        res = bruteforce(hash_list[i], charset, min_length_, max_length_, algo, debug_)
        if res is None:
            print("\n")
        else:
            result_list.append(res)
    for i in range(len(result_list)):
        print(str(i+1)+". "+"".join(result_list[i]))

if __name__ == "__main__":
    print("\n"*90)
    main()

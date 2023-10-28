import hashlib
import sys

BLOCK_SIZE = 1024

def find_groups(filenames):
    groups = {}
    for item in filenames:
        hash_code = None
        with open(item, "rb") as fp:
            chunk = fp.read(BLOCK_SIZE)
            if not chunk:
                break
            if hash_code == None:
                hash_code = hashlib.sha256(chunk)
            else:
                hash_code = hash_code.update(chunk)

        hash_code = hash_code.hexdigest()
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(item)
    return groups

if __name__ == '__main__':
    groups = find_groups(sys.argv[1:])
    for filenames in groups.values():
       print(", ".join(sorted(filenames)))

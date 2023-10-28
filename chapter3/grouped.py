from naive_hash import naive_hash
from brute_force_1 import find_duplicates
import sys
def find_groups(filenames):
    groups = {}
    for item in filenames:
        data = open(item, "rb").read()
        hash_code = naive_hash(data)
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(item)
    return groups

if __name__ == '__main__':
    groups = find_groups(sys.argv[1:])
    for files in groups.values():
        duplicates = find_duplicates(list(files))
        for (left, right) in duplicates:
            print(left, right)

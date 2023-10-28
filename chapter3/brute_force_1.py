import sys

def same_bytes(filename1, filename2):
    bytes1 = open(filename1, "rb").read()
    bytes2 = open(filename2, "rb").read()
    return bytes1 == bytes2

def find_duplicates(filenames):
    matches = []
    for left in range(len(filenames)):
        for right in range(left):
            if  same_bytes(filenames[left], filenames[right]):
                matches.append((filenames[left], filenames[right]))
    return matches

if __name__ == '__main__':
    duplicates = find_duplicates(sys.argv[1:])
    for (left, right) in duplicates:
        print(left, right)

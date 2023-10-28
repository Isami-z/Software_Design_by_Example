import hashlib
example = bytes("hashing", "utf-8")

for i in range(1, len(example) + 1):
    substring = example[:i]
    _hash = hashlib.sha256(substring).hexdigest()
    print(f"{_hash:2}, {substring}")

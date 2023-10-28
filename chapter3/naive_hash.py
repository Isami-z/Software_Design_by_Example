example = bytes("hashing", "utf-8")

def naive_hash(data):
    return sum(data) % 13

# for i in range(1, len(example) + 1):
#     substring = example[:i]
#     _hash = naive_hash(substring)
#     print(f"{_hash:2}, {substring}")

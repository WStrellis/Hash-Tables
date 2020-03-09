import hashlib

n = 10
key = b'cat'
key2 = 'dog'.encode()
# for i in range(n):
#     print(hash(key))
#     print(hashlib.sha256(key).hexdigest())

# breakpoint()

n = 1
key3 = b'noodles'
# '8' represents storing  8 values
index = hash(key) % 8
index2 = hash(key2) % 8
index3 = hash(key3) % 8
print(index)
print(index2)
print(index3)

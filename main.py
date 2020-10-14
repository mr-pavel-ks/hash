import hashlib
def my_gererator(name):
    with open(name, encoding='utf-8') as f:
        for line in f:
            yield line

generator = my_gererator('file.txt')
for item in generator:
    hash = hashlib.md5(item.encode('utf-8')).hexdigest()
    print(hash)

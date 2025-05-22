

table = [None] * 26

def hash(key):
    # return len(key)
    return ord(key[0]) - 97

def put(key, value):
    index = hash(key)
    if not table[index]:
        table[index] = []
    table[index].append((key, value))

def get(key):
    # return table[hash(key)]
    vals = table[hash(key)]
    for val in vals:
        if val[0] == key:
            return val

put("onion", 3.24)
put("tomato", 3.99)
put("red pepper", 5.99)
put('taro', 6.00)

print(table)

print(f'onions are ${get('onion')}')


table = [None] * 26

def hash(key):
    # return len(key)
    return ord(key[0]) - 97

def put(key, value):
    index = hash(key)
    if table[index] is None:
        table[index] = (key, value)
    index = index + 1
    while table[index] is not None:
        index = index + 1
    table[index] = (key, value)



def get(key):
    # return table[hash(key)]
    index = hash(key)
    vals = table[index]

    if vals[0] == key:
        return vals
    index = index - 1
    while index < len(table):
        if table[index][0] == key:
            return table[index]
        index = index + 1

    return None


put("onion", 3.24)
put("tomato", 3.99)
put("red pepper", 5.99)
put('taro', 6.00)

print(table)

print(f'onions are ${get('onion')}')
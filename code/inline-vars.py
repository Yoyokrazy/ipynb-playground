a = {'value': 5}

def local_fn():
    a = 20

    b = 10
    c = a + b

    return c

result = local_fn()

a['pie'] = 3.14

test = 'hello'

print(a)

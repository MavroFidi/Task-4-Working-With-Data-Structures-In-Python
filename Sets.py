def union(x,y):
    result = []
    result = set(result)
    for i in x:
      result.add(i)
    for j in y:
      result.add(j)
    return result

def intersect(x,y):
    result = []
    result = set(result)
    for i in x:
        for j in y:
            if i == j:
                result.add(i)
    return result

def diff(x,y):
    result = []
    result = set(result)
    for i in x:
        if i not in y:
            result.add(i)
    return result

def symdiff(x,y):
    result = []
    result = set(result)
    for i in x:
        if i not in y:
            result.add(i)
    for j in y:
        if j not in x:
            result.add(j)
    return result

E = {0,2,4,6,8}
N = {1,2,3,4,5}

print(union(E,N))
print(intersect(E,N))
print(diff(E,N))
print(symdiff(E,N))

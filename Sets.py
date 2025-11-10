def union(x,y):
  result = {}
  for i in x:
    result.add(i)
  for j in y:
    result.add(j)

def intersect(x,y):
  result = {}
  for i in x:
    for j in y:
      if i == j:
        result.add(i)

def diff(x,y):
  result = {}
  for i in y:
    for j in x:
      if i != j:
        result.add(j)

def symdiff(x,y):
  result = {}
  for i in x:
    for j in y:
      result.add(i)
      result.add(j)

E = {0,2,4,6,8}
N = {1,2,3,4,5}

print(union(E,N))
print(intersect(E,N))
print(diff(E,N))
print(symdiff(E,N))

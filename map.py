#map(function, iterables)

def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry')) 
print(list(x))


frutas = ['apple', 'banana', 'cherry']

x = map(lambda y: len(y), frutas)
print(list(x))
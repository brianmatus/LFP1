import numpy
n = int(input())
lines = []
for i in range (0,n):
    _arr = map(float, input().split(" "))
    arr = []
    for a in _arr:
        _a = [a]
        arr = arr + _a
    lines = lines + [arr]
print(round(numpy.linalg.det(lines),2))

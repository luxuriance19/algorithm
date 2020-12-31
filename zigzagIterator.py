from typing import Iterator, List
import itertools

#281
class ZigzagIterator:
    def __init__(self, v1:List[int], v2:List[int]):
        self.v1 = v1
        self.v2 = v2
        self.v = (v[i] for i in itertools.count() for v in (v1, v2) if i < len(v))  #generator
        self.n = len(v1) + len(v2)

    def next(self):
        self.n -= 1
        return next(self.v) 

    def hasNext(self):
        return self.n > 0

##
v1 = [1,2]; v2=[3,4,5]
nexti, v = ZigzagIterator(v1, v2), []
while nexti.hasNext():
    v.append(nexti.next())
print(v)

### 251 flatten 2D Vector
class Vector2D:
    def __init__(self, vec2d:List[List[int]]):
        self.vec2d = vec2d
        self.x = 0
        self.y = 0
        self.vec2d_len = len(self.vec2d)

    def next(self):
        ret_val = self.vec2d[self.x][self.y]
        self.y += 1
        return ret_val

    def hasNext(self):
        while self.x < self.vec2d_len and self.y == len(self.vec2d[self.x]):
            self.x += 1
            self.y = 0
        if self.x < self.vec2d_len and self.y < len(self.vec2d[self.x]):
            return True
        return False

vec2d = [[1,2],[3],[],[4,5,6]]
nexti= Vector2D(vec2d=vec2d)
v = []
while nexti.hasNext():
    v.append(nexti.next())
print(v)

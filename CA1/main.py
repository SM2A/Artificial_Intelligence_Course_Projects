import enum


class Cell(enum.Enum):
    empty = 0
    wall = 1
    potion = 2
    double = 3
    start = 4
    end = 5


file = open('test1.in')
n, m = file.readline().split()
c, k = file.readline().split()

temple = [[Cell.empty for x in range(int(m))] for y in range(int(n))]

for i in range(int(c)):
    x, y = file.readline().split()
    temple[int(x)][int(y)] = Cell.potion

for i in range(int(k)):
    x, y = file.readline().split()
    temple[int(x)][int(y)] = Cell.double

d = file.readline()

for i in range(int(d)):
    x, y = file.readline().split()
    temple[int(x)][int(y)] = Cell.wall

import enum


class Cell(enum.Enum):
    empty = 0
    wall = 1
    potion = 2
    double = 3
    start = 4
    end = 5


temple = []
source = [(0, 0)]
move = ((1, 0), (-1, 0), (0, 1), (0, -1))


def bfs(s):
    visited = [s]
    queue = [s]
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for adj in move:
            x = node[0] + adj[0]
            y = node[1] + adj[1]
            if x >= int(n) or x < 0 or y >= int(m) or y < 0:
                continue
            if temple[x][y] == Cell.wall:
                continue
            if (x, y) not in visited:
                visited.append((x, y))
                queue.append((x, y))
                if temple[x][y] == Cell.end:
                    print((x, y), end=" ")
                    return
                if temple[x][y] == Cell.potion:
                    temple[x][y] = Cell.empty
                if temple[x][y] == Cell.double:
                    xd = x - 1
                    yd = y - 1
                    if (temple[xd][yd] == Cell.wall) or (xd >= int(n) or xd < 0 or yd >= int(m) or yd < 0):
                        source.append((0, 0))
                    else:
                        source.append((xd, yd))

                    temple[x][y] = Cell.empty


if __name__ == '__main__':
    file = open('test1.in')
    n, m = file.readline().split()
    c, k = file.readline().split()

    temple = [[Cell.empty for x in range(int(n))] for y in range(int(m))]

    temple[0][0] = Cell.start
    temple[int(n) - 1][int(m) - 1] = Cell.end

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

    for start in source:
        bfs(start)
        print()

import enum
import time


class Cell(enum.Enum):
    empty = 0
    wall = 1
    potion = 2
    double = 3
    start = 4
    end = 5


temple = []
spells = []
final_path = []
source = [(0, 0)]
move = ((1, 0), (0, 1), (-1, 0), (0, -1))


# def bfs(s):
#     visited = []
#     queue = [[s]]
#     global spells
#     while queue:
#         path = queue.pop(0)
#         node = path[-1]
#         if node not in visited:
#             for adj in move:
#                 x = node[0] + adj[0]
#                 y = node[1] + adj[1]
#                 if x >= int(n) or x < 0 or y >= int(m) or y < 0:
#                     continue
#                 if temple[x][y] == Cell.wall:
#                     continue
#                 if (x, y) not in visited:
#                     new_path = list(path)
#                     new_path.append((x, y))
#                     queue.append(new_path)
#                     print(new_path)
#                     if temple[x][y] == Cell.end:
#                         print(set(spells).issubset(set(new_path)))
#                         print(new_path, end=f" len : {len(new_path)}\n")
#                         return
#                     if temple[x][y] == Cell.potion:
#                         temple[x][y] = Cell.empty
#                     if temple[x][y] == Cell.double:
#                         temple[x][y] = Cell.empty
#                         source.append((int(m) - 1, 0))
#             visited.append(node)


def bfs(s):
    visited = []
    queue = [[s]]
    global spells, x, y
    while queue:
        path = queue.pop(0)
        node = path[-1]
        for adj in move:
            x = node[0] + adj[0]
            y = node[1] + adj[1]
            if x >= int(n) or x < 0 or y >= int(m) or y < 0:
                continue
            if temple[x][y] == Cell.wall:
                continue
            if (node, (x, y)) not in visited:
                new_path = list(path)
                new_path.append((x, y))
                queue.append(new_path)
                if temple[x][y] == Cell.end and set(spells).issubset(set(new_path)):
                    print(new_path, end=f" len : {len(new_path)}\n")
                    spells = []
                    return
                if temple[x][y] == Cell.potion:
                    temple[x][y] = Cell.empty
                if temple[x][y] == Cell.double:
                    temple[x][y] = Cell.empty
                    source.append((int(m) - 1, 0))
        visited.append((node, (x, y)))


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
        spells.append((int(x), int(y)))

    for i in range(int(k)):
        x, y = file.readline().split()
        temple[int(x)][int(y)] = Cell.double

    d = file.readline()

    for i in range(int(d)):
        x, y = file.readline().split()
        temple[int(x)][int(y)] = Cell.wall

    doc = 1
    begin = time.time()
    for start in source:
        print(doc, end=" : ")
        bfs(start)
        doc += 1

    print(f"Executed in {time.time() - begin} seconds")

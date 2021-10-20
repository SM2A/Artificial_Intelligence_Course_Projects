import enum
import time
import copy


class Cell(enum.Enum):
    empty = 0
    wall = 1
    potion = 2
    double = 3
    start = 4
    end = 5


temple = []


class doctor:
    def __init__(self, id, x, y):
        self.id = id
        self.path = [(x, y)]

    def get_path(self):
        return self.path

    def get_position(self):
        return self.path[-1]

    def add_dest(self, x, y):
        self.path[-1][0] += x
        self.path[-1][1] += y

    def __hash__(self):
        return f"{self.id} : {self.path}"

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


class state:
    def __init__(self, doubles, potions, doctors, x, y):
        self.doubles = doubles
        self.potions = potions
        self.doctors = doctors
        self.x = x
        self.y = y

    def get_path(self):
        path = []
        for doc in self.doctors:
            for pos in doc:
                path.append(pos)
        return path

    def is_done(self):
        done = True
        if len(self.potions) != 0:
            return False
        for doc in self.doctors:
            if doc.path[-1][-1] != (x, y):
                return False
        return done

    def __str__(self):
        result = ""
        result += str(self.doubles)
        result += " "
        result += str(self.potions)
        result += " "
        for doc in self.doctors:
            result += (doc.__hash__() + " ")
        return result

    def __hash__(self):
        result = ""
        result += str(self.doubles)
        result += " "
        result += str(self.potions)
        result += " "
        for doc in self.doctors:
            result += (doc.__hash__() + " ")
        return result.__hash__()

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


move = ((1, 0), (0, 1), (-1, 0), (0, -1))


def next_state(frontier, visited):
    ns = []
    for i in range(len(frontier)):
        for j in range(len(frontier[i].doctors)):
            for adj in move:
                new_s = copy.deepcopy(frontier[i])
                pos = new_s.doctors[j].path[-1]
                new_pos = (pos[0] + adj[0], pos[1] + adj[1])
                new_s.doctors[j].path.append(new_pos)
                if new_pos[0] >= int(new_s.y) or new_pos[0] < 0 or new_pos[1] >= int(new_s.x) or new_pos[1] < 0:
                    continue
                elif temple[new_pos[0]][new_pos[1]] == Cell.wall:
                    continue
                if (j, pos, new_pos) not in visited:
                    ns.append(new_s)
                    visited.add((j, pos, new_pos))
    return ns


def bfs(initial):
    visited = set()
    queue = [initial]
    while queue:
        queue = next_state(queue, visited)
        for f in queue:
            print(f.__str__())
            for doc in f.doctors:
                x = doc.path[-1][0]
                y = doc.path[-1][1]
                if temple[x][y] == Cell.potion and (x, y) in f.potions:
                    f.potions.remove((x, y))
                if temple[x][y] == Cell.double and (x, y) in f.doubles:
                    new_doc = doctor(len(f.doctors) + 1, int(f.x) - 1, 0)
                    f.doctors.append(new_doc)
                    f.doubles.remove((x, y))
                if f.is_done():
                    return f


if __name__ == '__main__':

    file = open('test1.in')
    n, m = file.readline().split()
    c, k = file.readline().split()

    temple = [[Cell.empty for x in range(int(n))] for y in range(int(m))]

    temple[0][0] = Cell.start
    temple[int(n) - 1][int(m) - 1] = Cell.end

    potion = []
    for i in range(int(c)):
        x, y = file.readline().split()
        temple[int(x)][int(y)] = Cell.potion
        potion.append((int(x), int(y)))

    double = []
    for i in range(int(k)):
        x, y = file.readline().split()
        temple[int(x)][int(y)] = Cell.double
        double.append((int(x), int(y)))

    d = file.readline()

    for i in range(int(d)):
        x, y = file.readline().split()
        temple[int(x)][int(y)] = Cell.wall

    doc = doctor(1, 0, 0)
    initial_state = state(double, potion, [doc], int(n) - 1, int(m) - 1)
    begin = time.time()
    result = bfs(initial_state)
    print(result.__str__())
    print(f"Executed in {time.time() - begin} seconds")

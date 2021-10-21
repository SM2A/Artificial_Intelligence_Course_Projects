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
m, n = 0, 0


class State:
    def __init__(self, doubles, potions, doctors, parent):
        self.doubles = doubles
        self.potions = potions
        self.doctors = doctors
        self.parent = parent

    def print_path(self):
        doc = [[] for x in range(int(len(self.doctors)))]
        current = self
        while current is not None:
            for i in range(len(current.doctors)):
                if len(doc[i]) == 0:
                    doc[i].append(current.doctors[i])
                elif current.doctors[i] != doc[i][-1]:
                    doc[i].append(current.doctors[i])
            current = current.parent
        result = ""
        for index in range(len(doc)):
            doc[index].reverse()
            result += f"Doctor {index + 1} : {doc[index]} Length = {len(doc[index]) - 1}\n"
        return result

    def is_done(self):
        done = True
        if len(self.potions) != 0:
            return False
        for doc in self.doctors:
            if doc != (int(n) - 1, int(m) - 1):
                return False
        return done

    def __str__(self):
        result = ""
        result += str(self.doubles)
        result += " "
        result += str(self.potions)
        result += " "
        for i in range(len(self.doctors)):
            result += f"{i} : {self.doctors[i]} "
        return result

    def __hash__(self):
        return self.__str__().__hash__()

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


move = ((1, 0), (0, 1), (-1, 0), (0, -1))


def next_state(frontier, visited):
    ns = []
    for i in range(len(frontier)):
        for j in range(len(frontier[i].doctors)):
            for adj in move:
                pos = frontier[i].doctors[j]
                new_pos = (pos[0] + adj[0], pos[1] + adj[1])
                if pos == (int(n) - 1, int(m) - 1):
                    continue
                if new_pos[0] >= int(n) or new_pos[0] < 0 or new_pos[1] >= int(m) or new_pos[1] < 0:
                    continue
                if temple[new_pos[0]][new_pos[1]] == Cell.wall:
                    continue
                new_doubles = list(frontier[i].doubles)
                new_potions = list(frontier[i].potions)
                new_doctors = list(frontier[i].doctors)
                new_doctors[j] = new_pos
                new_s = State(new_doubles, new_potions, new_doctors, frontier[i])
                new_s.doctors[j] = new_pos
                new_s.parent = frontier[i]
                if new_s not in visited:
                    ns.append(new_s)
                    visited.add(new_s)

    return ns


def bfs(initial):
    visited = set()
    queue = [initial]
    while queue:
        for f in queue:
            for doc in f.doctors:
                x, y = doc
                if temple[x][y] == Cell.potion and (x, y) in f.potions:
                    f.potions.remove((x, y))
                elif temple[x][y] == Cell.double and (x, y) in f.doubles:
                    f.doctors.append((int(n) - 1, 0))
                    f.doubles.remove((x, y))
                if f.is_done():
                    return f
        queue = next_state(queue, visited)


result = []
test_time = []
for test in 1, 2, 3:
    test_time.append([])
    for r in 1, 2, 3:
        file = open(f'Tests/test{test}.in')
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

        initial_state = State(double, potion, [(0, 0)], None)
        begin = time.time()
        res = bfs(initial_state)
        test_time[test - 1].append(time.time() - begin)
        if len(result) == test - 1:
            result.append(res)
    print(f"Average execution time of test{test}.in is : {sum(test_time[test - 1]) / len(test_time[test - 1])} seconds")
    print("Optimal path is :")
    print(result[test - 1].print_path())

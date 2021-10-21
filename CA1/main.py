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
m, n = 0, 0


# class doctor:
#     def __init__(self, id, x, y):
#         self.id = id
#         self.position = (x, y)
#
#     def get_position(self):
#         return self.position
#
#     def __str__(self):
#         return f"{self.id} : {self.position}"
#
#     def __hash__(self):
#         return f"{self.id} : {self.position}".__hash__()
#
#     def __eq__(self, other):
#         return self.__hash__() == other.__hash__()


class state:
    def __init__(self, doubles, potions, doctors, parent):
        self.doubles = doubles
        self.potions = potions
        self.doctors = doctors
        self.parent = parent

    def print_path(self):
        result = "Drugs : "
        result += str(self.doubles)
        result += " | Potions "
        result += str(self.potions)
        result += "\nDoctors : "
        current = self
        while current is not None:
            result += "\n"
            for i in range(len(current.doctors)):
                result += f"{i} : {current.doctors[i]} "
            result += f" # STR : {current.__str__()} # HASH : {current.__hash__()}"
            current = current.parent
        return result

    def is_done(self):
        done = True
        if len(self.potions) != 0:
            return False
        for doc in self.doctors:
            if doc != (int(n)-1, int(m)-1):
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

                # if frontier[i].doctors[0] == (int(n) - 1, int(m) - 1) and len(frontier[i].doctors) == 2:
                #     print(frontier[i].print_path())
                # if len(frontier[i].doctors) == 2 and len(frontier[i].potions) == 0:
                #     if frontier[i].doctors[-1] == (int(n) - 1, int(m) - 1) and frontier[i].doctors[-2] == (int(n) - 1, int(m) - 1):
                #         print(f"{frontier[i].is_done()} $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                #         print(frontier[i].print_path())
                if pos == (int(n) - 1, int(m) - 1):
                    continue
                if new_pos[0] >= int(n) or new_pos[0] < 0 or new_pos[1] >= int(m) or new_pos[1] < 0:
                    continue
                if temple[new_pos[0]][new_pos[1]] == Cell.wall:
                    continue

                new_s = copy.deepcopy(frontier[i])
                # dd = list(frontier[i].doubles)
                # pp = list(frontier[i].potions)
                # ddd = list(frontier[i].doctors)
                # ddd[j] = new_pos
                # new_s = state(dd, pp, ddd, frontier[i])
                new_s.doctors[j] = new_pos
                new_s.parent = frontier[i]
                # strr = new_s.__hash__()

                # is_in_v = False
                # for kk in visited:
                #     if  kk.doctors == new_s.doctors and kk.parent.doctors == new_s.parent.doctors:
                #         is_in_v = True
                #         break

                if new_s not in visited:
                    ns.append(new_s)
                    # visited.append(new_s.__str__())
                    # print(new_s.__hash__())
                    # print(new_s.__str__())
                    visited.add(new_s)
                    # visited = sorted(visited)
                # print(new_s not in visited)
                # print(frontier[i] in visited)
    return ns


def bfs(initial):
    visited = set()
    queue = [initial]
    level = 0
    while queue:
        queue = next_state(queue, visited)
        print(f"level {level} ----------------------------------------------------------------------------------------")
        # if level == 14:
        #     visited = sorted(visited)
        #     print("ok")
        #     print("asd")
        # print(ssss)
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
            # print(f.print_path())
        level += 1


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

    initial_state = state(double, potion, [(0, 0)], None)
    # one = state(double, potion, [(0, 0)], None)
    # two = state(double, potion, [(0, 0)], initial_state)
    # three = state(double, potion, [(0, 0)], two)
    # print(initial_state == one)
    # print(initial_state == two)
    # print(initial_state == three)
    # print(two == one)
    # print(three == one)
    # print(three == two)
    begin = time.time()
    result = bfs(initial_state)
    print(result.print_path())
    print(f"Executed in {time.time() - begin} seconds")

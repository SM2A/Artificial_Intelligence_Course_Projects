import random
import copy

N = 9


def read_table(name):
    f = open(name)
    content = f.read()
    f.close()

    board = content.split('\n')
    table = []

    for row in board:
        row = row.split(' ')
        ll = []
        for column in row:
            ll.append(int(column))
        table.append(ll)

    return table


def print_board(sudoku_board):
    for i in sudoku_board:
        print(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])


def population_init(board, size):
    return [random_board(board) for _ in range(size)]


def random_board(board):
    table = copy.deepcopy(board)
    for i in range(9):
        possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if table[i][j] == 0:
                found = False
                while not found:
                    choice = random.choice(possible_numbers)
                    if choice not in table[i]:
                        table[i][j] = choice
                        possible_numbers.remove(choice)
                        found = True
                    else:
                        possible_numbers.remove(choice)
    return table


# todo fix this function
def selection(population, fitness_population, size):
    sorted_population = sorted(zip(population, fitness_population), key=lambda ind_fit: ind_fit[1])
    return [individual for individual, fitness in sorted_population[int(size * 0.2):]]


def crossover(population, size):
    a = []
    for i in range(size):
        a.append(_crossover_(random.choice(population), random.choice(population)))
    return a


def _crossover_(parent1, parent2):
    a = []
    for child_pair in zip(parent1, parent2):
        a.append(list(random.choice(child_pair)))
    return a


def mutation(population, board):
    return [_mutation_(individual, board) for individual in population]


def _mutation_(individual, board):
    for i in range(9):
        if random.random() < 0.1:
            flag = False
            while not flag:
                rand1 = random.randint(0, 8)
                rand2 = random.randint(0, 8)
                if board[i][rand1] == 0 and board[i][rand2] == 0:
                    individual[i][rand1], individual[i][rand2] = individual[i][rand2], individual[i][rand1]
                    flag = True
    return list(individual)


def check_inference(board, i, j):
    if (board[i][j] in board[:i]) or (board[i][j] in board[i + 1:]):
        return True

    for index in range(N):
        if index == i:
            continue
        if board[index][j] == board[i][j]:
            return True

    row_range = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    column_range = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    rr = []
    cr = []

    for row in row_range:
        if i in row:
            rr = row
            break

    for column in column_range:
        if j in column:
            cr = column
            break

    for row in rr:
        for column in cr:
            if row == i and column == j:
                continue
            if board[i][j] == board[row][column]:
                return True

    return False


def fitness_scale(population):
    fitness_ = []
    for board in population:
        fitness = 0
        for i in range(N):
            for j in range(N):
                if not check_inference(board, i, j):
                    fitness += 1

        if fitness == N ** 2:
            print_board(board)
            exit(0)
        fitness_.append(fitness)

    return fitness_


if __name__ == "__main__":
    board = read_table("Test\Test2.txt")

    population_size = 200
    iteration = 0

    population = population_init(board, population_size)
    population_fitness = fitness_scale(population)

    while iteration < 1000:
        iteration += 1
        parents = selection(population, population_fitness, population_size)
        child = crossover(parents, population_size)
        population = mutation(child, board)
        population_fitness = fitness_scale(population)

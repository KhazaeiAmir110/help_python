import numpy as np


def calculate_path_length(path, distance_matrix):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i], path[i + 1]]
    total_distance += distance_matrix[path[-1], path[0]]
    return total_distance


def antlion_optimizer_tsp(distance_matrix, num_cities, max_iter, num_agents):
    ants = [np.random.permutation(num_cities) for _ in range(num_agents)]
    antlions = [np.random.permutation(num_cities) for _ in range(num_agents)]

    best_antlion = min(antlions, key=lambda al: calculate_path_length(al, distance_matrix))
    best_length = calculate_path_length(best_antlion, distance_matrix)

    for t in range(max_iter):
        for i in range(num_agents):
            random_walk = np.random.permutation(num_cities)
            new_path = ants[i].copy()

            for j in range(num_cities):
                new_path[j] = random_walk[j]

            ants[i] = np.unique(new_path, return_index=False)

        for i in range(num_agents):
            if calculate_path_length(ants[i], distance_matrix) < calculate_path_length(antlions[i], distance_matrix):
                antlions[i] = ants[i].copy()

        best_antlion = min(antlions, key=lambda al: calculate_path_length(al, distance_matrix))
        best_length = calculate_path_length(best_antlion, distance_matrix)

    return best_antlion, best_length


def create_random_distance_matrix(num_cities, max_distance=100):
    matrix = np.random.randint(1, max_distance, size=(num_cities, num_cities))
    np.fill_diagonal(matrix, 0)
    return (matrix + matrix.T) // 2


num_cities = 10
max_iter = 100
num_agents = 30

distance_matrix = create_random_distance_matrix(num_cities)

best_path, best_path_length = antlion_optimizer_tsp(distance_matrix, num_cities, max_iter, num_agents)
print(distance_matrix)
print("Best Path:", best_path)
print("Best Path Length:", best_path_length)

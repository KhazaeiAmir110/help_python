import numpy as np


def calculate_path_length(path, distance_matrix):
    """Calculate the total distance of the TSP path."""
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i], path[i + 1]]
    total_distance += distance_matrix[path[-1], path[0]]
    return total_distance


def random_walk_with_bounds(antlion, num_cities):
    """Perform a random walk influenced by the antlion."""
    random_walk = np.random.permutation(num_cities)
    combined = np.concatenate((antlion, random_walk))
    _, unique_indices = np.unique(combined, return_index=True)
    return combined[np.sort(unique_indices)][:num_cities]


def antlion_optimizer_tsp(distance_matrix, num_cities, max_iter, num_agents):
    """Ant Lion Optimizer for solving the TSP problem."""
    ants = [np.random.permutation(num_cities) for _ in range(num_agents)]
    antlions = [np.random.permutation(num_cities) for _ in range(num_agents)]

    elite_antlion = min(antlions, key=lambda al: calculate_path_length(al, distance_matrix))
    elite_length = calculate_path_length(elite_antlion, distance_matrix)

    for t in range(max_iter):
        for i in range(num_agents):
            ants[i] = random_walk_with_bounds(antlions[i], num_cities)

            if calculate_path_length(ants[i], distance_matrix) < calculate_path_length(antlions[i], distance_matrix):
                antlions[i] = ants[i].copy()

        current_best_antlion = min(antlions, key=lambda al: calculate_path_length(al, distance_matrix))
        current_best_length = calculate_path_length(current_best_antlion, distance_matrix)

        if current_best_length < elite_length:
            elite_antlion = current_best_antlion.copy()
            elite_length = current_best_length

    return elite_antlion, elite_length


def create_random_distance_matrix(num_cities, max_distance=100):
    """Generate a symmetric random distance matrix."""
    matrix = np.random.randint(1, max_distance, size=(num_cities, num_cities))
    np.fill_diagonal(matrix, 0)
    return (matrix + matrix.T) // 2


num_cities = 10
max_iter = 100
num_agents = 30

distance_matrix = create_random_distance_matrix(num_cities)

best_path, best_path_length = antlion_optimizer_tsp(distance_matrix, num_cities, max_iter, num_agents)

print("Distance Matrix:")
print(distance_matrix)
print("Best Path:", best_path)
print("Best Path Length:", best_path_length)

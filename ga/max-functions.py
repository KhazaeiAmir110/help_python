import numpy as np

POP_SIZE = 10
GENS = 100
MUTATION_RATE = 0.1
X_MIN, X_MAX = 0, 10


def fitness(x):
    return x * np.sin(x)


population = np.random.uniform(X_MIN, X_MAX, POP_SIZE)

for generation in range(GENS):
    scores = fitness(population)
    parents = population[np.argsort(scores)][-2:]
    offspring = []
    for _ in range(POP_SIZE):
        parent1, parent2 = np.random.choice(parents, 2)
        child = (parent1 + parent2) / 2

        if np.random.rand() < MUTATION_RATE:
            child += np.random.uniform(-1, 1)

        offspring.append(child)

    population = np.clip(offspring, X_MIN, X_MAX)

best_solution = population[np.argmax(fitness(population))]
print("Best solution:", best_solution)
print("Max value:", fitness(best_solution))

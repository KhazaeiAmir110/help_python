import numpy as np

# تنظیمات الگوریتم ژنتیک
POP_SIZE = 10  # اندازه جمعیت
GENS = 100  # تعداد نسل‌ها
MUTATION_RATE = 0.1  # نرخ جهش
X_MIN, X_MAX = 0, 10  # بازه تابع


# تابع هدف: x * sin(x)
def fitness(x):
    return x * np.sin(x)


# تولید جمعیت اولیه
population = np.random.uniform(X_MIN, X_MAX, POP_SIZE)

for generation in range(GENS):
    # ارزیابی تابع هدف برای هر فرد
    scores = fitness(population)

    # انتخاب والدین (ساده‌ترین روش انتخاب بهترین‌ها)
    parents = population[np.argsort(scores)][-2:]

    # تولید نسل جدید با ترکیب والدین
    offspring = []
    for _ in range(POP_SIZE):
        # ترکیب تصادفی دو والدین
        parent1, parent2 = np.random.choice(parents, 2)
        child = (parent1 + parent2) / 2  # تقاطع به‌صورت میانگین والدین

        # اعمال جهش
        if np.random.rand() < MUTATION_RATE:
            child += np.random.uniform(-1, 1)

        # اضافه کردن فرزند به نسل جدید
        offspring.append(child)

    population = np.clip(offspring, X_MIN, X_MAX)  # محدود کردن به بازه

# پیدا کردن بهترین جواب
best_solution = population[np.argmax(fitness(population))]
print("Best solution:", best_solution)
print("Max value:", fitness(best_solution))
# -----------------------------------------------------------------------
import numpy as np
import random

# Define the function to maximize
def fitness_function(x):
    return x * x  # Example: f(x) = -x^2 + 10x

# Parameters
population_size = 10
num_generations = 100
mutation_rate = 0.1
interval = (0, 10)  # Search interval [0, 10]

# Initialize the population
def initialize_population(size, interval):
    return [random.uniform(*interval) for _ in range(size)]

# Select parents based on fitness
def select_parents(population):
    fitness_values = [fitness_function(x) for x in population]
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]
    return np.random.choice(population, size=len(population), p=probabilities)

# Crossover to create offspring
def crossover(parent1, parent2):
    return (parent1 + parent2) / 2  # Simple average crossover

# Mutation function
def mutate(individual, interval):
    if random.random() < mutation_rate:
        return random.uniform(*interval)
    return individual

# Main genetic algorithm function
def genetic_algorithm():
    population = initialize_population(population_size, interval)

    for generation in range(num_generations):
        parents = select_parents(population)
        offspring = []

        # Ensure pairs are created correctly
        for i in range(0, len(parents) - 1, 2):
            child = crossover(parents[i], parents[i + 1])
            child = mutate(child, interval)
            offspring.append(child)

        # If population size is odd, add one remaining parent to the offspring
        if len(parents) % 2 == 1:
            offspring.append(mutate(parents[-1], interval))

        population = offspring  # Replace population with offspring

    # Return the best solution
    best_individual = max(population, key=fitness_function)
    return best_individual, fitness_function(best_individual)

# Run the genetic algorithm
best_solution, best_value = genetic_algorithm()
print(f"Best solution: x = {best_solution}, f(x) = {best_value}")


import random

# آیتم‌های مسئله کوله‌پشتی
items = [
    {"value": 10, "weight": 5},
    {"value": 15, "weight": 7},
    {"value": 25, "weight": 10},
    {"value": 30, "weight": 12},
    {"value": 50, "weight": 20}
]

# ظرفیت کوله‌پشتی
knapsack_capacity = 25

# اندازه جمعیت
population_size = 10

# احتمال جهش
mutation_rate = 0.1

# تعداد نسل‌ها
generations = 100


# تولید یک کروموزوم جدید (بردار باینری)
def generate_chromosome():
    return [random.randint(0, 1) for _ in range(len(items))]


# محاسبه برازندگی (fitness) یک کروموزوم
def fitness(chromosome):
    total_value = 0
    total_weight = 0
    for i, gene in enumerate(chromosome):
        if gene == 1:
            total_value += items[i]["value"]
            total_weight += items[i]["weight"]
    if total_weight > knapsack_capacity:
        return 0  # اگر وزن از ظرفیت بیشتر شود، برازندگی صفر می‌شود.
    return total_value


# انتخاب دو والد برای تولید نسل بعدی (روش رولت)
def selection(population):
    total_fitness = sum(fitness(chromosome) for chromosome in population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for chromosome in population:
        current += fitness(chromosome)
        if current > pick:
            return chromosome


# عملیات تقاطع (Crossover)
def crossover(parent1, parent2):
    point = random.randint(1, len(items) - 1)
    return parent1[:point] + parent2[point:]


# عملیات جهش (Mutation)
def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]  # تغییر 0 به 1 یا 1 به 0
    return chromosome


# الگوریتم ژنتیک
def genetic_algorithm():
    population = [generate_chromosome() for _ in range(population_size)]

    for generation in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1 = selection(population)
            parent2 = selection(population)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))
        population = new_population

        best_chromosome = max(population, key=fitness)
        print(f"Generation {generation}: Best fitness = {fitness(best_chromosome)}")

    best_chromosome = max(population, key=fitness)
    return best_chromosome, fitness(best_chromosome)


# اجرای الگوریتم
best_solution, best_value = genetic_algorithm()
print("Best solution:", best_solution)
print("Best value:", best_value)

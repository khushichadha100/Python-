import random
# Genetic Algorithm parameters
POPULATION_SIZE = 10
CHROMOSOME_LENGTH = 10
MUTATION_RATE = 0.1
NUM_GENERATIONS = 10
def generate_random_chromosome(length):
    return [random.randint(0, 1) for _ in range(length)]
def fitness(chromosome):
    return sum(chromosome)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2
def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]
    return chromosome
# Initialization
population = [generate_random_chromosome(CHROMOSOME_LENGTH) for _ in range(POPULATION_SIZE)]
# Main loop for genetic algorithm
for generation in range(NUM_GENERATIONS):
    # Evaluate fitness
    fitness_scores = [fitness(chromosome) for chromosome in population]
    total_fitness = sum(fitness_scores)
    average_fitness = total_fitness / POPULATION_SIZE
    best_chromosome = population[fitness_scores.index(max(fitness_scores))]
    
    # Report progress
    print(f"Generation {generation+1}: Best Fitness = {max(fitness_scores)}, Average Fitness = {average_fitness}, Best Chromosome = {best_chromosome}")
    
    # Selection - Roulette Wheel Selection
    mating_pool = []
    for i in range(POPULATION_SIZE):
        prob = fitness_scores[i] / total_fitness
        num_entries = int(prob * POPULATION_SIZE)
        mating_pool.extend([population[i]] * num_entries)
    
    # Crossover
    next_generation = []
    while len(next_generation) < POPULATION_SIZE:
        parent1 = random.choice(mating_pool)
        parent2 = random.choice(mating_pool)
        child1, child2 = crossover(parent1, parent2)
        next_generation.append(mutate(child1))
        next_generation.append(mutate(child2))
    
    population = next_generation
# Final result
best_chromosome = max(population, key=fitness)
best_fitness = fitness(best_chromosome)
print("\nFinal Result:")
print("Best Chromosome:", best_chromosome)
print("Best Fitness:", best_fitness)

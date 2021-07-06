from GA_2 import *
import pickle


sol_per_pop = 75
num_weights = n_x*n_h + n_h*n_y

# Defining the population size.
pop_size = (sol_per_pop,num_weights)
#Creating the initial population.

new_population = np.random.choice(np.arange(-1,1,step=0.01),size=pop_size,replace=True)
# new_population = load()

num_generations = 150

num_parents_mating = 20


def saveWeights(filename, weights):
	with open(filename,'wb') as f:
		pickle.dump(weights, f)

maxScore_2 = []
avgScore_2 = []

# maxScore_1 = []
# avgScore_1 = []
for generation in range(num_generations):

    print('##############        GENERATION ' + str(generation)+ '  ###############' )

    fitness, maxscore, avgscore = cal_pop_fitness(new_population)
    print('#######  fittest chromosome in generation ' + str(generation) +' is having fitness value:  ', np.max(fitness))
    maxScore_2.append(maxscore)
    avgScore_2.append(avgscore)
    saveWeights('./weight_data_2.2/gen_' + str(generation)+'.pickle',new_population)


    parents, parents_fitness = select_mating_pool(new_population, fitness, num_parents_mating)
    print(parents.shape)

    offspring_crossover = twoPointCrossover(parents, (pop_size[0] - parents.shape[0], num_weights), parents_fitness)
    offspring_crossover = np.array(offspring_crossover)

    offspring_mutation = mutation(offspring_crossover)


    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

# saveWeights('./NN_two_point/avgValues_1.pickle',avgScore_1)
# saveWeights('./NN_two_point/avgValues_2.pickle',avgScore_2)
# saveWeights('./NN_two_point/maxValues_1.pickle',maxScore_1)
# saveWeights('./NN_two_point/maxValues_2.pickle',maxScore_2)

from random import choice, randint
import numpy as np
import random
from main import *

def cal_pop_fitness(pop):

    maxscore = 0
    avgscore = 0
    fitness = []
    for i in range(pop.shape[0]):
        # fit, sc = run_game_with_ml(display,clock,pop[i])
        scc, sc = main_menu(pop[i])
        maxscore = max(maxscore, scc)
        avgscore += scc
        print('fitness value of chromosome '+ str(i) +' :  ',  "score: ", scc, " reward: ", sc)
        # fitness.append(fit)
        fitness.append(sc)
    avgscore /= 75
    return np.array(fitness), maxscore, avgscore

def select_mating_pool(pop, fitness, num_parents):

    # parents = np.empty((num_parents, pop.shape[1]))
    parents = []
    parents_fitness = []
    # print(pop[0, :])
    for parent_num in range(num_parents):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents_fitness.append(np.max(fitness))

        parents.append(pop[max_fitness_idx, :])
        fitness[max_fitness_idx] = -99999999
    return np.array(parents), parents_fitness

# def getParentIndex(cummFitness, random_value):
#     i = -1
#     for value in cummFitness:
#         if value < random_value:
#             i += 1
#         else:
#             return i

def _random_n(N, chromosomes):
    # shuffle the parents to prevent any correlation
    shuffle = np.arange(len(chromosomes))
    np.random.shuffle(shuffle)
    return shuffle[:N]

def n_sort(fitness,temp, n, minimize):
    """
    :param fitness: fitness value of each chromosome
    :param n: number of chromosomes that are going to be returned
    :param minimize: minimization problem or maximization (boolean)
    :return: return n chromosomes from a sorted array regarding if it is a minimization
             or maximization problem
    """
    # if minimize:
    #     return fitness.argsort()[:n]
    # else:
    #     return fitness.argsort()[-n:][::-1]

    max = -999999
    indices = []
    idx1 = -1
    for i in temp:
        if max < fitness[i]:
            max = fitness[i]
            idx1 = i
    max = -999999
    idx2 = -1
    for i in temp:
        if max < fitness[i] and i != idx1:
            max = fitness[i]
            idx2 = i

    indices.append(idx1)
    indices.append(idx2)
    return indices



def twoPointCrossover(parents, offspring_size, fitness):

    offspring = []
    iterations = offspring_size
    for i in range(iterations[0]):
        # Select a subgroup of parents
        random_parents = _random_n(5, fitness)
        temp = []
        for j in random_parents:
            temp.append(j)
        # print(random_parents)
        temp = np.array(temp)
        # print(fitness)
        # print(temp)
        # random_parents = np.array(random_parents)
        idx = n_sort(fitness, temp, 2, False)
        # print(idx)
        # indices = np.append(idx, random_parents[idx])

        # two point
        prob = random.uniform(0, 1)
        idx1 = idx[0]
        idx2 = idx[1]
        cp1 = np.random.randint(len(parents[0]))
        cp2 = np.random.randint(len(parents[0]))

        while cp1 == cp2:
                cp2 = np.random.randint(len(parents[0]))

        if cp1 > cp2:
                cp1, cp2 = cp2, cp1

        parents[idx1, cp1:cp2], parents[idx2, cp1:cp2] = parents[idx2, cp1:cp2], parents[idx1, cp1:cp2].copy()
        if prob <= 0.5:
            offspring.append(parents[idx1])
        else: offspring.append(parents[idx2])


    return offspring




def mutation(offspring_crossover):

    for idx in range(offspring_crossover.shape[0]):
        prob = random.random()
        if(prob <= 0.1):
            for _ in range(25):
                i = randint(0,offspring_crossover.shape[1]-1)

                random_value = np.random.choice(np.arange(-1,1,step=0.001),size=(1),replace=False)
                offspring_crossover[idx, i] = offspring_crossover[idx, i] + random_value

    return offspring_crossover

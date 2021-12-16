
import math
import random
import copy

from Intraroute import Intraroute
from GAResult import GAResult
from util import generate_trucks

class GA():

    def __init__(self, pop_generator):
        super().__init__()
        self.pop_generator = pop_generator

    def fitness_function(self, ind, graph):
        fitness_value = 0
        n = len(ind.route)
        trucks = generate_trucks(ind.route,ind.breaks)

        for truck in trucks:
            for i in range(len(truck)-1):
                fitness_value += graph[truck[i]][truck[i+1]]
        ind.fitness = fitness_value
        return ind

    def tsp_fitness_function(self, tour, graph):
        fitness_value = 0
        n = len(tour)
        i_break = 0
        for i in range(0, n-1):
            fitness_value += graph[tour[i]][tour[i+1]]
        return fitness_value

    def ga_operation_IPGA(self, population, n, m, min_nodes, max_nodes, graph, evaluator_min):
        pop_size = len(population)
        offspring = []

        pop_suffled = random.sample(range(pop_size), pop_size)
        for i_bucket in range(0, pop_size, 10):
            
            # Step 1: Randomly select 10 individuals that have not been selected from the contemporary population
            i_pop_temp = pop_suffled[i_bucket:i_bucket+10]

            # Step 2: Find the best individual that has the best fitness in 10 individuals just selected
            pop_tmp = [population[i_pop_temp[i]] for i in range(0, 10)]
            best_tmp = evaluator_min(pop_tmp)

            # Step 3: Create a temporary population that consists of 10 individuals.
            # All of the 10 individuals are assigned to the best individual found in procedure 2
            pop_best = [copy.deepcopy(best_tmp) for i in range(0, 10)]

            # Step 4: Generate 2 random mutation segment selection points I and J,
            # and the mutation segment insertion location P
            intraroute = Intraroute()
            # intraroute.load_params(best_tmp)

            # Step 5: Mutate each individual in the temporary population created in
            # procedure 3 in different ways: do nothing, FlipInsert, SwapInsert,
            # LSlideInsert, RSlideInsert or Modify Breaks. The specific process
            # is as follows:

            # (1) Do nothing to the first individual.

            # (2) The second individual performs the FlipInsert operation.
            pop_best[1].route = intraroute.flipinsert(pop_best[1])

            # (3) The third individual performs the SwapInsert operation.
            pop_best[2].route = intraroute.swapinsert(pop_best[2])

            # (4) The fourth individual performs the LSlideInsert operation.
            pop_best[3].route = intraroute.lslideinsert(pop_best[3])

            # (5) The fifth individual performs the RSlideInsert operation.
            pop_best[4].route = intraroute.rslideinsert(pop_best[4])

            # (6) The sixth individual performs the Modify Breaks operation.
            pop_best[5].breaks = self.pop_generator.breaks_generator(n, m, min_nodes, max_nodes)

            # (7) The seventh individual performs the FlipInsert operation
            # and the Modify Breaks operation.
            pop_best[6].route = intraroute.flipinsert(pop_best[6])
            pop_best[6].breaks = self.pop_generator.breaks_generator(n, m, min_nodes, max_nodes)

            # (8) The eighth individual performs the SwapInsert operation
            # and the Modify Breaks operation.
            pop_best[7].route = intraroute.swapinsert(pop_best[7])
            pop_best[7].breaks = self.pop_generator.breaks_generator(n, m, min_nodes, max_nodes)

            # (9) The ninth individual performs the LSlideInsert operation
            # and the Modify Breaks operation.
            pop_best[8].route = intraroute.lslideinsert(pop_best[8])
            pop_best[8].breaks = self.pop_generator.breaks_generator(n, m, min_nodes, max_nodes)

            # (10) The tenth individual performs the RSlideInsert operation
            # and the Modify Breaks operation.
            pop_best[9].route = intraroute.lslideinsert(pop_best[9])
            pop_best[9].breaks = self.pop_generator.breaks_generator(n, m, min_nodes, max_nodes)

            # Join the temporary population that has already performed mutation operation into new population
            offspring += pop_best

        return offspring

    @staticmethod
    def get_min_by_fitness(population):
        best_tmp = population[0]
        for i in range(0, len(population)):
            if population[i].fitness < best_tmp.fitness:
                best_tmp = population[i]

        return best_tmp

    def start(self, max_iters, graph, m, evaluator_min):

        n = len(graph)
        min_nodes = math.ceil(n/(m+1))
        max_nodes = int(n/(m-1))

        population = self.pop_generator.create_population(100, n, m, min_nodes, max_nodes)
        best_global = None

        iter = 0
        data = []
        while iter < max_iters:
            # evaluate population
            population = [self.fitness_function(i, graph) for i in population]
            
            # get best individual of this generation
            best_local = evaluator_min(population)
            data.append(best_local.fitness)    

            # replace global best if necessary
            if best_global is None:
                best_global = best_local
            else:
                best_global = evaluator_min([best_global, best_local])

            # mutate full population
            population = self.ga_operation_IPGA(population, n, m, min_nodes, max_nodes, graph, evaluator_min)
            iter += 1

        result = GAResult(data, best_global)

        return result

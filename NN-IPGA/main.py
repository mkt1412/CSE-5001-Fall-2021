import random
import matplotlib.pyplot as plt
import time
from util import load_graph,generate_trucks
from PopGenerator import PopGenerator
from GA import GA
import os
import argparse

parser = argparse.ArgumentParser(description='NN-IPGA GA')
parser.add_argument('-d', '--data', default='mtsp51', type=str, help='target dataset')


random.seed()

args = parser.parse_args()
instance = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'datasets/{}.txt'.format(args.data))
graph,coords_list = load_graph(instance)
m = 5
max_iters = 196

evaluator = GA.get_min_by_fitness
generator = PopGenerator(graph, PopGenerator.generate_breaks_fully_random)

total_time = 0
start = time.time()

ga = GA(generator)
result = ga.start(max_iters, graph, m, evaluator)

end = time.time()
total_time += end - start


route = result.best_individual.route
breaks = result.best_individual.breaks

trucks = generate_trucks(route,breaks)

for i in range(m):
    real_route = []
    print("Sales man {}:".format(i),end="")
    for j in trucks[i]:
        print("({},{}) ".format(int(coords_list[j][0]),int(coords_list[j][1])),end="")
    
    print('\n')

print("MTSP Route Distance:{}".format(result.best_individual.fitness))
print("Total time:{}".format(total_time))

# record results
# check existence of result file
if os.path.isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), '{}_IPGA_result.txt'.format(args.data))):
    print('{}_IPGA_result.txt exists, append current result to it'.format(args.data))
    with open('{}_IPGA_result.txt'.format(args.data), 'a') as f:
        f.write(str(total_time) + ' ' + str(result.best_individual.fitness) + '\n')
else:
    print('{}_IPGA_result.txt does not exist, create a new one'.format(args.data))
    with open('{}_IPGA_result.txt'.format(args.data), 'w') as f:
        f.write(str(total_time) + ' ' + str(result.best_individual.fitness) + '\n')


import matplotlib.pyplot as plt
from argparse import ArgumentParser
import random
import time
import os

from GA import GA
from util import load_graph, generate_trucks, plot_result
from PopGenerator import PopGenerator


def parse_args():
    '''parse arguments'''
    parser = ArgumentParser()
    parser.add_argument('-d', '--data', required=True, 
                        help='MTSP dataset file path')
    parser.add_argument('-m', '--sales', type=int, default=5, 
                        help='Number of salesmen') 
    parser.add_argument('-it', '--max_iters', type=int, default=190,
                        help='Number of iteration')
    parser.add_argument('--method', default="Polar",
                        help='Initialize method: with Ploar or NN')
    parser.add_argument('--visualize', default=False,
                        help='Visualize result')
    return parser.parse_args()


def main():

    random.seed()
    args = parse_args()

    instance = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'datasets/{}.txt'.format(args.data))

    # evaluate time
    total_time = 0
    start = time.time()

    # initialize graph and coordinates
    graph,coords_list = load_graph(instance)
    evaluator = GA.get_min_by_fitness
    generator = PopGenerator(graph, PopGenerator.generate_breaks_fully_random,coords_list,args.method)
    ga = GA(generator)

    # genetic algorithm start
    result = ga.start(args.max_iters, graph, args.sales, evaluator)

    end = time.time()
    total_time += end - start


    # process the result and visualize
    route = result.best_individual.route
    breaks = result.best_individual.breaks

    trucks = generate_trucks(route,breaks)

    for i in range(args.sales):
        print("Sales man {}:".format(i),end="")
        for j in trucks[i]:
            print("({},{}) ".format(int(coords_list[j][0]),int(coords_list[j][1])),end="")
        print('\n')

    print("Route length:{}".format(len(result.best_individual.route)))
    print("MTSP Route Distance:{}".format(result.best_individual.fitness))
    print("Total time:{}".format(total_time))
    
    if args.visualize:
        plot_result(coords_list, trucks, args.sales)
    
    # record results
    if os.path.isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), '{}_Polar_IPGA_result.txt'.format(args.data))):
        print('{}_Polar_IPGA_result.txt exists, append current result to it'.format(args.data))
        with open('{}_Polar_IPGA_result.txt'.format(args.data), 'a') as f:
            f.write(str(total_time) + ' ' + str(result.best_individual.fitness) + '\n')
    else:
        print('{}_Polar_IPGA_result.txt does not exist, create a new one'.format(args.data))
        with open('{}_Polar_IPGA_result.txt'.format(args.data), 'w') as f:
            f.write(str(total_time) + ' ' + str(result.best_individual.fitness) + '\n')
    

if __name__=="__main__":
    main()
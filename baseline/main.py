from galogic import *
import matplotlib.pyplot as plt
import progressbar
import pdb
import os
import time
import argparse
pbar = progressbar.ProgressBar()

parser = argparse.ArgumentParser(description='baseline GA')
parser.add_argument('-d', '--data', default='mtsp51', type=str, help='target dataset')

t = time.time()

"""
change dataset path and number of nodes
"""
args = parser.parse_args()
dataset_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'datasets/{}.txt'.format(args.data))

with open (dataset_path) as f:
    lines = f.readlines()

# Add Dustbins
for i in range(1, len(lines)):
    x_i, y_i = eval(lines[i].split(' ')[1]), eval(lines[i].split(' ')[2]) 
    RouteManager.addDustbin(Dustbin(x=x_i, y=y_i))

# # Add Dustbins
# for i in range(numNodes):
#     RouteManager.addDustbin(Dustbin())


random.seed(seedValue)
yaxis = [] # Fittest value (distance)
xaxis = [] # Generation count

pop = Population(populationSize, True)
globalRoute = pop.getFittest()
print ('Initial minimum distance: ' + str(globalRoute.getDistance()))

# Start evolving
for i in pbar(range(numGenerations)):
    pop = GA.evolvePopulation(pop)
    localRoute = pop.getFittest()
    if globalRoute.getDistance() > localRoute.getDistance():
        globalRoute = localRoute
    yaxis.append(localRoute.getDistance())
    xaxis.append(i)

elapsed = time.time() - t
print('Total time used: ' + str(elapsed))

print ('Global minimum distance: ' + str(globalRoute.getDistance()))
print ('Final Route: ' + globalRoute.toString())

# check existence of result file
if os.path.isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), '{}_baseline_result.txt'.format(args.data))):
    print('{}_baseline_result.txt exists, append current result to it'.format(args.data))
    with open('{}_baseline_result.txt'.format(args.data), 'a') as f:
        f.write(str(elapsed) + ' ' + str(globalRoute.getDistance()) + '\n')
else:
    print('{}_baseline_result.txt does not exist, create a new one'.format(args.data))
    with open('{}_baseline_result.txt'.format(args.data), 'w') as f:
        f.write(str(elapsed) + ' ' + str(globalRoute.getDistance()) + '\n')



# fig = plt.figure()

# plt.plot(xaxis, yaxis, 'r-')
# plt.show()

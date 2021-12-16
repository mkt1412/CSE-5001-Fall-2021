import random
from random import randint, shuffle
import copy
from IndividualMTSP import IndividualMTSP
from util import compute_angles

class PopGenerator(object):

    def __init__(self, graph, breaks_generator, coords_list, init_method):
        super().__init__()
        self.graph = graph
        self.breaks_generator = breaks_generator
        self.coords_list = coords_list
        self.init_method = init_method

    def create_population(self, pop_size, n, m, min_nodes, max_nodes):

        # create population routes
        if self.init_method == 'Polar':
            pop_routes = self.polar_constrained_init(pop_size, n, m)
        elif self.init_method == 'NN':
            pop_routes = self.nearest_neighbor_init(pop_size, n, m)

        # create population of breakpoints
        pop_breakpoints = [self.breaks_generator(
            n, m, min_nodes, max_nodes) for i in range(0, pop_size)]

        # generate MTSP solution with number of pop_size
        population = [IndividualMTSP(i[0], i[1])
                      for i in zip(pop_routes, pop_breakpoints)]
        return population

    @staticmethod
    def constrained_breaks_rules(n, m, min_nodes, max_nodes=None):

        valid = False

        while valid is False:
            valid = True

            # Rule 1: Generate individual in increasing order
            breakpoints = sorted(random.sample(range(n), m-1))

            # Rule 2: The difference between every two adjacent numbers should not be less than min.
            for i in range(0, len(breakpoints)-1):
                if breakpoints[i+1] - breakpoints[i] < min_nodes or (max_nodes is not None and breakpoints[i+1] - breakpoints[i] > max_nodes):
                    valid = False
                    break

            if not valid:
                continue

            # Rule 3: The first number should not be less than min
            if breakpoints[0] < min_nodes or (max_nodes is not None and breakpoints[0] > max_nodes):
                valid = False
                continue

            # Rule 4: The difference between N and the last number should not be less than min
            if n - breakpoints[-1] < min_nodes or (max_nodes is not None and n - breakpoints[-1] > max_nodes):
                valid = False

        return breakpoints

    @staticmethod
    def generate_breaks_fully_random(n, m, min, max_nodes=None):
        breakpoints = sorted(random.sample(range(2,n-1), m-1))
        return breakpoints
    
    def fully_random_init(self,pop_size,n):

        pop_routes = [[0]+random.sample(range(1,n), n-1) for i in range(0, pop_size)]
        
        return pop_routes

    def polar_constrained_init(self,pop_size,n,m):
        angles = compute_angles(self.coords_list[0],self.coords_list[1:])
        angles = sorted(angles,key=lambda angle:angle[1])
        base_route = [0] + [angle[0]for angle in angles]

        pop_routes = [base_route]
        divide = int(n-1/m)
        for i in range(pop_size-1):
            for j in range(1,m,divide):
                tmp_route = copy.deepcopy(base_route)
                tmp = tmp_route[j:j+divide]
                random.shuffle(tmp)
                del tmp_route[j:j+divide]
                tmp_route[j:j] = tmp
            pop_routes.append(tmp_route)

        return pop_routes

    def nearest_neighbor_init(self, pop_size, n, m):
        depot = 0
        base_route = [depot]

        for i in range(1, n):
            min_dist = None
            next_v = None
            for j in range(0, n):
                if i != j and j not in base_route:
                    if min_dist is None or (min_dist > self.graph[base_route[-1]][j]):
                        min_dist = self.graph[base_route[-1]][j]
                        next_v = j
            base_route.append(next_v)

        pop_routes = [base_route]
        for i in range(pop_size-1):
            tmp_route = copy.deepcopy(base_route)
            start_pos, end_pos = random.sample(range(0,n),2)
            tmp = tmp_route[start_pos:end_pos]
            random.shuffle(tmp)

            del tmp_route[start_pos:end_pos]

            p = random.randint(0,len(tmp_route))
            tmp_route[p:p] = tmp
            
            pop_routes.append(tmp_route)

        return pop_routes
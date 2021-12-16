import random
from random import randint

class Intraroute(object):

    def __init__(self):
        super().__init__()

    def flipinsert(self, ind):
        
        route = ind.route.copy()
        n = len(route)

        # generate range to be mutated
        ij = sorted(random.sample(range(1,n-1), 2))

        # getting segment to be mutated
        segment = route[ij[0]:ij[1]+1]

        #reverse segment
        segment.reverse()

        #removing old segment
        del route[ij[0]:ij[1]+1]

        #inserting reversed segment in random position
        #p = randint(0, len(route)-1)
        p =  randint(1, len(route)-1)
        route[p:p]= segment

        return route


    def swapinsert(self, ind):
        route = ind.route.copy()
        n = len(route)

        # generate range to be mutated
        ij = sorted(random.sample(range(1,n-1), 2))

        # getting segment to be mutated
        segment = route[ij[0]:ij[1]+1]

        #swap endpoints of segment
        segment[0], segment[-1] = segment[-1], segment[0]

        #removing old segment
        del route[ij[0]:ij[1]+1]

        #inserting swapped segment in random position
        # p = randint(0, len(route)-1)
        p =  randint(1, len(route)-1)
        route[p:p]= segment

        return route


    def lslideinsert(self, ind):
        route = ind.route.copy()
        n = len(route)

        # generate range to be mutated
        ij = sorted(random.sample(range(1,n-1), 2))

        # getting segment to be mutated
        segment = route[ij[0]:ij[1]+1]

        # rotate segment to left
        segment.append(segment.pop(0))

        #removing old segment
        del route[ij[0]:ij[1]+1]

        #inserting rotated segment in random position
        # p = randint(0, len(route)-1)
        p =  randint(1, len(route)-1)
        route[p:p]= segment

        return route


    def rslideinsert(self, ind):
        route = ind.route.copy()
        n = len(route)

        # generate range to be mutated
        ij = sorted(random.sample(range(1,n-1), 2))

        # getting segment to be mutated
        segment = route[ij[0]:ij[1]+1]

        # rotate segment to right
        segment.insert(0, segment.pop())

        #removing old segment
        del route[ij[0]:ij[1]+1]

        #inserting rotated segment in random position
        # p = randint(0, len(route)-1)
        p =  randint(1, len(route)-1)
        route[p:p]= segment

        return route
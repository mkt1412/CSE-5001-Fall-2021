class IndividualMTSP(object):
    
    feasibility = None  # degree of feasibility of individual

    def __init__(self, route, breaks):
        super().__init__()
        self.route = route
        self.breaks = breaks

    # penalized fitness value
    def p_f(self):
        n = len(self.route)
        return self.fitness*(1+self.feasibility/n)
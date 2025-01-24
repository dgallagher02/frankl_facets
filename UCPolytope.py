from itertools import chain, combinations


class UCPolytope:

    def __init__(self, base, max_occurence, built = False, build = False, integral = False):
        self.base = base #size of base set
        self.max_occurence = max_occurence #maximal number of occurences of any base element
        self.built = built #as n grows, building the polytope becomes very expensive
        self.build = build #should we build the polytoe now
        self.integral = integral #are we dealing with the actual polytope or the linear relaxation
        self.powerset = self.power_set(list(range(1, base + 1)))

    def __repr__(self):
        return f"Union Closed polytope({self.base}, {self.max_occurence}, built = {self.built}, integral = {self.integral})"



    #This is only capable of building fairly small examples (n,k < 5) on 
    # Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz   1.50 GHz
    # 16GB RAM

    #build a series of triples (A, B, A \cup B) where A and B are subsets of [base]
    # these triples are used to enforce the union-closed condition on the LP
    def union_closed_ab(self):
        res = []
        for i in range(2**self.base - 1):
            family = []
            subset_a = set(self.powerset[i])
            for j in range(i + 1, 2**self.base):
                subset_b = set(self.powerset[j])
                union_ab = subset_a.union(subset_b)
                
                if union_ab != subset_b:
                    res.append([tuple(subset_a), tuple(subset_b), tuple(union_ab)])
        return res
    


    #Constraint on the number of occurences of a particular base element.
    # this gives us base many constraints in the LP

    def less_than_max_occurence(self):
        res = []
        base_list = range(1, self.base + 1)
        for i in base_list:
            family_i = []
            for subset in self.powerset:
                if i in subset:
                    family_i.append(subset)
            res.append(family_i)
        return res
        


    #it is helpful to have the powerset of the base so we have easy
    # labelling for our variables. 
    def power_set(self, iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return tuple(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))


    # build constraint vectors from a given set of families
    # thise is an intermediate step before feeding into gurobi
    # if union_closed = True, then the constraints is x_a + x_b <= x_{a \cup b} + 1
    # this is the vector [0,0,...,0,1,0,...,0,1,0,...,0,-1,0,..,0,1]
    # where the indicies corresponding to the sets a and b get ones, a union b gets a -1 and 
    # the whole shebang is added up and less then the final element of the vector
    # i.e. the vector can be read as [v | b] will be used as v \dot x <= b
    

    def build_constraints(self, families, union_closed = False, max_occ = False):
        res = []
        for family in families:
            v = [0] * (2**self.base + 1)
            for i in range(len(family)):
                ind = self.powerset.index(subset)
                if union_closed and i == 2:
                    v[ind] = -1
                else:
                    v[ind] = 1
            if union_closed:
                v[-1] = 1
            else:
                v[-1] = self.max_occurence
        return res

    
def union_tuple(a, b):
    res = []
    for x in a:
        print('union', x)
        res.append(x)
    for y in b:
        if y not in res:
            res.append(y)
    res = sorted(res)
    return res
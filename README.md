# frankl_facets
Facets of the polytopes P(n,a).

Currently refactoring some of the code. I will make enough available to build some of the smaller polytopes and perform basic manipulations of them.

# Frankl conjecture aka Union Closed conjecture

Back in the 70s Peter Frankl (possibly someone else) came up with the following conjecture.

Given a union-closed family $$\mathcal{F}$$ which is a subset of the powerset on $n$ letters, there exists some element $i \in [n]$ such that $i$ is in at least half of the sets in $\mathcal{F}$.

This conjecture has been open with minimal progress for about fifty years. There were some great strides made in 2023 using information theory and entropy. However, my thesis took a different approach and used mixed integer programs to formulate the conjecture as an optimization problem so that it could be studied with the tools of optimization and polyhedral geometry. That work is detailed in my thesis. This repository contains the programs I wrote which formulate the conjecture as MIPs and use Gurobi as a solver to gain some computational insight into larger examples.

# Goal of computation
All of the models the were built with these programs were used to build examples from which theorems about the Union-closed polytope could be derived. Essentially, the models found facets of the polytope in low dimensions that I proved existed in some form for the general polytope. Finding facets which were easily interpretable combinatorially or significantly diminished the gap between linear relaxation and the integral polytope were the ideal.

# Warning on complexity
Finding the integer hull of a polytope is an NP-Hard problem. Additionally finding the first Chvatal closure of a polytope is NP-Hard and we must go through this process several times. Finally, the problem is transformed into a MIP by taking variables in the powerset of our base. In other words, the union closed polytope is a $2^n$ dimensional polytope with the number of vertices potentially on the order of $2^{2^n}$. This is all to say that this is a computationally hard problem and the results obtained here are meant to serve as a springboard for non-computational work.
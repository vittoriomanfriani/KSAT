import SimAnn
import KSAT

## Generate a problem to solve.
# This generate a K-SAT instance with N=100 variables and M=350 Clauses
ksat = KSAT.KSAT(100, 350, 4, seed=8)

## Optimize it.
best = SimAnn.simann(ksat,
                     mcmc_steps = 1000, anneal_steps = 20,
                     beta0 = 1.0, beta1 = 10.0,
                     seed = 5,
                     debug_delta_cost = False) # set to True to enable the check

# %%
import SimAnn
import KSAT

import importlib
importlib.reload(SimAnn)
importlib.reload(KSAT)
#%%

## Generate a problem to solve.
# This generate a K-SAT instance with N=100 variables and M=350 Clauses
ksat = KSAT.KSAT(200, 100, 3, seed=41)

## Optimize it.
best = SimAnn.simann(ksat,
                     mcmc_steps = 1000, anneal_steps = 20,
                     beta0 = 0.1, beta1 = 10.0,
                     seed = 41,
                     debug_delta_cost = False) # set to True to enable the check

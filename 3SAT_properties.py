# %%
import SimAnn
import KSAT
from tqdm import tqdm

import importlib
importlib.reload(SimAnn)
importlib.reload(KSAT)

# %%
M = [200, 400, 500, 600, 700, 800, 900, 1000]
percentage_solved = {}
for m in tqdm(M):
    ksat = KSAT.KSAT(200, m, 3, seed=41)
    cost_n = []
    numbers_solved_m = 0
    for i in range(30):
        best = SimAnn.simann(ksat,
                             mcmc_steps=1000, anneal_steps=10,
                             beta0=0.1, beta1=10.0,
                             seed=None,
                             debug_delta_cost=False)
        cost_n.append(best.cost())
        if best.cost() == 0:
            numbers_solved_m += 1

    percentage_solved[m] = numbers_solved_m/30

# %%
percentage_solved
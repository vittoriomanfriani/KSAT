# %%
import SimAnn
import KSAT
from tqdm import tqdm

import importlib
importlib.reload(SimAnn)
importlib.reload(KSAT)



# %%
def empirical_probability(M, N = 200, trials = 30, mcmc_steps = 100):
    ksat = KSAT.KSAT(N, M, 3, seed=41)
    numbers_solved = 0
    for i in tqdm(range(trials)):
        best = SimAnn.simann(ksat,
                             mcmc_steps=mcmc_steps, anneal_steps=10,
                             beta0=0.1, beta1=10.0,
                             seed=None,
                             debug_delta_cost=False)
        if best.cost() == 0:
            numbers_solved += 1

    return numbers_solved/trials

# %%
M = [200, 400, 500, 600, 700, 800, 900, 1000]
percentage_solved = {}
for m in tqdm(M):
    percentage_solved[m] = empirical_probability(m)

# %%
def find_threshold(N=200, target_prob=0.5, trials=30, min_M=500, max_M=1000, max_steps = 10):
    steps = 0
    while max_M - min_M > 1:
        mid_M = (min_M + max_M) // 2
        prob = empirical_probability(mid_M, N=N, trials=trials, mcmc_steps=1000)
        if prob < target_prob:
            max_M = mid_M
        else:
            min_M = mid_M
        steps += 1
        if steps >= max_steps:
            break
        print(steps, max_M - min_M)
    return min_M, max_M


threshold_min, threshold_max = find_threshold(N=200, target_prob=0.5, min_M=200, max_M=1000)
print(threshold_min, threshold_max)

# %%
empirical_probability(M = 703, mcmc_steps=1000)
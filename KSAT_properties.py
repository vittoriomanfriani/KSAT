import SimAnn
import KSAT
import importlib
import Utils
importlib.reload(SimAnn)
importlib.reload(KSAT)
importlib.reload(Utils)


def empirical_probability(M, N = 200, trials = 30, mcmc_steps = 100):
    ksat = KSAT.KSAT(N = N, M = M, K = 3, seed=45)
    numbers_solved = 0
    for _ in range(trials):
        best = SimAnn.simann(ksat,
                             mcmc_steps=mcmc_steps, anneal_steps=30,
                             beta0=1, beta1=10.0,
                             seed=None,
                             debug_delta_cost=False)
        if best.cost() == 0:
            numbers_solved += 1

    return numbers_solved/trials

def find_threshold(N, target_prob=0.5, trials=30, min_M=100, max_M=2000, max_steps = 10, epsilon = 0.05):
    steps = 0
    while max_M - min_M > 1:
        mid_M = (min_M + max_M) // 2
        prob = empirical_probability(mid_M, N=N, trials=trials, mcmc_steps=100)
        print(prob, mid_M)
        if abs(target_prob - prob) <= epsilon or prob == target_prob:
            return mid_M
        elif prob < target_prob:
            max_M = mid_M
        elif prob > target_prob:
            min_M = mid_M

        steps += 1
        if steps >= max_steps:
            break
    return mid_M

def loss_function(M, n):
    return abs(0.5 - empirical_probability(M, n))

def find_treshold_2(N, max_iters = 10, alpha = 1, grad_f = None, epsilon = 1e-8):

    if isinstance(N, list):
        M_alg = {}
        for n in N:
            M_alg_n = Utils.grad_desc1d(lambda M: loss_function(M, n),
                                        x0 = 300,
                                        alpha = alpha,
                                        max_iters = max_iters,
                                        grad_f = grad_f,
                                        epsilon = epsilon)
            M_alg[n] = M_alg_n
        return M_alg
    else:
        return Utils.grad_desc1d(lambda M: loss_function(M, N),
                                 x0 = 300,
                                 alpha = alpha,
                                 max_iters = max_iters,
                                 grad_f = grad_f,
                                 epsilon = epsilon)






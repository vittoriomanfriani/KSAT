import SimAnn
import KSAT
import importlib
import Utils
importlib.reload(SimAnn)
importlib.reload(KSAT)
importlib.reload(Utils)


def empirical_probability(M, N=200, trials=30, mcmc_steps=500):
    # Create a K-SAT problem instance with N variables, M clauses, and K=3 (3-SAT).
    ksat = KSAT.KSAT(N=N, M=M, K=3, seed=None)
    # Initialize a counter to track the number of trials where a solution is found.
    numbers_solved = 0
    # Perform the Simulated Annealing algorithm over the specified number of trials.
    for k in range(trials):

        best_c = SimAnn.simann(ksat,
                               mcmc_steps=mcmc_steps,  # Number of MCMC steps in each annealing iteration.
                               anneal_steps=20,       # Number of annealing steps.
                               beta0=1,               # Initial inverse temperature (beta).
                               beta1=10.0,            # Final inverse temperature (beta).
                               seed=None,             # No seed specified for randomness.
                               debug_delta_cost=False) # Disable debugging output for delta cost changes.
        # If the cost of the best solution found is 0 (all clauses satisfied), increment the counter.
        if best_c == 0:
            numbers_solved += 1
    # Return the fraction of successful trials, representing the empirical probability of solving the K-SAT problem.
    return numbers_solved / trials

def find_threshold(N, target_prob=0.5, trials=30, min_M=100, max_M=2000, max_steps=10):
    # Initialize a counter to track the number of binary search steps.
    steps = 0
    # Continue binary search until the range of M (max_M - min_M) is reduced to 1 or less.
    while max_M - min_M > 1:
        # Compute the midpoint of the current range of M.
        mid_M = (min_M + max_M) // 2
        # Estimate the empirical probability of solving the K-SAT problem for mid_M clauses
        prob = empirical_probability(mid_M, N=N, trials=trials, mcmc_steps=200)
        # If the empirical probability matches the target probability, return the current mid_M as the threshold.
        if prob == target_prob:
            return mid_M
        # If the probability is less than the target, search the lower half by reducing max_M.
        elif prob < target_prob:
            max_M = mid_M
            # If the probability is greater than the target, search the upper half by increasing min_M.
        elif prob > target_prob:
            min_M = mid_M
        # Increment the binary search step counter.
        steps += 1
        # If the maximum number of steps is reached, exit the loop to avoid infinite iterations.
        if steps >= max_steps:
            break
    # Return the midpoint as the best approximation of the threshold after the loop ends.
    return mid_M

def loss_function(M, n):
    return abs(0.5 - empirical_probability(M, n))

def find_treshold_grad_desc(N, max_iters = 10, alpha = 1, grad_f = None, epsilon = 1e-8):

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






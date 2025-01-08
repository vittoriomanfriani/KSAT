from tqdm import tqdm

def grad(f, x, delta = 1):
    return (f(x + delta) - f(x - delta)) / 2 * delta

def grad_desc1d(function, x0, alpha = 100, max_iters = 100, grad_f = None, epsilon = 1e-8):
    if grad_f is None:
        grad_f = lambda x: grad(function, x)

    # initialize the starting point at x0
    x = x0

    # repeat for max_iters times
    for k in tqdm(range(max_iters)):
    # add a stopping criterion based on the value of the gradient
        p = grad_f(x)
        x = int(round(x - alpha * p))

        if abs(p) < epsilon:
            break

    # return the final x
    return x
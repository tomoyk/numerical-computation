def solve_CG(A, b, k):
    alpha = 0
    x = np.array([[0], [0], [0]])
    r = A*x-b
    p = A.T * r
    beta = -(naiseki(p, A.T*(A*x-b))) / (naiseki(p, A.T*A*p))
    x = x + beta*p

    for i in range(k):
        _Ap = A.T * A * p
        bunshi = - (naiseki(p, A.T * A * A.T*r))
        bunbo = naiseki(p, _Ap)
        
        alpha = bunshi / bunbo
        p = A.T * r + alpha*p
        beta = -(naiseki(p, A.T*(A*x-b))) / (naiseki(p, A.T*A*p))
        x = x + beta*p

    return x

import numpy as np
import scipy.linalg as lg

def lu(A, b):
    sol = []
    L,U = lg.lu(A,True)
    y = lg.solve(L,b)
    x = lg.solve(U,y)
    return list(x)

def sor(A, b):
    sol = []
    ITERATION_LIMIT = 5000
    omega = 0.9
    size = len(A)
    
    # A = D - L - U
    D = np.zeros_like(A)
    for i in range(size):
        D[i][i] = A[i][i]

    L = np.zeros_like(A)
    for i in range(size):
        for j in range(i):
            L[i][j] = -A[i][j]
    
    U = np.zeros_like(A)
    for i in range(size):
        for j in range(i+1,size):
            U[i][j] = -A[i][j]
    
    #omega
    K = np.zeros_like(A)
    for i in range(size):
        K[i][i] = 1/D[i][i]
    eig = lg.eigvals(K)
    p = max(abs(eig))    
    p2 = np.power(p,2)
    omega = 2 * (1 - np.sqrt(1 - p2)) / p2    
    print ('omega = ' ,omega)
    
    omega = 0.6
    
    
    Q = D/omega -L
    K = np.linalg.inv(Q).dot(Q-A)
    c = np.linalg.inv(Q).dot(b)
    x = np.zeros_like(b)
    
    
    for itr in range(ITERATION_LIMIT):
        x    = K.dot(x) + c
    
    return list(x)

def solve(A, b):
    condition = check_condition(A)
    if condition:
        print('Solve by lu(A,b)')
        return lu(A,b)
    else:
        print('Solve by sor(A,b)')
        return sor(A,b)

if __name__ == "__main__":
    ## import checker
    ## checker.test(lu, sor, solve)

    A = [[2,1,6], [8,3,2], [1,5,1]]
    b = [9, 13, 7]
    sol = solve(A,b)
    print(sol)
    
    A = [[6566, -5202, -4040, -5224, 1420, 6229],
         [4104, 7449, -2518, -4588,-8841, 4040],
         [5266,-4008,6803, -4702, 1240, 5060],
         [-9306, 7213,5723, 7961, -1981,-8834],
         [-3782, 3840, 2464, -8389, 9781,-3334],
         [-6903, 5610, 4306, 5548, -1380, 3539.]]
    b = [ 17603,  -63286,   56563,  -26523.5, 103396.5, -27906]
    sol = solve(A,b)
    print(sol)

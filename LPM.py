# This is a program for Longest Path Matrix.

# Import libraires
import numpy as np

# Input used
A = np.array([[-1, 0, -1, -1],
              [4, -1, 0, -1],
              [5, -1, -1, 0],
              [5, -1, -1, -1]])
H, W = A.shape
L = [A]  # store L matrix


# function check condition of k and return lij element
def Kelement(x, y, z):
    """This function take input "x" and "y" as row and column
    of element and "z" as index of "L" matrix, and returns lij element."""
    K = [-1]  # if path doesn't exists
    for i in range(H):
        l1 = A[x, i]
        l2 = L[z][i, y]
        if l1 != -1 and l2 != -1:
            K.append(l1 + l2)
    return max(K)


# function for calculation of Iteration bound
def Ibound():
    Ib = []
    for k in range(H):
        M = L[k]
        for i in range(H):
            Ib.append(M[i, i] / (k + 1))  # divide by (k+1), "k" starts from 0
    return max(Ib)


# main program
for k in range(H - 1):
    M = np.zeros((H, W))
    for i in range(H):
        for j in range(W):
            Lij = Kelement(i, j, k)
            M[i, j] = Lij
    L.append(M)


# display output
print("Solution using Longest Path Matrix Algorithm:")
for i in range(H):
    print(f"L({i+1}) = {L[i]}\n")
T_bound = Ibound()
print(f"Iteration Bound is {T_bound}.")

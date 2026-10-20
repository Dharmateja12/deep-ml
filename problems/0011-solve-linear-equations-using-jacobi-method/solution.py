import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	d = np.diag(A)
	R = A - np.diagflat(d)
	x = np.zeros_like(b)
	for i in range(n):
		x = (b - R @ x)/d 
	
	return np.round(x,4).tolist()
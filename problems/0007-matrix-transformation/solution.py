import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	T = np.array(T)
	S = np.array(S)
	if (np.linalg.matrix_rank(T) < T.shape[0]) or (np.linalg.matrix_rank(S) < S.shape[0]):
		return -1 
	else :
		return (np.linalg.inv(T) @ A @ S).tolist()
import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	a = 1 if mode == 'row' else 0
	return np.mean(matrix,axis = a).tolist()
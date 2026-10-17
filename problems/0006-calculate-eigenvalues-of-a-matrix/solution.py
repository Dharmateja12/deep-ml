import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	eigenvalues = np.linalg.eigvals(np.array(matrix))
	return eigenvalues.tolist()
import math
from typing import Tuple

from src.probability import NormalProbability


class Inference:
    def two_sided_p_value(x: float, mu: float = 0, sigma: float = 1) -> float:
        if x >= mu:
            return 2 * NormalProbability.above(x, mu, sigma)
        else:
            return 2 * NormalProbability.below(x, mu, sigma)
    
    def estimated_parameters(N: int, n: int) -> Tuple[float, float]:
        p = n/N
        sigma = math.sqrt(p * (1-p) / N)
        return p, sigma
    
    #TODO: use t-distribution
    def a_b_test_statistic(N_a: int, n_a: int, N_b: int, n_b: int) -> float:
        p_a, sigma_a = Inference.estimated_parameters(N_a, n_a)
        p_b, sigma_b = Inference.estimated_parameters(N_b, n_b)
        
        return (p_b - p_a) / math.sqrt(sigma_a ** 2 + sigma_b ** 2)
    
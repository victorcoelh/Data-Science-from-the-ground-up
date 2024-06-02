import math
import random
from matplotlib import pyplot as plt
from typing import Tuple


#TODO: Impelement partials
class Distributions:
    @staticmethod
    def uniform_pdf(x: float) -> float:
        return 1 if 0 <= x <= 1 else 0
    
    @staticmethod
    def uniform_cdf(x: float) -> float:
        if x < 0: return 0
        elif x < 1: return x
        else: return 1
    
    @staticmethod
    def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
        k = math.sqrt(2*math.pi)*sigma
        exponent = -((x-mu)**2) / (2*(sigma**2))
        return math.exp(exponent) / k
    
    @staticmethod
    def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
        return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2
    
    @staticmethod
    def binomial_to_normal(p: float, n: int) -> Tuple[float, float]:
        mu = p*n
        sigma = math.sqrt(p * (1-p) * n)
        return mu, sigma
    
    #TODO: reimplement inverse_normal_cdf
    @staticmethod
    def inverse_normal_cdf(p: float,
                           mu: float = 0,
                           sigma: float = 0,
                           tolerance: float = 0.00001) -> float:
        if mu != 0 or sigma != 1:
            return mu + sigma * Distributions.inverse_normal_cdf(p, tolerance=tolerance)

        low_z = -10.0                      # normal_cdf(-10) is (very close to) 0
        hi_z  =  10.0                      # normal_cdf(10)  is (very close to) 1
        while hi_z - low_z > tolerance:
            mid_z = (low_z + hi_z) / 2     # Consider the midpoint
            mid_p = Distributions.normal_cdf(mid_z)      # and the CDF's value there
            if mid_p < p:
                low_z = mid_z              # Midpoint too low, search above it
            else:
                hi_z = mid_z               # Midpoint too high, search below it

        return mid_z
    
    @staticmethod
    def bernoulli_trial(p: float) -> int:
        return 1 if random.random() < p else 0
    
    @staticmethod
    def binomial(p: float, n: int):
        return sum([Distributions.bernoulli_trial(p) for i in range(n)])


class NormalProbability:
    @staticmethod
    def below(x: float, mu: float = 0, sigma: float = 1) -> float:
        return Distributions.normal_cdf(x, mu, sigma)
    
    @staticmethod
    def above(x: float, mu: float = 0, sigma: float = 1) -> float:
        return 1 - NormalProbability.below(x, mu, sigma)
    
    @staticmethod
    def between(x: float, y: float, mu: float = 0, sigma: float = 1) -> float:
        high = NormalProbability.below(y, mu, sigma)
        low = NormalProbability.below(x, mu, sigma)
        return high - low
    
    @staticmethod
    def outside(x: float, y: float, mu: float = 0, sigma: float = 1) -> float:
        return 1 - NormalProbability.between(x, y, mu, sigma)
    
    def upper_bound(p: float, mu: float = 0, sigma: float = 1) -> float:
        return Distributions.inverse_normal_cdf(p, mu, sigma)
    
    def lower_bound(p: float, mu: float = 0, sigma: float = 1) -> float:
        return Distributions.inverse_normal_cdf(1 - p, mu, sigma)
    
    def two_sided_bound(p: float, mu: float = 0, sigma: float = 1) -> float:
        tail_probability = (1 - p) / 2  
        return abs(NormalProbability.lower_bound(tail_probability, mu, sigma))


def plot_function(func: callable, label: str, *args):
    x = [i/10 for i in range(-50, 50)]
    y = [func(x, *args) for x in x]
    
    plt.plot(x, y, label=label)


if __name__ == '__main__':
    print(NormalProbability.two_sided_bound(0.2))
    
    # visual representation of the probability density functions
    plot_function(Distributions.normal_pdf, "mu=0,sigma=1", 0, 1)
    plot_function(Distributions.normal_pdf, "mu=0,sigma=2", 0, 2)
    plot_function(Distributions.normal_pdf, "mu=0,sigma=0.5", 0, 0.5)
    plot_function(Distributions.normal_pdf, "mu=-1,sigma=1", -1, 1)
    plt.legend()
    plt.show()

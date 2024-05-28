from typing import List
from collections import Counter
import math

from src.linear_algebra import Vector


class Statistics:
    @classmethod
    def mean(cls, vector: Vector) -> float:
        return sum(vector)/len(vector)
    
    @classmethod
    def median(cls, vector: Vector) -> float:
        x = sorted(vector)
        index = int(len(x)//2) - 1
        
        if len(vector) % 2 == 0:  #even
            return (x[index] + x[index+1]) / 2
        else:
            return x[index]
    
    @classmethod
    def quartile(cls, vector: Vector, p: float) -> float:
        index = int(p * len(vector))
        return sorted(vector)[index]
    
    @classmethod
    def mode(cls, vector: Vector) -> Vector:
        counts = Counter(vector)
        max_count = max(counts.values())

        return [x for x, count in counts.items()
                if count == max_count]
        
    @classmethod
    def data_range(cls, vector: Vector) -> float:
        return max(vector) - min(vector)
    
    @classmethod
    def deviations(cls, vector: Vector) -> Vector:
        mean = cls.mean(vector)
        return Vector([x - mean for x in vector])
    
    @classmethod
    def variance(cls, vector: Vector) -> float:
        deviations = cls.deviations(vector)
        deviations = [x**2 for x in deviations]
        return (sum(deviations)) / (len(vector)-1)
    
    @classmethod
    def sd(cls, vector: Vector) -> float:
        return math.sqrt(cls.variance(vector))
    
    @classmethod
    def interquartile_range(cls, vector: Vector) -> float:
        return cls.quartile(vector, 0.75) - cls.quartile(vector, 0.25)
    
    @classmethod
    def covariance(cls, xs: Vector, ys: Vector) -> float:
        return (cls.deviations(xs) * cls.deviations(ys)) / (len(xs)-1)

    @classmethod
    def correlation(cls, xs: Vector, ys: Vector) -> float:
        sd_x = cls.sd(xs)
        sd_y = cls.sd(ys)
        
        if sd_x == 0 or sd_y == 0: return 0
        return cls.covariance(xs, ys) / sd_x / sd_y

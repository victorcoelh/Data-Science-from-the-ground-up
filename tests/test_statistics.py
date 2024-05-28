import pytest

from src.linear_algebra import Vector
from src.statistics import Statistics


class TestStatistics:
    def test_mean(self):
        vector = Vector([2,3,4])
        assert Statistics.mean(vector) == 3
        
    def test_median(self):
        vector = Vector([2,3,4,5])
        assert Statistics.median(vector) == 3.5
    
    def test_quartile(self):
        vector = Vector([2,3,4,5,6])
        assert Statistics.quartile(vector, 0.75) == 5
    
    def test_mode(self):
        vector = Vector([2,2,2,3,3,3,4,5,5])
        assert Statistics.mode(vector) == [2,3]
    
    def test_data_range(self):
        vector = Vector([0, 3, 5, 1, 2, 12, 3])
        assert Statistics.data_range(vector) == 12
    
    def test_deviations(self):
        vector = Vector([1,2,3,4,5])
        assert Statistics.deviations(vector) == [-2,-1,0,1,2]
    
    def test_variance(self):
        vector = Vector([1,2,3,4,5])
        assert Statistics.variance(vector) == 2.5
    
    def test_sd(self):
        vector = Vector([1,2,3,4,5])
        assert Statistics.sd(vector) == pytest.approx(1.5811, 0.05)
    
    def test_interquartile_range(self):
        vector = Vector([1,2,3,4,5])
        assert Statistics.interquartile_range(vector) == 2
    
    def test_covariance(self):
        vector_1 = Vector([1,2,3,4,5])
        vector_2 = Vector([2,4,5,6,9])
        assert Statistics.covariance(vector_1, vector_2) == 4
    
    def test_correlation(self):
        vector_1 = Vector([1,2,3,4,5])
        vector_2 = Vector([2,4,5,6,9])
        assert Statistics.correlation(vector_1, vector_2) == pytest.approx(0.97, 0.05)

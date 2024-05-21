import pytest
from src.linear_algebra import Vector, Matrix


class TestVector:
    def test_vector_sum(self):
        example = Vector([1,2,3])
        vector_list = [Vector(example), Vector(example), Vector(example)]
        assert Vector.sum_vectors(vector_list) == Vector([3,6,9])
        
    def test_mean_vector(self):
        example = Vector([1,2,3])
        vector_list = [Vector(example), Vector(example), Vector(example)]
        assert Vector.mean_vector(vector_list) == Vector([1,2,3])
        
    def test_size(self):
        example_vector = Vector([1,2,3])
        assert example_vector.size == 3
    
    def test_magnitude(self):
        example_vector = Vector([3, 4])
        assert example_vector.magnitude() == 5
        
    def test_distance_to(self):
        example_1 = Vector([1,2,3])
        example_2 = Vector([4,5,6])
        assert example_1.distance_to(example_2) == pytest.approx(5.19, 0.05)
    
    def test_sum(self):
        example_1 = Vector([1,2,3])
        example_2 = Vector([4,5,6])
        assert example_1 + example_2 == Vector([5,7,9])
    
    def test_subtraction(self):
        example_1 = Vector([1,2,3])
        example_2 = Vector([4,5,6])
        assert example_1 - example_2 == Vector([-3,-3,-3])
    
    def test_multiplication_scalar(self):
        example_vector = Vector([1,2,3])
        scalar = 4
        assert example_vector * scalar == Vector([4,8,12])
    
    def test_multiplication_vector(self):
        example_1 = Vector([1,2,3])
        example_2 = Vector([4,5,6])
        assert example_1 * example_2 == 32


class TestMatrix:
    def test_make_matrix(self):
        pass
    
    def test_identity_matrix(self):
        pass
    
    def test_shape(self):
        pass
    
    def test_get_row(self):
        pass
    
    def test_get_column(self):
        pass

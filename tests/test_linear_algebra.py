import pytest
from src.linear_algebra import Vector, Matrix


@pytest.fixture
def example_vector():
    return Vector([1,2,3])


@pytest.fixture
def example_matrix():
    return Matrix([[1,2,3], [4,5,6]])


class TestVector:
    def test_vector_sum(self, example_vector):
        vector_list = [Vector(example_vector), Vector(example_vector), Vector(example_vector)]
        assert Vector.sum_vectors(vector_list) == Vector([3,6,9])
        
    def test_mean_vector(self, example_vector):
        vector_list = [Vector(example_vector), Vector(example_vector), Vector(example_vector)]
        assert Vector.mean_vector(vector_list) == Vector([1,2,3])
        
    def test_size(self, example_vector):
        assert example_vector.size == 3
    
    def test_magnitude(self, example_vector):
        example_vector = Vector([3, 4])
        assert example_vector.magnitude() == 5
        
    def test_distance_to(self, example_vector):
        example_2 = Vector([4,5,6])
        assert example_vector.distance_to(example_2) == pytest.approx(5.19, 0.05)
    
    def test_sum(self, example_vector):
        example_2 = Vector([4,5,6])
        assert example_vector + example_2 == Vector([5,7,9])
    
    def test_subtraction(self, example_vector):
        example_2 = Vector([4,5,6])
        assert example_vector - example_2 == Vector([-3,-3,-3])
    
    def test_multiplication_scalar(self, example_vector):
        scalar = 4
        assert example_vector * scalar == Vector([4,8,12])
    
    def test_multiplication_vector(self, example_vector):
        example_2 = Vector([4,5,6])
        assert example_vector * example_2 == 32


class TestMatrix:
    def test_make_matrix(self):
        sum_matrix = Matrix.make_matrix(2, 2, lambda x,y: x+y)
        
        for i in range(sum_matrix.shape[0]):
            for j in range(sum_matrix.shape[1]):
                assert sum_matrix[i][j] == i+j
    
    def test_identity_matrix(self):
        identity = Matrix.identity_matrix(9, 9)
        
        for i in range(identity.shape[0]):
            for j in range(identity.shape[1]):
                if i==j: assert identity[i][j] == 1
                else: assert identity[i][j] == 0
    
    def test_shape(self, example_matrix):
        assert example_matrix.shape == (2, 3)
    
    def test_get_row(self, example_matrix):
        assert example_matrix.get_row(0) == [1, 2, 3]
    
    def test_get_column(self, example_matrix):
        assert example_matrix.get_column(0) == [1, 4]

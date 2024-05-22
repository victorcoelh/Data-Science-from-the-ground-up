from collections import UserList
from typing import Self, Union, List, Tuple, Callable
import math


#TODO: Unit testing and type checking
class Vector(UserList):
    @classmethod
    def sum_vectors(cls, vectors: List[Self]) -> Self:
        #TODO: Attempt functional approach
        result = Vector()
        
        for i in range(vectors[0].size):
            ith_sum = sum([v[i] for v in vectors])
            result.append(ith_sum)
        return result
    
    @classmethod
    def mean_vector(cls, vectors: List[Self]) -> Self:
        sum_vector = Vector.sum_vectors(vectors)
        n = len(vectors[0])
        return Vector([x/n for x in sum_vector])
    
    @property
    def size(self) -> int:
        return len(self)
    
    def magnitude(self) -> float:
        sum_of_squares = self * self
        return math.sqrt(sum_of_squares)
    
    def distance_to(self, other: Self) -> float:
        difference = self - other
        return difference.magnitude()
    
    def __add__(self, other: Self) -> Self:
        result = [self[i] + other[i] for i in range(self.size)]
        return Vector(result)
    
    def __sub__(self, other: Self) -> Self:
        result = [self[i] - other[i] for i in range(self.size)]
        return Vector(result)
    
    def __mul__(self, other: Union[Self, float]) -> Self:
        if isinstance(other, Vector):
            return self.dot(other)
        else:
            return self.scalar_multiply(other)
    
    def scalar_multiply(self, other: float) -> Self:
        result = [x*other for x in self]
        return Vector(result)
    
    def dot(self, other: Self) -> float:
        products = [self[i] * other[i] for i in range(len(self))]
        return sum(products)
    

class Matrix(UserList):
    @classmethod
    def make_matrix(cls, num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]) -> Self:
        result = [[entry_fn(i, j)
                for j in range(num_cols)]
                for i in range(num_rows)]
        return Matrix(result)
    
    @classmethod
    def identity_matrix(cls, num_rows: int, num_cols: int) -> Self:
        return Matrix.make_matrix(num_rows, num_cols, lambda i,j: 1 if i == j else 0)
    
    @property
    def shape(self) -> Tuple[int, int]:
        rows = len(self)
        columns = len(self[0])
        return (rows, columns)
    
    def get_row(self, row: int) -> Vector:
        return Vector(self[row])
    
    def get_column(self, column: int) -> Vector:
        return [row[column] for row in self]

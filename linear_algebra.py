from collections import UserList
from typing import Self, Union


class Vector(UserList):
    def __add__(self, other: Self) -> Self:
        return [self[i] + other[i] for i in range(len(self))]
    
    def __sub__(self, other: Self) -> Self:
        return [self[i] - other[i] for i in range(len(self))]
    
    def __mul__(self, other: Union[Self, float]) -> Self:
        if isinstance(other, Vector):
            return self.dot(other)
        else:
            return self.scalar_multiply(other)
    
    def scalar_multiply(self, other: float):
        return [x*other for x in self]
    
    def dot(self, other: Self):
        products = [self[i] * other[i] for i in range(len(self))]
        return sum(products)
    

class Matrix(UserList):
    pass
        

if __name__ == '__main__':
    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6])
    print(a+b)
    print(a-b)
    print(a*b)
    print(a*5)

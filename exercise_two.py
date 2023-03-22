# write a function that accepts a number as a parameter. 

# The function should return a number that’s the difference between the largest 
# and smallest numbers that the digits can form in the number.

# For example, if the parameter is “213”, the function should return “198”, which is the result of 123 subtracted from 321.
from typing import List


class Main:
    def __init__(self, number: int) -> None:
        self.number = number

    def split_number(self) -> List[str]:
        split = [int(num) for num in str(self.number)]
        return split

    def get_largest(self) -> str:
        largest = self.split_number()
        largest.sort(reverse=True)
        largest = "".join(map(str, largest))
        return largest
    
    def get_smallest(self) -> str:
        smallest = self.split_number()
        smallest.sort()
        smallest = "".join(map(str, smallest))
        return smallest
    

class Calculate(Main):
    def __init__(self, number: int) -> None:
        super().__init__(number)

    def result(self) -> int:
        result = int(self.get_largest()) - int(self.get_smallest())
        return result
    

x = Calculate(number= 15)
print(x.result())

# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload, Union
import numpy as np 
from numpy.typing import NDArray
import copy

from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("starting_sequence must be a sequence")
        
        self.__data_type=data_type
        self.__elements=[]
        self.__item_count=len(starting_sequence)

        for item in starting_sequence:
            if not isinstance(item,self.__data_type):
                raise TypeError(f"Element '{item}' is not of type {self.__data_type.__name__}")
        
        for index in range(self.__item_count):
            self.__elements.append(copy.deepcopy(starting_sequence[index]))

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if isinstance(index, slice):
            start, stop = index.start, index.stop
            if start >= self.__item_count or stop > self.__item_count:
                raise IndexError("Out of Bounds")
            items_to_return = self.__elements[index]
            return Array(starting_sequence=items_to_return, data_type=self.__data_type)
        else:
            return self.__elements[index]
            
    def __setitem__(self, index: int, item: T) -> None:
        if index >=self.__item_count:
            raise IndexError("Out of Bounds")
        if not isinstance(item, self.__data_type):
            raise TypeError("Item is not correct type")
        self.__elements[index]=item

    def append(self, data: T) -> None:
        self.__elements.append(data)
        self.__item_count +=1

    def append_front(self, data: T) -> None:
        self.__elements.insert(0,data)
        self.__item_count +=1

    def pop(self) -> None:
        if self.__item_count==0:
            raise IndexError("Empty Array :(")
        item=self.__elements.pop()
        self.__item_count -=1
        return item
    
    def pop_front(self) -> None:
        if self.__item_count ==0:
            raise IndexError("Empty Array :(")
        item=self.__elements.pop(0)
        self.__item_count -=1
        return item

    def __len__(self) -> int: 
        return self.__item_count

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Array):
            return False
        return self.__elements==other.__elements and self.__data_type == other.__data_type
    def __iter__(self) -> Iterator[T]:
        return iter(self.__elements)

    def __reversed__(self) -> Iterator[T]:
        return reversed(self.__elements)

    def __delitem__(self, index: int) -> None:
        if index >= self.__item_count:
            raise IndexError("Out of Bounds")
        del self.__elements[index]
        self.__item_count -=1

    def __contains__(self, item: Any) -> bool:
        return item in self.__elements

    def clear(self) -> None:
        self.__elements.clear()
        self.__item_count=0

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__item_count}, Physical: {len(self.__elements)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
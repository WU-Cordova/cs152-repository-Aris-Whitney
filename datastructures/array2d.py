from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int, data_type:type) -> None:
            self.row_index=row_index
            self.array=array
            self.num_columns=num_columns
            self.data_type=data_type

        def __getitem__(self, column_index: int) -> T:
            if column_index < 0 or column_index >=self.num_columns:
                raise IndexError(f"column index {column_index} out of bounds for row {self.row_index}")
            index=self.map_index(self.row_index, column_index)
            return self.array[index]
        
        def __setitem__(self, column_index: int, value: T) -> None:
            if column_index < 0 or column_index >=self.num_columns:
                raise IndexError(f"column_index {column_index} out of bounds for row {self.row_index}")
            index=self.map_index(self.row_index, column_index)
            self.array[index]=value

        def map_index(self, row_index:int, column_index:int)->int:
            return row_index * self.num_columns + column_index
        
        def __iter__(self) -> Iterator[T]:
            for column_index in range(self.num_columns):
                yield self[column_index]
            #return iter(self.array[self.row_index])
        
        def __reversed__(self) -> Iterator[T]:
            for column_index in range(self.num_columns -1,-1,-1):
                yield self[column_index]
            #return reversed(self.array[self.row_index])
        def __len__(self) -> int:
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns - 1)])}, {str(self[self.num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        if not isinstance(starting_sequence, (list, tuple)):
            raise ValueError("Wanted a sequence of sequences for starting_sequence")
        for row in starting_sequence:
            if not isinstance(row, (list,tuple)):
                raise ValueError("All items in starting_sequence must be a sequence(list or tuple)")
            if not all(isinstance(item, data_type) for item in row):
                raise ValueError("All items must be of the same type")
        if starting_sequence:
            first_row_length=len(starting_sequence[0])
            for row in starting_sequence:
                if len(row) !=first_row_length:
                    raise ValueError("All rows in starting_sequence must have the same length")
        self.data_type=data_type
        self.row_len=len(starting_sequence)
        self.column_len=len(starting_sequence[0]) if starting_sequence else 0

        self.array2d=Array([data_type() for item in range(self.row_len * self.column_len)], data_type=data_type)
        index=0

        for row_index in range (self.row_len):
            for column_index in range(self.column_len):
                self.array2d[index]=starting_sequence[row_index][column_index]
                index +=1


    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        starting_sequence=[]
        for row in range(rows):
            starting_sequence.append([data_type() for _ in range(cols)])
            #for col in range(cols):
             #   starting_sequence[row].append(data_type())

        return Array2D(starting_sequence=starting_sequence, data_type=data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        return Array2D.Row(row_index, self.array2d, self.column_len, self.data_type)
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        for row_index in range(self.row_len):
            yield self[row_index]
        return (self[row_index] for row_index in range(self.row_len))
    
    def __reversed__(self):
        for row_index in range(self.row_len -1,-1,-1):
            yield self[row_index]
        #return reversed([self[row_index] for row_index in range (self.row_len)])
    
    def __len__(self): 
        return self.row_len
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.row_len} Rows x {self.column_len} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
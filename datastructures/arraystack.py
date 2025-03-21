import os

from datastructures.array import Array, T
from datastructures.istack import IStack

class ArrayStack(IStack[T]):
    ''' ArrayStack class that implements the IStack interface. The ArrayStack is a 
        fixed-size stack that uses an Array to store the items.'''
    
    def __init__(self, max_size: int = 0, data_type=object) -> None:
        ''' Constructor to initialize the stack 

            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> s.empty
                True
                >>> s.full
                False
                >>> s.maxsize
                5
        
            Arguments: 
                max_size: int -- The maximum size of the stack. 
                data_type: type -- The data type of the stack.       
        '''
        if max_size <=0:
            raise ValueError("max_size must be greater than 0")
        self._maxsize=max_size
        self.data_type=data_type
        starting_sequence=[self.data_type() for _ in range(max_size)]
        self.stack=Array(starting_sequence=starting_sequence, data_type=data_type)
        self._top=0




    def push(self, item: T) -> None:
        ''' Pushes an item onto the stack.
        
            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> s.push(1)
                >>> s.push(2)
                >>> s.push(3)
                >>> s.push(4)
                >>> s.push(5)
                >>> s.full
                True
                >>> print(repr(s))
                ArrayStack(5): items: [1, 2, 3, 4, 5]
                >>> s.push(6)
                IndexError('Stack is full')

            Arguments:
                item: T -- The item to push onto the stack.
        '''
        if self.full:
            raise IndexError("stack is full")
        self.stack[self._top]=item
        self._top += 1

    def pop(self) -> T:
        ''' Pops an item from the stack.

            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> s.push(1)
                >>> s.push(2)
                >>> s.push(3)
                >>> s.pop()
                3
                >>> s.pop()
                2
                >>> s.pop()
                1
                >>> s.empty
                True
                >>> print(repr(s))
                ArrayStack(5): items: []
                >>> s.pop()
                IndexError('Stack is empty')
        
            Returns:
                T -- The item popped from the stack.
        '''
        if self.empty:
            raise IndexError("stack is empty")
        self._top -=1
        #item=self.stack[self._top]
       # self.stack[self._top]=None
        return self.stack[self._top]

    def clear(self) -> None:
       ''' Clears the stack. 
       
           Examples:
               >>> s = ArrayStack(max_size=5, data_type=int)
               >>> s.push(1)
               >>> s.push(2)
               >>> s.push(3)
               >>> s.clear()
               >>> s.empty
               True
               >>> print(repr(s))
               ArrayStack(5): items: []
        '''
       default_value=self.data_type()
       self.stack=Array(starting_sequence=[default_value]*self._maxsize, data_type=self.data_type)
       self._top=0
    
    @property
    def peek(self) -> T:
        ''' Returns the top item on the stack without removing it.
        
            Returns:
                T -- The top item on the stack.

            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> s.push(1)
                >>> s.push(2)
                >>> s.push(3)
                >>> s.peek
                3
                >>> s.pop()
                3
                >>> s.peek
                2
                >>> s.pop()
                2
                >>> s.peek
                1
                >>> s.pop()
                1
                >>> s.empty
                True
                >>> s.peek
                IndexError('Stack is empty')
        '''
        if self.empty:
            raise IndexError("Stack is empty")
        return self.stack[self._top-1]
    

    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the stack. 

            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> s.maxsize
                5
        
            Returns:
                int: The maximum size of the stack.
        '''
        return self._maxsize    
    @property
    def full(self) -> bool:
        ''' Returns True if the stack is full, False otherwise. 

            Examples:

        
            Returns:
                bool: True if the stack is full, False otherwise.
        '''
        return self._top ==self._maxsize

    @property
    def empty(self) -> bool:
        ''' Returns True if the stack is empty, False otherwise. 

            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> s.empty
                True
                >>> s.push(1)
                >>> s.empty
                False
                >>> s.pop()
                1
                >>> s.empty
                True
        
            Returns:
                bool: True if the stack is empty, False otherwise.
        '''
        return self._top==0
    
    def __eq__(self, other: object) -> bool:
        ''' Compares two stacks for equality.

            Examples:
                >>> s1 = ArrayStack(max_size=5, data_type=int)
                >>> s2 = ArrayStack(max_size=5, data_type=int)
                >>> s1 == s2
                True
                >>> s1.push(1)
                >>> s1 == s2
                False
                >>> s2.push(1)
                >>> s1 == s2
                True
                >>> s1.push(2)
                >>> s2.push(3)
                >>> s1 == s2
                False
        
            Arguments:
                other: object -- The other stack to compare.
                
            Returns:
                bool -- True if the stacks are equal, False otherwise.
        '''
        if not isinstance(other, ArrayStack):
            return False
        return self.stack == other.stack and self._top ==other._top

    def __len__(self) -> int:
        ''' Returns the number of items in the stack.

            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> len(s)
                0
                >>> s.push(1)
                >>> len(s)
                1
                >>> s.push(2)
                >>> len(s)
                2
                >>> s.pop()
                2
                >>> len(s)
                1
                >>> s.pop()
                1
                >>> len(s)
                0
        
            Returns:
                int -- The number of items in the stack.
        '''
        return self._top
    
    def __contains__(self, item: T) -> bool:
        ''' Returns True if the item is in the stack, False otherwise.
        
            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> s.push(1)
                >>> s.push(2)
                >>> s.push(3)
                >>> 1 in s
                True
                >>> 2 in s
                True
                >>> 3 in s
                True
                >>> 4 in s
                False
                >>> 5 in s
                False
            
            Arguments:
                item: T -- The item to search for.
                
            Returns:
                bool -- True if the item is in the stack, False otherwise.
        '''
        for i in range(self._top):
            if self.stack[i] ==item:
                return True
        return False

    def __str__(self) -> str:
        ''' Returns a string representation of the stack.

            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> s.push(1)
                >>> s.push(2)
                >>> s.push(3)
                >>> print(s)
                [1, 2, 3]
        
            Returns:
                str -- A string representation of the stack.
        '''
        return str([self.stack[i] for i in range(self._top)])
    
    def __repr__(self) -> str:
        ''' Returns a string representation of the stack.

            Examples:
                >>> s = ArrayStack(max_size=5, data_type=int)
                >>> s.push(1)
                >>> s.push(2)
                >>> s.push(3)
                >>> repr(s)
                'ArrayStack(5): items: [1, 2, 3]'
        
            Returns:
                str -- A string representation of the stack.
        '''
        return f"ArrayStack({self.maxsize}): items: {str(self)}"
    
if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')


import sys
import os
import random
import time
import copy
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from typing import List
from datastructures.array2d import Array2D
from time import sleep

if os.name == 'nt':
    import msvcrt
# Posix (Linux, OS X)
else:
    import sys
    import termios
    import atexit
    from select import select

class KBHit:
    def __init__(self):
        '''Creates a KBHit object that you can call to do various keyboard things.'''
        if os.name == 'nt':
            pass
        else:
            # Save the terminal settings
            self.fd = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.fd)
            self.old_term = termios.tcgetattr(self.fd)
            # New terminal setting unbuffered
            self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)
            # Support normal-terminal reset at exit
            atexit.register(self.set_normal_term)

    def set_normal_term(self):
        '''Resets to normal terminal. On Windows, this is a no-op.'''
        if os.name == 'nt':
            pass
        else:
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)

    def getch(self):
        '''Returns a keyboard character after kbhit() has been called.
        Should not be called in the same program as getarrow().'''
        s = ''
        if os.name == 'nt':
            return msvcrt.getch().decode('utf-8')
        else:
            return sys.stdin.read(1)

    def getarrow(self):
        '''Returns an arrow-key code after kbhit() has been called. Codes are
        0 : up
        1 : right
        2 : down
        3 : left
        Should not be called in the same program as getch().'''
        if os.name == 'nt':
            msvcrt.getch()  # skip 0xE0
            c = msvcrt.getch()
            vals = [72, 77, 80, 75]
        else:
            c = sys.stdin.read(3)[2]
            vals = [65, 67, 66, 68]
        return vals.index(ord(c.decode('utf-8')))

    def kbhit(self):
        '''Returns True if keyboard character was hit, False otherwise.'''
        if os.name == 'nt':
            return msvcrt.kbhit()
        else:
            dr, dw, de = select([sys.stdin], [], [], 0)
            return dr != []



class Cell:
    def __init__(self, alive=False):
        self.alive=alive

    def __repr__(self):
        return "🦠" if self.alive else " "

    def is_alive(self)-> bool:
        return self.alive

class Grid():
    def __init__(self, rows, cols):
        self.grid=Array2D.empty(rows, cols, Cell)
        self.rows=rows
        self.cols=cols
        if self.grid is None or len(self.grid) != rows or len(self.grid[0]) !=cols:
            raise ValueError("Grid intialization falied. Check Grid size or Array2D class")

    def __getitem__(self, pos):
        row, col=pos
        return self.grid[row][col]
    
    def __setitem__(self, pos, cell):
        row, col=pos
        self.grid[row][col]=cell

    def get_neighbors(self, row: int, col: int) -> int:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        neighbors = 0
        for direction in directions:
            r, c = row + direction[0], col + direction[1]
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if self.grid[r][c].is_alive():
                    neighbors += 1
        return neighbors
    
    def num_alive(self):
        alive_count=0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col].is_alive():
                    alive_count +=1
        return alive_count
    
    def __eq__(self,other)->bool:
        if not isinstance(other, Grid):
            return False
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] != other.grid[row][col]:
                    return False
        return True


    def __str__(self):
        return "\n".join(["".join([str(self.grid[row][col]) for col in range(self.cols)]) for row in range(self.rows)])
    
    def clear(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col].alive=False

    def randomize(self, percent_alive=50):
        for row in range(self.rows):
            for col in range(self.cols):
                if random.randint(0,100) < percent_alive:
                    self.grid[row][col].alive= True
                else:
                    self.grid[row][col].alive=False

class GameController:
    def __init__(self, rows:int, cols:int, mode="auto", history_size=5):
        self.rows=rows
        self.cols=cols
        self.mode=mode
        self.grid=Grid(rows, cols)
        self.history=[]
        self.history_size=history_size
        self.kb=KBHit()

    def display_grid(self):
        print(self.grid)
        print("\n")

    def next_generation(self):
        new_grid = Grid(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                neighbors = self.grid.get_neighbors(row, col)
                if self.grid[row,col].is_alive():
                    if neighbors < 2 or neighbors > 3:
                        new_grid[row,col].alive=False 
                elif neighbors == 3:
                    new_grid[row, col].alive=True  
        return new_grid
    
    def check_stability(self):
        return self.grid==self.history[-1] if len(self.history) > 0 else False
    
    def run_auto(self):
        while True:
            self.display_grid()
            if self.check_stability():
                print("The colony Has Stabilized :)")
                break
            self.history.append(copy.deepcopy(self.grid))
            if len(self.history)> self.history_size:
                self.history.pop(0)

            self.grid=self.next_generation() #goes to the next gen
            time.sleep(1)

    def run_manual(self):
        print("Press 'm' to toggle manual mode.")
        print("Press 'a' to switch to auto mode.")
        print("Press 'q' to quit.")
        while True:
            self.display_grid()
            if self.check_stability():
                print("The Colony Has Stabilized :)")
                break
            if self.kb.kbhit():
                key=self.kb.getch()
                if key.lower() == 'm':
                    self.mode="manual"
                    return
                elif key.lower() =='a':
                    self.mode="auto"
                    return
                elif key.lower() == 'q':
                    print("Leaving The Game")
                    return
            self.grid=self.next_generation() #goes to next gen
            time.sleep(1)
    def set_mode(self):
        if self.mode=="auto":
            return self.run_auto()
        elif self.mode == "manual":
            return self.run_manual()
    def run(self):
        while True:
            if self.mode=="auto":
                self.run_auto()
            elif self.mode =="manual":
                self.run_manual()
            else:
                print("invalid mode")
                break



    

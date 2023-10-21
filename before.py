import numpy as np
import json
import os

class Class_B:
    pass

class Class_A:
    def __init__(self) -> None:
        self.val_3 = 3
        self.val_1 = 1
        self.val_2 = 2

    def __str__(self) -> str:
        return f'[{self.val_1}, {self.val_2}, {self.val_3}]'
    
    def print_current_dir(self):
        this_dir = os.path.abspath('.')
        print(this_dir)

    def add_1_to_vals(self):
        self.val_1 += 1
        self.val_2 += 1
        self.val_3 += 1

def main():
    obj_2 = Class_B()
    obj_1 = Class_A()
    print(obj_1)
    obj_1.add_1_to_vals()
    print(obj_1)

if __name__ == '__main__':
    main()
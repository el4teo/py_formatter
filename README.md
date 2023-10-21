**CONTENT**

- [Description](#description)
  - [Guidelines](#guidelines)
- [Pactical example](#pactical-example)
  - [Before](#before)
  - [After](#after)
- [TODO](#todo)

# Description

A python script that improves the code organization of other python scripts

## Guidelines

- The begining of the script, before the first `class` or `def`, will not be changed
- Classes and functions on the same level will be alphabetically sorted
- In case of classes:
  - The sort method will call to itsel with the content of the class
  - The funcitons within the class will be alphabetically sorted too
- In case of funtions (defined with `def`):
  - Their content will remain the same (the order is inportant there)

# Pactical example

## Before

~~~ python
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
~~~

## After

~~~ python
import numpy as np
import json
import os

class Class_A:
    def __init__(self) -> None:
        self.val_3 = 3
        self.val_1 = 1
        self.val_2 = 2

    def __str__(self) -> str:
        return f'[{self.val_1}, {self.val_2}, {self.val_3}]'
    
    def add_1_to_vals(self):
        self.val_1 += 1
        self.val_2 += 1
        self.val_3 += 1

    def print_current_dir(self):
        this_dir = os.path.abspath('.')
        print(this_dir)

class Class_B:
    pass

def main():
    obj_2 = Class_B()
    obj_1 = Class_A()
    print(obj_1)
    obj_1.add_1_to_vals()
    print(obj_1)

if __name__ == '__main__':
    main()
~~~

# TODO

A lot of improvements can be done, here you have a list of the main ones:

- [ ] Print status of the progress
- Function `FomratApplier.split_code`
  - [ ] Decorators as part of the section below them
  - [ ] Add new keywords, for exampe `if` and `import`
  - [ ] End a section when a new line with lower tab level is found
- Format improvement
  - [ ] Lines with only spaces -> ''
  - [ ] Two or more consecutive empty lines -> save only one

#!/usr/bin/env python3

import sys
sys.path.append('.')

from app.conversion import as_int

# exported function
def add(a, b):
    return as_int(a) + as_int(b)

if __name__ == '__main__':
    assert add('1', '1') == 2
    print('Test passed.')
#!/usr/bin/env python3

# exported function
def as_int(a):
    return int(a)

if __name__ == '__main__':
    assert as_int('1') == 1
    print('Test passed.')
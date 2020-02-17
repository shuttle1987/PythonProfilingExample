from sorting import bogo
from random import shuffle

if __name__ == '__main__':
    ordered = [1, 2, 3, 4, 5]

    bogo(ordered)

    ints = list(range(10))
    shuffle(ints)
    bogo(ints)

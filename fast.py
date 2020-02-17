from sorting import default_sort
from random import shuffle

if __name__ == '__main__':
    # See perf of sorting and already ordered collection
    ordered = list(range(10))
    default_sort(ordered)

    # See perf of sorting random ordered collection
    ints = list(range(10))
    shuffle(ints)
    default_sort(ints)

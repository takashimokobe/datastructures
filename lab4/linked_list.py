# a linked list is one of
# None, or
# an object Pair

class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def __eq__(self, other):
        return ((type(other) == Pair)
                and self.first == other.first
                and self.rest == other.rest
                )

    def __repr__(self):
        return ("Pair({!r}, {!r})".format(self.value, self.rest))

class Iterator:
    def __init__(self, llist):
        self.llist = llist

    def __eq__(self, other):
        return ((type(other) == Iterator)
                and self.llist == other.llist
                )

    def __repr__(self):
        return ("Iterator({!r})".format(self.llist))

# linked list -> Iterator(list)
# takes a linked list and returns a iterator
def object_iterator(llist):
    return Iterator(llist)

# iterator -> boolean
# takes a Iterator and returns True if there is another value to return from the iterated list
def has_next(iterator):
    if (iterator.llist == None):
        return False
    else:
        return True

# iterator -> alist.next
# takes in a iterator and returns the next value in the iteration sequence,
# if no remaining values, a StopIterator exception should be raised
def next(iterator):
    if has_next(iterator) == True:
        value = iterator.llist.first
        iterator.llist = iterator.llist.rest
        return value
    else:
        raise StopIteration

# linkedlist -> yield each value in list
def yield_iterator(llist):
    if llist is not None:
        yield llist.first
        yield from yield_iterator(llist.rest)
    else:
        raise StopIteration()

# no arguments -> None
# takes in 0 arguments, and returns an empty list
def empty_list():
    return None

# list int value -> list
# puts the value at the index specified in your list
def add(llist, index, value):
    if (index < 0 or index > length(llist)):
        raise IndexError
    if (index == 0 and list == None):
        return Pair(value, None)
    elif (index == 0):
        return Pair(value, llist)
    else:
        return Pair(llist.first, add(llist.rest, index  -1 , value))

# list -> int
# returns the number of elements in your lsit
def length(llist):
    if (llist == None):
        return 0
    else:
        return 1 + length(llist.rest)

# list int -> value
# returns the value at the index position in the list
def get(llist, index):
    if (llist is None or index < 0):
        raise IndexError
    else:
        if (index == 0):
            return llist.first
        else:
            return get(llist.rest, index - 1)

# list int value -> list
# replaces the element at the index position with the given value.
def set(llist, index, value):
    if (index < 0 or llist is None):
        raise IndexError
    if (index == 0):
        return Pair(value, llist.rest)
    else:
        return Pair(llist.first, set(llist.rest, index - 1, value))

# list int -> list
# removes the element at the given index of the list
def removing(llist, index):
    if (index < 0 or index > length(llist)):
        raise IndexError
    elif (index == 0):
        return llist.rest
    else:
        return Pair(llist.first, removing(llist.rest, index - 1))

# list int -> tuple
# returns a 2-tuple with {element before(removed element} and the resulting list.
def remove(llist, index):
    if (index < 0 or index > length(llist)):
        raise IndexError
    else:
        return (get(llist, index), removing(llist, index))


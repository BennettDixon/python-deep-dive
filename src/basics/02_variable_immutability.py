# Immutability in python applies to int, float, bool, str, tuple, and frozenset.

# When you create an object of these types, you cannot change its value in memory.
# If you try to change it, what actually happens is that a new object is created and
# the reference is updated to point to this new object.

# This behavior is contrasted with mutable types like list, dict, and set, where you can change the
# contents of the object in place without creating a new object.
# For instance, appending an item to a list changes the list itself, rather than creating a new list.

def show_integer_immutability():
    print("---Integer immutability---")
    a = 1
    b = a
    print("a = ", a)
    print("b = ", b)
    print("id(a) = ", id(a))
    print("id(b) = ", id(b))
    print("a == b: ", a == b)
    print("a is b: ", a is b)
    print("----now update b, a should not change even though it is a reference----")
    print("this is because integers are immutable in python and a new copy is created")
    b += 1
    print("a = ", a)
    print("b = ", b)
    print("id(a) = ", id(a))
    print("id(b) = ", id(b))
    print("a == b: ", a == b)
    print("a is b: ", a is b)
    print("----")


def show_tuple_immutability():
    print()
    print("---Tuple immutability---")
    a = (1, 2, 3)
    b = a
    print("a = ", a)
    print("b = ", b)
    print("id(a) = ", id(a))
    print("id(b) = ", id(b))
    print("a is b: ", a is b)
    b = b + (4,)
    print("----now update b, a should not change----")
    print("a = ", a)
    print("b = ", b)
    print("id(a) = ", id(a))
    print("id(b) = ", id(b))
    print("a is b: ", a is b)


if __name__ == "__main__":
    show_integer_immutability()
    show_tuple_immutability()

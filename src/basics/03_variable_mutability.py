# Immutability in python applies to int, float, bool, str, tuple, and frozenset.

# When you create an object of these types, you cannot change its value in memory.
# If you try to change it, what actually happens is that a new object is created and
# the reference is updated to point to this new object.

# This behavior is contrasted with mutable types like list, dict, and set, where you can change the
# contents of the object in place without creating a new object.
# For instance, appending an item to a list changes the list itself, rather than creating a new list.

# Now we will show how mutability works (compared to immutability in src/basics/02_variable_immutability.py)

# Lists are mutable, meaning references will also change if the list is changed.
def show_list_mutability(l):
    my_new_list = l
    print("current passed list: ", l)
    print("current my_new_list: ", my_new_list)
    print("id(l): ", id(l))
    print("id(my_new_list): ", id(my_new_list))
    print("l is my_new_list: ", l is my_new_list)
    print("----now update my_new_list, l should also change----")
    print("this is because lists are mutable in python and the same reference is used")
    my_new_list.append(4)
    print("l: ", l)
    print("my_new_list: ", my_new_list)
    print("id(l): ", id(l))
    print("id(my_new_list): ", id(my_new_list))
    print("l is my_new_list: ", l is my_new_list)
    print("----")

# Instead if we copy the list, we can change the copy without changing the original.


def list_copy_reference(l):
    my_new_list = l.copy()
    print("current passed list: ", l)
    print("current my_new_list: ", my_new_list)
    print("id(l): ", id(l))
    print("id(my_new_list): ", id(my_new_list))
    print("l is my_new_list: ", l is my_new_list)
    print("----now update my_new_list, l should not change----")
    print("this is because lists are mutable in python and the same reference is used, but we copied the list")
    print("this is not a deep copy, so if the list contains mutable objects, they will still be references")
    my_new_list.append(4)
    print("l: ", l)
    print("my_new_list: ", my_new_list)
    print("id(l): ", id(l))
    print("id(my_new_list): ", id(my_new_list))
    print("l is my_new_list: ", l is my_new_list)
    print("----")


if __name__ == "__main__":
    print("---List mutability---")
    my_list = [1, 2, 3]
    print("my_list pre pass by reference append: ", my_list)
    show_list_mutability(my_list)
    print("my_list post pass by reference append (should be appended to): ", my_list)
    print()
    print()
    print("-------------------------")
    print()
    print()
    print("---List copy reference---")
    my_list = [1, 2, 3]
    print("my_list pre pass by reference append: ", my_list)
    list_copy_reference(my_list)
    print("my_list post pass by reference append (should be same): ", my_list)

# Immutability in python applies to int, float, bool, str, tuple, and frozenset.

# When you create an object of these types, you cannot change its value in memory.
# If you try to change it, what actually happens is that a new object is created and
# the reference is updated to point to this new object.

# This behavior is contrasted with mutable types like list, dict, and set, where you can change the
# contents of the object in place without creating a new object.
# For instance, appending an item to a list changes the list itself, rather than creating a new list.

# Now we will show how mutability works (compared to immutability in src/basics/02_variable_immutability.py)

# In the prior example we showed how lists are mutable, meaning references will also change if the list is changed.
# However we used mutable objects in the list, so we will show how side effects can happen if we are not careful.
import copy


def shallow_copy_list(l: list) -> list:
    return l.copy()


def deep_copy_list(l: list) -> list:
    return copy.deepcopy(l)


if __name__ == "__main__":
    # Here we use mutable objects (dictionaries) in the list.
    my_list = [{"value": 1}, {"value": 2}, {"value": 3}]
    my_list_copy = shallow_copy_list(my_list)
    print("my_list: ", my_list)
    print("my_list_copy: ", my_list_copy)
    print("--appended {\"value\": 4} to my_list_copy--")
    my_list_copy.append({"value": 4})
    print("my_list: ", my_list)
    print("my_list_copy: ", my_list_copy)
    print("as you can see my_list_copy is now different than my_list since they are shallow copies")
    print("----")
    print("However, once we change the value of the dictionary, it will change in both lists")
    print("This is because the objects in the list are still references to the same objects")
    my_list_copy[0]["value"] = 5
    print("my_list: ", my_list)
    print("my_list_copy: ", my_list_copy)
    print("Notice how both lists have propogated the change of value to 5 for the first dictionary.")

    print("----")
    print("Now we will show how deep copying can help with this issue")
    my_list = [{"value": 1}, {"value": 2}, {"value": 3}]
    my_list_copy = deep_copy_list(my_list)
    print("my_list: ", my_list)
    print("my_list_copy: ", my_list_copy)
    print("--appended {\"value\": 4} to my_list_copy--")
    my_list_copy.append({"value": 4})
    print("my_list: ", my_list)
    print("my_list_copy: ", my_list_copy)
    print("as you can see my_list_copy is still different since it is a copy")
    print("----")
    my_list_copy[0]["value"] = 5
    print("However when we update one of the dictionaries in the list, it will not propogate to the other list.")
    print("This is because we deep copied this list, so the dictionaries are also deep copied and not just references.")
    print("my_list: ", my_list)
    print("my_list_copy: ", my_list_copy)

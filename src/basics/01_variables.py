
if __name__ == "__main__":
    my_num = 3
    my_float = 3.14
    my_string = "Hello World!"
    my_bool = True
    print(my_num)
    print(my_float)
    print(my_string)
    print(my_bool)
    print("----Variable references----")

    # References in python
    reference_of_my_float = my_float
    print("my_float and _reference_of_my_float will have same memory address")
    print(id(my_float))
    print(id(reference_of_my_float))
    assert id(my_float) == id(reference_of_my_float)
    my_float = 3.15
    print("my_float and _reference_of_my_float will have different memory address")
    print(id(my_float))
    print(id(reference_of_my_float))
    assert id(my_float) != id(reference_of_my_float)
    print("----String references & interning of literals----")
    reference_of_my_string = "Hello World!"
    reference_of_both_strings = reference_of_my_string
    print("my_string and _reference_of_my_string will have same memory address,")
    print(" since they reference same string literal. Same with an actual reference for them.")
    print("This is due to interning in python.")
    print("Python interns common strings and other things like small integers to save memory.")
    print(id(my_string))
    print(id(reference_of_my_string))
    print(id(reference_of_both_strings))
    assert id(my_string) == id(reference_of_my_string)

    print("----Interning can apply to other types too----")
    my_new_num = 3
    my_new_second_num = 3
    print("my_new_num and my_new_second_num will have same memory address,")
    print("since they reference an interned integer (-5:256).")
    print(id(my_new_num))
    print(id(my_new_second_num))
    assert id(my_new_num) == id(my_new_second_num)

    print("---Reserved keywords---")
    print("following are reserved keywords:")
    help("keywords")

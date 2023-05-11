# # # # single line comment, I will not be interpreted

# # # # i am a 
# # # # mulitline
# # # # comment

# # # """
# # # this is a python docstring, it is used 
# # # to document modules, funcitons
# # # classes, methods
# # # etc.
# # # """

# # # # python 'snake_case' to define varaibles
# # # my_variable = "some string value 🐍"

# # # print(my_variable)

# # # # shouting snake case = const (do not change)
# # # # coding convention, not a language feature
# # # MY_CONSTANT = "dont change me"

# # # # whitespace and functions/scope-ish type thing (loops, functions, classes, conditional logic)
# # # # def keyword starts a funciton
# # # # : means codeblock starting
# # # def compliment_machine(name):
# # #     # this indentation indicates that i am in the funciton
# # #     # print("hey, " + name + " looking good today. Did you get a haircut?")
# # #     # format string = template string literal/string interpolation
# # #     print(f"hey, {name} looking good today. Did you get a haircut?")
# # #     # everything that is indeneted is in this funciton

# # # # not in function anymore
# # # compliment_machine("Gabe") # invocation of the function
# # # compliment_machine("Anthony")

# # # def function_stub_third_word():
# # #     pass # tells python to skip this indentation block

# def adding_machine(num_one, num_two):
#     # print(num_one + num_two)
#     return num_one + num_two


# # value = adding_machine(10, 15)
# # print("what is the value?", value)

# # # ## # ## # ## # ## 
# # # DATA TYPES

# # # Bools
# # None # implicit and explicit lack of value (falsy)
# # False # explicit falsyness
# # True # explicit truthyness

# # # Strings -- chars text
# # "double quotes are cool"
# # 'as are single quotes'

# # # Numeric types
# # # int -- whole number integers
# # 10
# # 45
# # 116
# # # float -- decimal numbers
# # 3.1415
# # 89.2
# # .001
# # # complex numbers (used infrequently unless you are going hard on the math)
# # 10j
# # 3.5j

# print(type(10))
# print(type(3.7))


# # Data contianers (aka reference types)
# # lists -- (arrays)
# # googleable key term
# # python3 list methods
# my_list = ['hello', 'spam', 'eggs', 'bacon', 'sausage']

# # dictionarys
# my_dict = {
#     "key": "value",
#     "fruits": ['mango', 'banana'],
#     10: "hello",
#     False: True,
#     None: "wtf python",
#     "a_list": my_list
# }

# my_list[0] = "spam" 
# print(my_list)
# my_dict["key"] = "new value"
# print(my_dict["a_list"])

# del my_dict["a_list"]

# print(my_dict)

# print(dir("hello"))


# my_string = "spam"
# print(my_string.capitalize())

# # ## # ## # ## # ## 
# # Control Flow

# my_breakfast = ['spam', 'eggs', 'bacon', 'sausage']
# like_spam = True

# # logical operaters
# # and -- &&
# # or -- ||
# # not  -- ! 
# # in -- check if contains

# # if "spam" in my_breakfast and not like_spam:
# #     # indentation required
# #     print("but I don't like spam!")
# # elif "eggs" in my_breakfast:
# #     print("bleeeeech")
# # else:
# #     print("yum")

# # ## # ## # ## # ## 
# # Data Containers and iteration

# # simple iteration syntax works on all iterables
# # for taco in my_breakfast:
# #     print(taco)

# # for key in my_dict:
# #     print(f"{key}: {my_dict[key]}")

# # most similar to a traditional for loop
# for i in range(len(my_breakfast)):
#     print(my_breakfast[i])

# # while
# i = 0
# while i < len(my_breakfast):
#     print(my_breakfast[i])
#     # you have to increment
#     i += 1

# ## # ## # ## # ## 
# Scope

my_value = "sausage"

def my_function():
    # pluck a variable from the global scope and 
    # make it modifyable here
    global my_value
    print("inside function:",  my_value)
    my_value += " " + "eggs"
    in_function = "hello"
    def inside():
        # nonlocal plucks from a scope above that is not global
        nonlocal in_function
        in_function += " " + "spam"
    
    inside()

my_function()
print(my_value)



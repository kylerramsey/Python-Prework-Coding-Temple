# Question 1 : Write a function to print "hello_USERNAME!"
def hello_name(user_name):
    print(f"Hello {user_name}!")


hello_name(input("What's your name?: "))
print("\n")


# Question 2 : Write a python function, first_odds that prints the odd numbers from 1-100
# and returns nothing
def first_odds():
    for x in range(1, 100):
        if x % 2 != 0:
            print(x, end=" ")


first_odds()
print("\n")


# Question 3 : Please write a Python function, max_num_in_list
# to return the max number of a given list.
def max_num_in_list(a_list):
    print(max(a_list))


max_num_in_list([1, 5, 300, 52, 45, 64, 224])
print("\n")


# Question 4 : Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0 or a_year == 0:
        return True
    else:
        return False


print(is_leap_year(2024))
print("\n")


# Question 5 : Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type.

def is_consecutive(input_list):
    for index, value in enumerate(input_list[:-1]):
        if value + 1 != input_list[index + 1]:
            return False
    return True


print(is_consecutive([1, 2, 3]))

print(is_consecutive([1, 2, 4]))
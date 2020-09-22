# Consider comparisons with "in" to check if a variable is equal to one of many values,
# combine the values into a tuple and check if the variable is contained "in" it
# instead of checking for equality against each of the values.
# This is faster and less verbose.

value = 10
value_to_compare_1 = 10
value_to_compare_2 = 20
print(value in (value_to_compare_1, value_to_compare_2))

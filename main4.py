
# Ex4 - String 
# We have text = "3 4 5 6"
# Q1 - display number 1 by one without space
# Q2 - Sum all number (Total: 18)



# Q1 - Display numbers one by one without spaces
text = "3 4 5 6"
numbers = text.split()
for number in numbers:
    print(number, end="")


# Q2 - Sum all numbers
text = "3 4 5 6"
numbers = text.split()
total_sum = sum(int(number) for number in numbers)
print(total_sum)
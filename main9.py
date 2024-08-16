
# Ex9 - String
# We have string = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"
# Q2 - Multiple each letter by 2 result = "6 8 10 12"

# Q1 - Remove spaces
text = "3 4 5 6"
numbers = text.split()
for number in numbers:
    print(number, end="")

# Q2 - Multiply each number by 2

text = "3 4 5 6"
total=""
for i in range(len(text)):
    if text[i] != " ":
        total+=str(int(text[i])*2)+" "
print(total)
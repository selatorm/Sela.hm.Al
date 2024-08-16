# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0
# numbers = []

numbers = ""
for i in range(5):
    n=input()
    numbers+=str(n)
    max_number=numbers
    min_number=numbers
    for i in range (len(numbers)):
        if numbers[i]>max_number:
            max_number=numbers[i]
        elif numbers[i]<min_number:
            min_number=numbers[i]
print("max",max_number)
print("min",min_number)

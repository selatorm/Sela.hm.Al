# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text
# Q2 - Sum all number 
# Q3 - Sum only even number 
# Q4 - Reverse 




# Q1 - Count odd and even numbers
text = "454639"
odd=0
even=0
for i in range(len(text)):
    if int(text[i]) % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even number: ", even)
print("Odd number: ", odd)

# Q2 - Sum all numbers
text = "454639"
total_sum = sum(int(c) for c in text)
print(total_sum)

# Q3 - Sum only even numbers
text = "454639"
even_sum = sum(int(c) for c in text if int(c) % 2 == 0)
print(even_sum)

# # Q4 - Reverse

text = "454639"
index= len(text)-1
result=""
for i in range(len(text)):
    result+=text[index-i]
print(result)


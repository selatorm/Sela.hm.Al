# Ex3 - String
# Enter text and check if it contains capital letter or not
# Display "Yes" if capital
# display "No" if all lowercase letter

text = input("Enter text: ")
has_capital = text
# any(c.isupper() for c in text)
if has_capital:
    print("yes")
else:
    print("No")

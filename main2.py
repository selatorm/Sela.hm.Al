# Ex2 - String
# Enter text and display number of letter
# solve1
letter_count = sum(c.isalpha() for c in text)
print(f"Number of letters: {letter_count}")
text = input("Enter text: ")

# solve2
text=input("Enter your text: ")
print(len(text))
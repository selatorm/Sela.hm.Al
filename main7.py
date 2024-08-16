# Ex7 - number
# Enter number in range 10 - 20 until you enter other number out of range
# display "Continue" if number in range 10 - 20
# display "Out of range" if number difference from range 10 - 20

while True:
    number = int(input("Enter a number (10-20): "))
    if 10 <= number <= 20:
        print("Continue")
    else:
        print("Out of range")
        break
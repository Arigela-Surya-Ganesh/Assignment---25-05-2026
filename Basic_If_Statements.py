                            #Basic If Statements
# 1. Check whether a number is positive.
pos = int(input("Please enter a number\n"))
if pos>=0:
    print("Given number is Positive")

# 2. Check whether a number is negative.
neg = int(input("Please enter a number\n"))
if neg<0:
    print("Given number is Negative")

# 3. Check whether a number is zero.
num = int(input("please enter a number"))
if num == 0:
    print("The given number is Zero")

# 4. Check whether a number is even.
eve = int(input("Please enter a number\n"))
if eve%2==0:
    print("Given number is Positive")

# 5. Check whether a number is odd.
odo = int(input("Please enter a number\n"))
if odo%2==0:
    print("Given number is Negative")

# 6. Check whether a person is eligible to vote (18+).
age = int(input("Please enter your age correctly in numbers"))
if age >= 18:
    print("You are elgible to vote")

# 7. Check whether a student passed (marks ≥ 35).
marks = int(input("Please enter your marks"))
if marks >=35:
    print("Mr.X paased all exams")

# 8. Check whether a number is divisible by 5.
dig = int(input("Please enter a number"))
if dig%5==0:
    print("Given number is divisble by 5")

# 9. Check whether a number is divisible by 10.
dig = int(input("Please enter a number"))
if dig%10==0:
    print("Given  number is divisble by 10")

# 10. Check whether a character is a vowel.
vow = ['a','e','i','o','u','A','E','I','O','U]
checkVow = input("Please enter a char")

if checkVow in vow:
    print("Entered char is Vowel")
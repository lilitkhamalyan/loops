i = 0
# Get the number from the user
number = int(input("Enter a number from 1 to 20: "))

# Number should be [1, 20]
while not number in range (1, 21):
    number = int(input("Error! Enter a number from 1 to 20: "))

# i < number, print i^2
while (i < number):
    print(i ** 2)
    i = i + 1



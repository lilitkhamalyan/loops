i = 0
number = int(input("Enter a number from 1 to 20: "))

while not number in range (1, 21):
    number = int(input("Error! Enter a number from 1 to 20: "))
    
while (i < number):
    print(i ** 2)
    i = i + 1



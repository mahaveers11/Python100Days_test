# fruits = ["apple","peach","pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
#
# print("#######this is outside loop now######")
# print(fruits)


# student_scores = [120, 130, 145, 154, 122, 143, 152, 111, 128,176]
# max = 0
# for score in student_scores:
#     if score > max:
#         max = score
#     # else:
#
# print(f"this is the maximum score: {max}")
# total = 0
# for number in range(1, 101):
#     total += number
#
# print(total)


# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuss")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# password = ""
#
# for letter in range(1, nr_letters+1):
#     # random_letter = random.choice(letters)
#     password += random.choice(letters)
#
# for letter in range(1, nr_numbers+1):
#     # random_letter = random.choice(letters)
#     password += random.choice(numbers)
#
# for letter in range(1, nr_symbols+1):
#     # random_letter = random.choice(letters)
#     password += random.choice(symbols)
#
# print(password)

password_list = []

for letter in range(1, nr_letters+1):
    # random_letter = random.choice(letters)
    password_list.append(random.choice(letters))

for letter in range(1, nr_numbers+1):
    # random_letter = random.choice(letters)
    password_list.append(random.choice(numbers))

for letter in range(1, nr_symbols+1):
    # random_letter = random.choice(letters)
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print()
print("--------------- After Shuffle-----------------")
print(password_list)

#convert the list to a full string of the password
final_password=""

for char in password_list:
    final_password += char
print()
print("----------Final Password---------------")
print(final_password)






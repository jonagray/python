
friends = ["Bob", "Jake", "Larry", "Blazey", "Stirfry"]
first = 1
# print(friends[1:5])
for name in range(1, len(friends)):
    print(friends[name])
    print(friends[first])

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# secret_word = "bonk"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#       guess = input("Enter guess:")
#       guess_count += 1
#     else:
#        out_of_guesses = True
# if out_of_guesses:
#    print("Out of guesses - you lose!")
# else:
#    print("You win!")

# for letter in "Bonkey Monkey":
#     print(letter)

# for name in range(len(friends)):
#     print(friends[name])

# def translate(phrase):
#     phrase = phrase.lower()
#     translation = ""
#     for letter in phrase:
#         if letter in "aeiou":
#             translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation

# print(translate(input("Enter a phrase")))

# map_file = open("map1.txt", "w")

# # print(map_file.readlines()[1])
# map_file.write("\nUrmom")

# map_file.close()

# import useful_tools

# print(useful_tools.get_file_ext("getrekt.html"))

# from Student import Student
# from ExchangeStudent import ExchangeStudent

# student1 = Student("Frank", "Business", 3.8, False)
# student2 = ExchangeStudent("Chinese")

# # print(student1.gpa)

# print(student1.on_honor_roll())
# print(student2.foreign_language())
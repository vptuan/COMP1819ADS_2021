n = int(input("Number of staircases: "))

number_of_chars = ""
for i in range(0, n):
    spaces = ""
    for j in range(n - i):
        spaces += " "
    number_of_chars += "#"
    staircase = spaces + number_of_chars
    print(staircase)


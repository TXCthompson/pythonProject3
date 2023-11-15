###1#########################################################

print("Programming", "Essential", "in", sep="***", end='...')
print("Python")

###2#########################################################

arrow = ["    *    ",
         "  *   *  ",
         "*       *",
         "***   ***",
         "  *   *  ",
         "  *   *  ",
         "  *****  "]

for x in arrow:
    print(x)

###3###########################################################

print("I'm student")

###4###########################################################

print('"I\'m"', '""learning""', '"""Python"""', sep='\n')

###5-6#########################################################

number_one = "500"
number_two = "777"

number_one = int(number_one, 8)
number_two = int(number_two, 16)

print(f'number one = {number_one}, number two = {number_two}')

import pyfiglet

name = input("Enter your name: ")

result = pyfiglet.figlet_format(name, font="slant")

print(result)

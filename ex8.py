# to use json
import json
# to use sys.argv
import sys
# to use for a random password generator
import random

# empty dict
passwords = {}
# instructions() function to see how u can use this program and what facility has
def instructions(command):
        print("""
    You need to use as commands "gen" or "show" + argument like(website the key of passwords) from bash!

    You can use this program for :  - Generate a random password for a website and save it in a dictionary
                                    - Search a password by key(website)
                                    - Have a document with all passwords and websites saved in your PC. """)

 
# read() function to read the dict first of all
def read():
    with open("withstatement.txt", "r+") as r:
        content2 = json.loads(r.read())
        return content2

# gen() function to generate password with 2 inputs: website,lenght & write/save json file in dict
def gen(website):
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHKLZXCVBNM!@#$%^&*"
    try:
# input from user and we use try/except to eliminate ValueError(we can use only numbers because is int not letters)
        lenght = int(input("how many chars? - "))
    except ValueError:
        print("Sorry, you can use only numbers, not letters !")
        return gen(website)
# here we open the function read()
    passwords = read()
# random password generator
    password = ""
    for c in range(lenght):
        password += random.choice(chars)
    print(password)
# dict passwords asociezi "key-ului" o valoare(in cazul nostru un sir de caractere)
    passwords[website] = password
# open the file for writing, and saving
    with open("withstatement.txt", "w") as w:
        w.write(json.dumps(passwords))
        print(passwords)

# show() function to read dict after saving dates(key,value pair)
def show(website):
    with open("withstatement.txt", "r") as s:
        content = json.loads(s.read())
        print(content[website]) 


# main() function to ask INPUT from user wich command will use from bash
def main():
# input from bash
    command = sys.argv[1]
# to use just "instructions argument from bash only"
    if len(sys.argv) < 3:
        instructions(command)
        return 
# input from bash
    website = sys.argv[2]

    if command == "gen":
        gen(website)
    elif command == "show":
        show(website)
    elif command == "instructions":
        instructions(command)
    else:
        print("invalid command ")
main()

    
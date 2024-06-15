import random
import string

def generatePassword(pwlengths):
    passwords = []

    for length in pwlengths:
        password = generate_single_password(length)
        passwords.append(password)

    return passwords

def generate_single_password(length):
    alphabet = string.ascii_lowercase
    password = ''.join(random.choice(alphabet) for _ in range(length))
    
    password = replaceWithNumber(password)
    password = replaceWithUppercaseLetter(password)
    
    return password

def replaceWithNumber(pword):
    for _ in range(random.randint(1, 3)): 
        pword = pword[:replace_index] + str(random.randint(0, 9)) + pword[replace_index + 1:]
    return pword

def replaceWithUppercaseLetter(pword):
    for _ in range(random.randint(1, 3)):  
        replace_index = random.randrange(len(pword) // 2, len(pword))
        pword = pword[:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]
    return pword

def main():
    numPasswords = int(input("How many passwords do you want to generate? "))
    print(f"Generating {numPasswords} passwords")

    passwordLengths = []

    print("Minimum length of password should be 3")

    for i in range(numPasswords):
        length = int(input(f"Enter the length of Password #{i+1}: "))
        if length < 3:
            length = 3
        passwordLengths.append(length)

    passwords = generatePassword(passwordLengths)

    for i, password in enumerate(passwords):
        print(f"Password #{i+1} = {password}")

if __name__ == "__main__":
    main()

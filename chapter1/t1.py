# requires: py -m pip install random-words
# by acided aka bogdan4ik cutie <3
from random_word import RandomWords

random = RandomWords()
rand_word = random.get_random_word()
secret = "_" * len(rand_word)
count = 0
print(rand_word)
print(secret)
def main():
    global secret
    global count
    if secret == rand_word:
        print("You got it!")
        exit()
    print()
    user_letter = input("Enter a letter: ").lower()

    if len(user_letter) == 1:
        if user_letter in secret:
            print("Already guessed!")
            print(secret)
        elif user_letter in rand_word:
            new = ""
            for i in range(len(rand_word)):
                if rand_word[i] == user_letter:
                    new += user_letter
                else:
                    new += secret[i]
            secret = new
            print(secret)
        else:
            count += 1
            killer(count)

    elif len(user_letter) > 1:
        print("Please write only one letter")

    else:
        print("Empty string!")

def killer(count):
    if count == 1:
        print('''
          0
        ''')
    elif count == 2:
        print('''
          0
          |
        ''')
    elif count == 3:
        print('''
          0
         -|
        ''')
    elif count == 4:
        print('''
          0
         -|-
        ''')
    elif count == 5:
        print('''
          0
         -|-
         /
        ''')
    elif count == 6:
        print('''
          0
         -|-
         / \ 
        ''')
        print("He is dead! You killed him!")
        print("You are going to prison!")
        exit()

while True:
    main()
# requires: py -m pip install Random-Word-Generator
# by aciede aka bogdan4ik cutie <3
from RandomWordGenerator import RandomWord

max_len = int(input("Enter password length: "))
rw = RandomWord(max_word_size=max_len,
                constant_word_size=True,
                include_digits=True,
                special_chars=r"@_!#$%^&*()<>?/\|}{~:",
                include_special_chars=True)

print(rw.generate())
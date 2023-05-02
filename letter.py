from unicodedata import name


letter = '''Dear <|Name|>
Greetings from ABC coding house.I am happy to
tell you about your selection.

You are selected!
Have a great day ahead!
Thanks and regards,
Raj
Date : <|Date|>'''

name = input("Enter your name : ")
date = input("Enter date : ")
letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)